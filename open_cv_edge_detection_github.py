import numpy as np
import cv2
import os


class EdgeDetection:
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

    def detect_edges(self):
        self.edges = cv2.Canny(self.image,100,200)
    
    def show(self):
        # Detect edges
        self.detect_edges()

        # Convert side view to BGR format (cv2.imshow() to display side by side)
        edges_bgr = cv2.cvtColor(self.edges, cv2.COLOR_GRAY2BGR)

        # Scale original and edge image proportionally
        resized_original = self.resize_with_aspect_ratio(self.image, self.screen_width // 2, self.screen_height)
        resized_edges = self.resize_with_aspect_ratio(edges_bgr, self.screen_width // 2, self.screen_height)

        # If the dimensions are not equal, resize them to the same height.
        if resized_original.shape[0] != resized_edges.shape[0]:
            height = min(resized_original.shape[0], resized_edges.shape[0])
            resized_original = cv2.resize(resized_original, (resized_original.shape[1], height))
            resized_edges = cv2.resize(resized_edges, (resized_edges.shape[1], height))

        # Combine side by side
        combined = cv2.hconcat([resized_original, resized_edges])

        # Padding to center the screen
        final_image = self.pad_to_center(combined, (self.screen_width, self.screen_height))

        # Display
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow("image", final_image)

        while True:
            key = cv2.waitKey(1) & 0xFF
            if key == 27:  # ESC
                break
            elif key == ord('s'):
                self.save("open_cv_edge_of_image.jpg")

        cv2.destroyAllWindows()

    
    def save(self, filename: str):
        path = os.path.join(self.output_folder, filename)
        cv2.imwrite(path, self.edges)
        print(f"✅ Edge image saved: {path}")


def main():
    print("="*50)
    print("🖌️  Welcome to Interactive Image Enhancement Tool")
    print("-" * 50)
    print("🎨 Controls:")
    print(" Use trackbars to adjust Contrast, Brightness and Blur.")
    print(" [s] Save the image")
    print(" [ESC] Exit the program")
    print("="*50)

#Photo by <a href="https://unsplash.com/@mianismusic?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Myan Nguyen</a> on <a href="https://unsplash.com/photos/gray-concrete-road-between-green-trees-during-daytime-D9SJWE89GyU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

    image_path = "low_resolution_sample.jpg"
    folder_name = "edited_images"
    
    app = EdgeDetection(image_path=image_path, output_folder=folder_name)
    app.show()

if __name__ == "__main__":
    main()
