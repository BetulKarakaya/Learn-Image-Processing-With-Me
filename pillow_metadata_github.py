from PIL import Image
from pathlib import Path

class ImageMetadataExtractor:
    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = Image.open(self.image_path)

    def display_metadata(self):
        print("📂 Filename:", self.image.filename)
        print("📏 Image Size:", self.image.size)
        print("↕️ Height:", self.image.height)
        print("↔️ Width:", self.image.width)
        print("🖼️ Format:", self.image.format)
        print("🎨 Mode:", self.image.mode)
        if hasattr(self.image, "is_animated"):
            print("🎞️ Animated:", self.image.is_animated)
            print("🖼️ Frame Count:", self.image.n_frames)


def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg" 
    extractor = ImageMetadataExtractor(image_path)
    extractor.display_metadata()


if __name__ == "__main__":
    main()
