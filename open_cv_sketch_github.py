import cv2

class PencilSketchStudio:
    def __init__(self, image_path):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError(f"⚠️ Image not found: {image_path}")

        self.window_name = "🎨 Pencil Sketch Studio"
        self.running = True

        # Resize image to fit screen and add black padding if needed
        self.image = self.resize_with_padding(self.image)

        # Create window and trackbars
        cv2.namedWindow(self.window_name)
        cv2.createTrackbar("Blur Kernel", self.window_name, 21, 99, lambda x: None)
        cv2.createTrackbar("Divide Scale", self.window_name, 256, 512, lambda x: None)

    def resize_with_padding(self, img):
        screen_width = 1280
        screen_height = 720

        h, w = img.shape[:2]
        scale = min(screen_width / w, screen_height / h)
        new_w, new_h = int(w * scale), int(h * scale)

        resized = cv2.resize(img, (new_w, new_h))
        result = cv2.copyMakeBorder(
            resized,
            top=(screen_height - new_h) // 2,
            bottom=(screen_height - new_h + 1) // 2,
            left=(screen_width - new_w) // 2,
            right=(screen_width - new_w + 1) // 2,
            borderType=cv2.BORDER_CONSTANT,
            value=[0, 0, 0]  # Black padding
        )
        return result

    def run(self):
        while self.running:
            if cv2.getWindowProperty(self.window_name, cv2.WND_PROP_VISIBLE) < 1:
                # Window was closed manually (X button)
                break

            gray = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)

            # Get trackbar values
            k = cv2.getTrackbarPos("Blur Kernel", self.window_name)
            s = cv2.getTrackbarPos("Divide Scale", self.window_name)
            if k % 2 == 0:  # Gaussian kernel size must be odd
                k += 1

            # Pencil sketch effect
            blur = cv2.GaussianBlur(gray, (k, k), 0)
            sketch = cv2.divide(gray, blur, scale=s)

            cv2.imshow(self.window_name, sketch)

            key = cv2.waitKey(30)
            if key == 27:  # ESC key
                break

        cv2.destroyAllWindows()


if __name__ == "__main__":
    print("="*50)
    print("🎨 Welcome to Pencil Sketch Studio")
    print("- Use the sliders to adjust the effect")
    print("- Press ESC to exit or close the window")
    print("="*50)

    app = PencilSketchStudio("sample.jpg")
    app.run()
