import os
from PIL import Image, ImageOps

class PillowEffects:
    def __init__(self, image_path: str, folder_name: str):
        self.image = Image.open(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  # create output directory

    def show_image(self):
        """Display the original image"""
        self.image.show()

    def invert_colors(self, filename: str):
        """Create and save an inverted color version of the image"""
        inverted = ImageOps.invert(self.image)
        path = f"{self.folder_name}/{filename}"
        inverted.save(path)
        print(f"✅ Inverted image saved as {path}")
        return inverted

    def show_side_by_side(self, img1: Image.Image, img2: Image.Image, output_name: str):
        """Display two images side by side, resizing them proportionally and padding with black"""
        #Let's set the target height according to the image with the largest height
        target_height = max(img1.height, img2.height)

        # Proportional reduction (thumbnail)
        def resize_with_padding(img, target_height):
            ratio = target_height / img.height
            new_width = int(img.width * ratio)
            resized = img.resize((new_width, target_height))

            # New black background (RGB, black background)
            background = Image.new("RGB", (new_width, target_height), (0, 0, 0))
            background.paste(resized, (0, 0))
            return background

        img1_resized = resize_with_padding(img1, target_height)
        img2_resized = resize_with_padding(img2, target_height)

        total_width = img1_resized.width + img2_resized.width
        combined = Image.new("RGB", (total_width, target_height), (0, 0, 0))
        combined.paste(img1_resized, (0, 0))
        combined.paste(img2_resized, (img1_resized.width, 0))

        path = f"{self.folder_name}/{output_name}"
        combined.save(path)
        print(f"📷 Combined image saved as {path}")
        combined.show()


def main():
    image_path = "sample.jpg"
    folder_name = "processed_images"
    pe = PillowEffects(image_path, folder_name)

    original = pe.image
    inverted = pe.invert_colors("inverted_sample.jpg")

    pe.show_side_by_side(original, inverted, "side_by_side.jpg")


if __name__ == "__main__":
    main()
