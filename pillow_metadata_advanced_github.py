from PIL import Image
from PIL.ExifTags import TAGS
from pathlib import Path

class ExifMetadataExtractor:
    def __init__(self, image_path: str):
        self.image_path = Path(image_path)
        self.image = Image.open(self.image_path)

    def display_exif_data(self):
        """Extract and display all available EXIF metadata"""
        # Extract EXIF data
        exif_data = self.image.getexif()
        if not exif_data:
            print("❌ No EXIF metadata found.")
            return

        print(f"📂 EXIF Metadata for: {self.image.filename}\n")
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            print(f"{tag_name:25}: {value}")


def main():
    # Note: Not all images contain EXIF metadata. 
    # - Photos taken by cameras/phones usually include EXIF (date, model, GPS, etc.).  
    # - Screenshots or images downloaded from the internet often have EXIF removed.  
    # - Editing tools and social media apps may strip EXIF data during compression.  
    # - EXIF is mainly supported in JPEG/JPG and some TIFF formats, but rarely in PNG or GIF.  
    
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg" 
    extractor = ExifMetadataExtractor(image_path=image_path)
    extractor.display_exif_data()


if __name__ == "__main__":
    main()
