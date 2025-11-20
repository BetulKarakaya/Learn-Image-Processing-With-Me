from functools import cached_property
from PIL import Image
from pathlib import Path

class ImageAnalyzer:
    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = Image.open(self.image_path)

    @cached_property
    def total_pixels(self):
        """Expensive computation executed ONLY once."""
        print("Calculating total pixels...")
        width, height = self.image.size
        return width * height

    @cached_property
    def aspect_ratio(self):
        """Another cached expensive calculation."""
        print("Calculating aspect ratio...")
        w, h = self.image.size
        return round(w / h, 2)

    def show_info(self):
        print(f"- File: {self.image_path.name}")
        print(f"- Resolution: {self.image.size}")
        print(f"- Total Pixels: {self.total_pixels}")
        print(f"- Aspect Ratio: {self.aspect_ratio}")

def main():
    analyzer = ImageAnalyzer("sample.jpg")

    analyzer.show_info()

    # These two calls will NOT re-run the calculations (cached!)
    print("\nCalling again...")
    print(analyzer.total_pixels)
    print(analyzer.aspect_ratio)

if __name__ == "__main__":
    main()
