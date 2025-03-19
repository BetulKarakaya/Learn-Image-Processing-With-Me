import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class PillowBasics:
    def __init__(self, image_path: str):
        self.image = Image.open(image_path)
        os.makedirs("edited_images", exist_ok=True)  #Create Directory

    def show_image(self):
        self.image.show()

    def resize_image(self, new_size: tuple, filename: str):
        resized = self.image.resize(new_size)
        path = f"edited_images/{filename}"
        resized.save(path)
        print(f"✅ Resized image saved as {path}")

    def crop_image(self, box: tuple, filename: str):
        cropped = self.image.crop(box)
        path = f"edited_images/{filename}"
        cropped.save(path)
        print(f"✅ Cropped image saved as {path}")

    def rotate_image(self, angle: int, filename: str):
        rotated = self.image.rotate(angle, expand=True)
        path = f"edited_images/{filename}"
        rotated.save(path)
        print(f"✅ Rotated image saved as {path}")

    def flip_image(self, mode: str, filename: str):
        if mode == "horizontal":
            flipped = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        elif mode == "vertical":
            flipped = self.image.transpose(Image.FLIP_TOP_BOTTOM)
        else:
            raise ValueError("Mode must be 'horizontal' or 'vertical'")
        
        path = f"edited_images/{filename}"
        flipped.save(path)
        print(f"✅ Flipped image saved as {path}")

    def apply_filter(self, filter_type: str, filename: str):
        filters = {
            "blur": ImageFilter.BLUR,
            "contour": ImageFilter.CONTOUR,
            "sharpen": ImageFilter.SHARPEN
        }
        if filter_type not in filters:
            raise ValueError("Filter must be 'blur', 'contour', or 'sharpen'")
        
        filtered = self.image.filter(filters[filter_type])
        path = f"edited_images/{filename}"
        filtered.save(path)
        print(f"✅ Filtered image saved as {path}")

    def convert_to_grayscale(self, filename: str):
        grayscale = self.image.convert("L")
        path = f"edited_images/{filename}"
        grayscale.save(path)
        print(f"✅ Grayscale image saved as {path}")

    def add_text(self, text: str, position: tuple, filename: str):
        image_copy = self.image.copy()
        draw = ImageDraw.Draw(image_copy)

        try:
            font = ImageFont.truetype("arial.ttf", 200)
        except IOError:
            font = ImageFont.load_default()

        draw.text(position, text, fill="white", font=font)
        path = f"edited_images/{filename}"
        image_copy.save(path)
        print(f"✅ Image with text saved as {path}")

    def access_pixels(self, x: int, y: int):
        pixel_value = self.image.getpixel((x, y))
        print(f"🔍 Pixel at ({x}, {y}): {pixel_value}")
        return pixel_value

def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg"  
    pb = PillowBasics(image_path)

    pb.show_image()
    pb.resize_image((300, 300), "resized.jpg")
    pb.crop_image((50, 50, 300, 300), "cropped.jpg")
    pb.rotate_image(45, "rotated.jpg")
    pb.flip_image("horizontal", "flipped.jpg")
    pb.apply_filter("sharpen", "sharpened.jpg")
    pb.apply_filter("blur", "blur.jpg")
    pb.convert_to_grayscale("grayscale.jpg")
    pb.add_text("Hello, World! I'm Betül", (500, 500), "text_added.jpg")
    pb.access_pixels(100, 100)

if __name__ == "__main__":
    main()
