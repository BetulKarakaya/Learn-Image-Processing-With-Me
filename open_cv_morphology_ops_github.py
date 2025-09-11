import cv2
import os
import numpy as np
import tkinter as tk


class MorphologyOps:
    def __init__(self, image_path: str, folder_name: str):
        self.image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Get screen size
        root = tk.Tk()
        root.withdraw() # Hide the TK window
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

    def _resize_with_padding(self, img, target_size):
        """
        Resize image keeping aspect ratio, add black padding to fit target size.
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
        padded = cv2.copyMakeBorder(resized, top, bottom, left, right,
                                    cv2.BORDER_CONSTANT, value=(0, 0, 0))
        return padded

    def show_comparison(self, eroded, dilated, win_name="Original vs Erosion vs Dilation"):
        """
        Show Original, Eroded, and Dilated images side by side,
        scaled to screen size.
        """
       # Equal space for three images → let's divide the screen into 3 parts
        target_w = self.screen_w // 3
        target_h = self.screen_h

        original_resized = self._resize_with_padding(self.image, (target_w, target_h))
        eroded_resized = self._resize_with_padding(eroded, (target_w, target_h))
        dilated_resized = self._resize_with_padding(dilated, (target_w, target_h))

        combined = np.hstack((original_resized, eroded_resized, dilated_resized))

        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_name, combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def erosion(self, kernel_size=(5, 5), iterations=1, save_name="eroded.png"):
        kernel = np.ones(kernel_size, np.uint8)
        eroded = cv2.erode(self.image, kernel, iterations=iterations)
        path = f"{self.folder_name}/{save_name}"
        cv2.imwrite(path, eroded)
        print(f"✅ Eroded image saved as {path}")
        return eroded

    def dilation(self, kernel_size=(5, 5), iterations=1, save_name="dilated.png"):
        kernel = np.ones(kernel_size, np.uint8)
        dilated = cv2.dilate(self.image, kernel, iterations=iterations)
        path = f"{self.folder_name}/{save_name}"
        cv2.imwrite(path, dilated)
        print(f"✅ Dilated image saved as {path}")
        return dilated

    def explain_morphology(self):
        print("Morphological Operations:")
        print("- Erosion: Removes pixels on object boundaries → shrinks objects.")
        print("- Dilation: Adds pixels to object boundaries → enlarges objects.")
        print("Often used in noise removal, edge detection, or shape analysis.")


def main():
    image_path = "sample.jpg"
    folder_name = "morphology_results"

    mo = MorphologyOps(image_path, folder_name)

    # Apply Erosion & Dilation
    eroded_img = mo.erosion(kernel_size=(5, 5), iterations=1)
    dilated_img = mo.dilation(kernel_size=(5, 5), iterations=1)

    # Show full screen comparison
    mo.show_comparison(eroded_img, dilated_img)

    mo.explain_morphology()


if __name__ == "__main__":
    main()
