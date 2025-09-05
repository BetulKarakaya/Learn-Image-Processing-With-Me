import os
from PIL import Image

class PillowFormats:
    def __init__(self, image_path: str, folder_name: str):
        self.image = Image.open(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  # Create Directory

    def show_image(self):
        self.image.show()

    def convert_and_save(self, filename: str, format: str):
        """
        Convert the source image to a new format and save.
        """
        path = f"{self.folder_name}/{filename}"
        self.image.save(path, format=format)
        print(f"✅ Image saved successfully as {path}")

    def explain_supported_formats(self):
        """
        Pillow Supported Formats
        Fully Supported (Read + Write): JPEG, PNG, BMP, GIF, TIFF, WebP, ICO, etc.
        Read-Only Formats: CUR, PSD, QOI, FLI, MPO, etc. (can open but not save)
        Write-Only Formats: PDF, PALM, XV Thumbnails (can save but not open)
        """
        print("-Fully Supported: JPEG, PNG, BMP, GIF, TIFF, WebP, ICO ...")
        print("-Read-Only: CUR, PSD, QOI, FLI, MPO ...")
        print("-Write-Only: PDF, PALM, XV Thumbnails ...")


def main():
    # Example: Base image in BMP format
    image_path = "sample.jpg"
    folder_name = "converted_images"
    pf = PillowFormats(image_path, folder_name)

    pf.show_image()
    pf.convert_and_save("output_image.gif", format="GIF")  # Fully supported example
    pf.explain_supported_formats()

    # ⚠️ Trying to save as PSD (read-only) would fail
    # pf.convert_and_save("example.psd", format="PSD")

    # ⚠️ Trying to open PDF (write-only) would fail
    # img = Image.open("example.pdf")


if __name__ == "__main__":
    main()
