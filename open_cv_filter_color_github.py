import cv2
import os
import numpy as np
import tkinter as tk


class ColorFilter:
    def __init__(self, image_path: str, folder_name: str = "color_filter_results"):
        """
        Initialize with an image path and create output folder.
        Load the image in BGR and get screen size for display.
        """
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")
        
        # HSV range for blue (default)
        self.lower_color = np.array([60, 35, 140])
        self.upper_color = np.array([180, 255, 255])

        # Get screen size
        root = tk.Tk()
        root.withdraw()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

    def _resize_with_padding(self, img, target_size):
        """
        Resize image keeping aspect ratio and add black padding to fit target size.
        """
        h, w = img.shape[:2]
        target_w, target_h = target_size

        scale = min(target_w / w, target_h / h)
        new_w, new_h = int(w * scale), int(h * scale)
        resized = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)

        top = (target_h - new_h) // 2
        bottom = target_h - new_h - top
        left = (target_w - new_w) // 2
        right = target_w - new_w - left

        padded = cv2.copyMakeBorder(
            resized, top, bottom, left, right,
            cv2.BORDER_CONSTANT, value=(0, 0, 0)
        )
        return padded

    def apply_filter(self):
        """
        Convert image to HSV, create mask, and filter selected color.
        Returns (mask, result).
        """
        hsv = cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower_color, self.upper_color)
        result = cv2.bitwise_and(self.image, self.image, mask=mask)

        # Save results
        cv2.imwrite(f"{self.folder_name}/original.png", self.image)
        cv2.imwrite(f"{self.folder_name}/mask.png", mask)
        cv2.imwrite(f"{self.folder_name}/result.png", result)

        print(f"✅ Filtered results saved in: {self.folder_name}")
        return mask, result

    def show_comparison(self, mask, result, win_name="Original vs Mask vs Result"):
        """
        Show Original, Mask, and Result images side by side in full screen.
        """
        # We are converting the single channel mask into a 3 channel one
        mask_bgr = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        target_w = self.screen_w // 3
        target_h = self.screen_h

        frame_resized = self._resize_with_padding(self.image, (target_w, target_h))
        mask_resized = self._resize_with_padding(mask_bgr, (target_w, target_h))
        result_resized = self._resize_with_padding(result, (target_w, target_h))

        combined = np.hstack((frame_resized, mask_resized, result_resized))

        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_name, combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


    def explain_filter(self):
        """
        Print explanation of color filtering.
        """
        print("📘 Color Filtering with OpenCV:")
        print("- Convert BGR image to HSV (Hue, Saturation, Value).")
        print("- Define lower and upper range for a color (default: Blue).")
        print("- Create mask to isolate regions within range.")
        print("- Apply mask → get filtered result.")


def main():
    image_path = "sample.jpg"
    folder_name = "color_filter_results"

    cf = ColorFilter(image_path, folder_name)

    # Apply filter
    mask, result = cf.apply_filter()

    # Show full screen comparison
    cf.show_comparison(mask, result)

    # Explain process
    cf.explain_filter()


if __name__ == "__main__":
    main()
