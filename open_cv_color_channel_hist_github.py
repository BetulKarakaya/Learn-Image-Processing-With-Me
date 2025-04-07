import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

class Histogram:
    def __init__(self, image_path: str):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")
        self.color = ("b", "g", "r")

    def human_format(self, num):
        """Y ekseni değerlerini K, M, B gibi daha okunabilir hale getirir."""
        for unit in ['', 'K', 'M', 'B']:
            if abs(num) < 1000.0:
                return f"{num:.0f}{unit}"
            num /= 1000.0
        return f"{num:.0f}T"

    def color_channel_hist(self):
        plt.figure(figsize=(10, 5))
        max_val = 0

        for i, col in enumerate(self.color):
            hist = cv2.calcHist([self.image], [i], None, [256], [0, 256])
            max_val = max(max_val, np.max(hist))  # En büyük değerleri kontrol et
            plt.plot(hist, color=col, label=f'{col.upper()} channel')

        plt.title("Color Channel Histogram")
        plt.xlabel("Pixel Intensity")
        plt.ylabel("Number of Pixels")
        plt.xlim([0, 256])
        plt.grid(axis="y", linestyle='--', alpha=0.5)
        plt.legend()

        # Eğer değerler büyükse, y etiketlerini daha okunabilir formatta göster
        if max_val >= 1e5:
            formatter = FuncFormatter(lambda x, _: self.human_format(x))
            plt.gca().yaxis.set_major_formatter(formatter)

        plt.tight_layout()
        plt.show()

def main():
    image_path = "sample.jpg"
    hist_app = Histogram(image_path=image_path)
    hist_app.color_channel_hist()

if __name__ == "__main__":
    main()
