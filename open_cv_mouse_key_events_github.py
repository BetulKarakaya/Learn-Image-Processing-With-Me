import numpy as np
import cv2
import os

class MouseAndKeyBoard:
    def __init__(self, image_path: str, output_folder: str):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

        self.screen_width = 1920 
        self.screen_height = 1080
        self.x_first, self.y_first = 0, 0
        self.x_last, self.y_last = 0, 0
        self.shape = "circle"  # default shape

    def drawfunction(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_first, self.y_first = self.convert_to_original_coords(x, y, self.resized_shape, self.padding)
        
        elif event == cv2.EVENT_LBUTTONUP:
            self.x_last, self.y_last = self.convert_to_original_coords(x, y, self.resized_shape, self.padding)
            self.draw()


    def draw(self):
        if self.shape == "circle":
            center = (self.x_first, self.y_first)
            radius = int(np.linalg.norm(np.array([self.x_last, self.y_last]) - np.array([self.x_first, self.y_first])))
            cv2.circle(self.image, center, radius, (255, 0, 0), -1)
        elif self.shape == "rectangle":
            cv2.rectangle(self.image, (self.x_first, self.y_first), (self.x_last, self.y_last), (0, 255, 0), -1)
        elif self.shape == "line":
            cv2.line(self.image, (self.x_first, self.y_first), (self.x_last, self.y_last), (0, 0, 255), 2)
    
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

    def convert_to_original_coords(self, x, y, resized_shape, padding):
        resized_w, resized_h = resized_shape
        left, top = padding
        original_h, original_w = self.image.shape[:2]

        scale_w = original_w / resized_w
        scale_h = original_h / resized_h

        x = (x - left) * scale_w
        y = (y - top) * scale_h

        return int(x), int(y)

    def show(self):
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback('image', self.drawfunction)

        while True:
           # Resize bilgilerini al
            resized = self.resize_with_aspect_ratio(self.image, self.screen_width, self.screen_height)
            padded = self.pad_to_center(resized, (self.screen_width, self.screen_height))
            padding_left = (self.screen_width - resized.shape[1]) // 2
            padding_top = (self.screen_height - resized.shape[0]) // 2

            self.resized_shape = resized.shape[1], resized.shape[0]  # width, height
            self.padding = (padding_left, padding_top)

            cv2.imshow('image', padded)

            key = cv2.waitKey(1) & 0xFF

            if key == ord('1'):
                self.shape = 'rectangle'
                print("Shape set to rectangle")
            elif key == ord('2'):
                self.shape = 'line'
                print("Shape set to line")
            elif key == ord('3'):
                self.shape = 'circle'
                print("Shape set to circle")
            elif key == ord('s'):
                self.save("open_cv_drawn_image.jpg")
            elif key == 27:  # ESC key
                break

        cv2.destroyAllWindows()
    
    def save(self, filename: str):
        path = os.path.join(self.output_folder, filename)
        cv2.imwrite(path, self.image)
        print(f"✅ Image saved: {path}")

def main():
    print("="*50)
    print("🖌️  Welcome to Interactive Drawing Tool")
    print("-" * 50)
    print("🎨 Controls:")
    print("    [1] Draw Rectangle")
    print("    [2] Draw Line")
    print("    [3] Draw Circle")
    print("    [s] Save the image")
    print(" [ESC] Exit the program")
    print("="*50)
    print("👉 Click and drag with the left mouse button to draw")
    print("")

    # Image path and output directory
    image_path = "sample.jpg"
    folder_name = "edited_images"
    
    app = MouseAndKeyBoard(image_path=image_path, output_folder=folder_name)
    app.show()


if __name__ == "__main__":
    main()
