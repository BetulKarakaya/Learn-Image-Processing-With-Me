import numpy as np
import cv2 
import os

def nothing(x):
    pass

class Trackbar:
    def __init__(self, image_path: str, output_folder: str):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)
        self.screen_width = 1920 
        self.screen_height = 1080
    
    def resize_with_aspect_ratio(self, image, max_width, max_height):
        h, w = image.shape[:2]
        scale = min(max_width / w, max_height / h)
        new_size = (int(w * scale), int(h * scale))
        return cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)

    def pad_to_center(self, image, target_size):
        target_w, target_h = target_size
        h, w = image.shape[:2]
        top = (target_h - h) // 2
        bottom = target_h - h - top
        left = (target_w - w) // 2
        right = target_w - w - left
        return cv2.copyMakeBorder(image, top, bottom, left, right, cv2.BORDER_CONSTANT, value=(0, 0, 0))

    def show(self):
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        # Create trackbars
        cv2.createTrackbar('Contrast','image',10,20,nothing)      # alpha = 0.0 - 2.0
        cv2.createTrackbar('Brightness','image',50,100,nothing)   # beta = 0 - 100
        cv2.createTrackbar('Gaussian Blur','image',0,20,nothing)  # kernel size

        while True:
            edited_image = self.image.copy()

            alpha = cv2.getTrackbarPos('Contrast','image') / 10
            beta = cv2.getTrackbarPos('Brightness','image')
            blur = cv2.getTrackbarPos('Gaussian Blur','image')

            # Contrast and Brightness
            edited_image = cv2.convertScaleAbs(edited_image, alpha=alpha, beta=beta)

            # Apply Gaussian Blur (only if blur > 1 and odd)
            if blur % 2 == 0:
                blur += 1
            if blur > 1:
                edited_image = cv2.GaussianBlur(edited_image, (blur, blur), 0)

           # Resize and pad to fullscreen without stretching
            resized = self.resize_with_aspect_ratio(edited_image, self.screen_width, self.screen_height)
            padded = self.pad_to_center(resized, (self.screen_width, self.screen_height))
            cv2.imshow('image', padded)


            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            elif key == ord('s'):
                self.save("open_cv_enhancement_image.jpg", edited_image)

        cv2.destroyAllWindows()

    def save(self, filename: str, image_to_save=None):
        path = os.path.join(self.output_folder, filename)
        if image_to_save is None:
            image_to_save = self.image
        cv2.imwrite(path, image_to_save)
        print(f"✅ Image saved: {path}")

def main():
    print("="*50)
    print("🖌️  Welcome to Interactive Image Enhancement Tool")
    print("-" * 50)
    print("🎨 Controls:")
    print(" Use trackbars to adjust Contrast, Brightness and Blur.")
    print(" [s] Save the image")
    print(" [ESC] Exit the program")
    print("="*50)

    image_path = "sample.jpg"
    folder_name = "edited_images"
    
    app = Trackbar(image_path=image_path, output_folder=folder_name)
    app.show()

if __name__ == "__main__":
    main()
