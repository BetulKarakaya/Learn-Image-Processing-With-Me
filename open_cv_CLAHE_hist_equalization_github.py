import cv2
import os
import numpy as np

class CLAHEMethod:
    def __init__(self, image_path: str, folder_name: str, filename: str, upscale=False):
        self.image_path = image_path
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"⚠️ Image not found at path: {self.image_path}")
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  # Create folder if it doesn't exist
        self.filename = filename
        self.upscale = upscale
        self.is_gray = self.image.shape[2] == 1 or np.array_equal(self.image[..., 0], self.image[..., 1]) and np.array_equal(self.image[..., 1], self.image[..., 2])

    def enhance_image(self):
        if self.is_gray:
            self.low_light_grayscale()  # Process the image if it's grayscale
        else:
            self.low_light_colorful()  # Process the image if it's colorful

        if self.upscale:
            self.enhanced_image = self.upscale_with_opencv(self.enhanced_image)

    def low_light_grayscale(self):
        gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)  # Convert image to grayscale
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))  # Create CLAHE object for enhancement
        enhanced = clahe.apply(gray)  # Apply CLAHE to the grayscale image
        self.enhanced_image = cv2.cvtColor(enhanced, cv2.COLOR_GRAY2BGR)  # Convert back for consistency

    def low_light_colorful(self):
        # Convert BGR to YCrCb (for colorful images)
        ycrcb = cv2.cvtColor(self.image, cv2.COLOR_BGR2YCrCb)
        y, cr, cb = cv2.split(ycrcb)  # Split the channels

        # Enhance only the luminance (Y) channel using CLAHE
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(6, 6))
        y_clahe = clahe.apply(y)

        # Merge the enhanced Y channel back with the Cr and Cb channels
        ycrcb_clahe = cv2.merge([y_clahe, cr, cb])
        enhanced = cv2.cvtColor(ycrcb_clahe, cv2.COLOR_YCrCb2BGR)

        # Apply slight lighting enhancement
        self.enhanced_image = cv2.addWeighted(enhanced, 1, self.image, 0, 0)

    def upscale_with_opencv(self, image, scale_factor=2):
        # Upscale the image using OpenCV's resize method
        h, w = image.shape[:2]
        new_dim = (int(w * scale_factor), int(h * scale_factor))
        return cv2.resize(image, new_dim, interpolation=cv2.INTER_CUBIC)

    def show(self):
        # Show the enhanced image in a window
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("image", self.enhanced_image)

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC key
                break
            elif key == ord('s'):  # 's' key to save the image
                self.save()

        cv2.destroyAllWindows()

    def save(self):
        # Save the enhanced image to the specified path
        path = os.path.join(self.folder_name, self.filename)
        cv2.imwrite(path, self.enhanced_image)
        print(f"✅ Enhanced image saved: {path}")

def main():
    print("="*50)
    print("🖌️  Welcome to Low Light Image Enhancement Tool")
    print("-" * 50)
    print("🎨 Controls:")
    print(" [s] Save the image")
    print(" [ESC] Exit the program")
    print("="*50)

    image_path = "test_2.jpg"
    folder_name = "open_cv_enhanced_images"
    
    app = CLAHEMethod(image_path=image_path, folder_name=folder_name, filename="lighted_test2.jpg", upscale=True)
    app.enhance_image()  # Enhance the image
    app.show()  # Display the image

if __name__ == "__main__":
    main()
