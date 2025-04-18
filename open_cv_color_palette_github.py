import cv2
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

class MyColorPalette:
    def __init__(self, image_path: str, num_colors: int = 5):
        self.image_path = image_path
        self.num_colors = num_colors
        self.image = cv2.imread(self.image_path)
        if self.image is None:
            raise FileNotFoundError(f"⚠️ Image not found: {self.image_path}")
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    def extract_palette(self):
        reshaped_image = self.image.reshape((-1, 3))

        print("Colors are being analyzed...")
        kmeans = KMeans(n_clusters=self.num_colors, n_init=10)
        kmeans.fit(reshaped_image)

        self.colors = kmeans.cluster_centers_.astype(int)
        self.percentages = np.bincount(kmeans.labels_) / len(kmeans.labels_)

    def show_palette(self):
        if not hasattr(self, "colors"):
            raise Exception("⚠️ First call the `extract palette()` method")

        palette = np.zeros((100, 500, 3), dtype=np.uint8)

        start = 0
        for idx, (color, percent) in enumerate(zip(self.colors, self.percentages)):
            end = start + int(percent * 500)
            palette[:, start:end, :] = color
            start = end

        plt.figure(figsize=(8, 4))
        plt.imshow(palette)
        plt.axis("off")
        plt.title("Color Palette", fontsize=14, fontweight="bold")
        plt.show()

    def get_palette_as_hex(self):
        hex_colors = ['#%02x%02x%02x' % tuple(color) for color in self.colors]
        return hex_colors

    def run(self):
        self.extract_palette()
        self.show_palette()
        
        print("🌈 Palette Hex Codes :")
        for hex_code in self.get_palette_as_hex():
            print(f"  {hex_code}")
def main():
    print("=" * 60)
    print("Welcome to Color Palette Analyzer App")
    print("📷 The most dominant colors are analyzed for you through the visual...")
    print("=" * 60)

    image_path = "sample.jpg"
    num_colors = 6

    palette_app = MyColorPalette(image_path=image_path, num_colors=num_colors)
    palette_app.run()
    
if __name__ == "__main__":
    main()
