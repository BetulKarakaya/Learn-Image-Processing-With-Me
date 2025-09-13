import cv2
import os
import numpy as np
import tkinter as tk


class DenoiseImage:
    def __init__(self, image_path: str, folder_name: str = "denoise_results"):
        """
        Initialize with an image path and create output folder.
        Load the image in color and get screen size for display.
        """
        self.image = cv2.imread(image_path, cv2.IMREAD_COLOR)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)

        if self.image is None:
            raise FileNotFoundError(f"❌ Image not found at {image_path}")

        # Get screen size
        root = tk.Tk()
        root.withdraw()
        self.screen_w = root.winfo_screenwidth()
        self.screen_h = root.winfo_screenheight()

    def _resize_with_padding(self, img:np.ndarray, target_size:tuple[int,int]):
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

    def apply_denoise(self, h:int=8, hColor:int=8, templateWindowSize:int=7, searchWindowSize:int=15):
        """
        Apply Non-Local Means denoising and save result.
        """
        denoised = cv2.fastNlMeansDenoisingColored(
            self.image, None, h, hColor, templateWindowSize, searchWindowSize
        )
        path = f"{self.folder_name}/denoised.png"
        cv2.imwrite(path, denoised)
        print(f"✅ Denoised image saved as {path}")
        return denoised

    def show_comparison(self, denoised:np.ndarray, win_name:str="Original vs Denoised"):
        """
        Show Original and Denoised images side by side in full screen.
        """
        target_w = self.screen_w // 2
        target_h = self.screen_h

        original_resized = self._resize_with_padding(self.image, (target_w, target_h))
        denoised_resized = self._resize_with_padding(denoised, (target_w, target_h))

        combined = np.hstack((original_resized, denoised_resized))

        cv2.namedWindow(win_name, cv2.WINDOW_NORMAL)
        cv2.setWindowProperty(win_name, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow(win_name, combined)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def explain_denoising(self):
        
        print("Image Denoising with OpenCV:")
        print("- Uses Non-Local Means denoising algorithm.")
        print("- Removes noise while preserving edges and details.")
        print("- Parameters control filter strength and neighborhood sizes.")


def main():
    image_path = "bird.jpg"
    folder_name = "denoise_results"

    dn = DenoiseImage(image_path, folder_name)

    # Apply denoising
    denoised_img = dn.apply_denoise()

    # Show full screen comparison
    dn.show_comparison(denoised_img)

    # Explain process
    dn.explain_denoising()


if __name__ == "__main__":
    main()
