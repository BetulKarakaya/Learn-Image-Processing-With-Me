from PIL import Image, ImageDraw, ImageFont
import os

class PillowText:
    def __init__(self, image_path: str, folder_name: str):
        self.image = Image.open(image_path).convert("RGBA") 
        self.empty_image = Image.new("RGBA", (1920, 1080), color=(255, 255, 255, 255))
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  

    def write_text(self, image: Image, position: tuple, text: str, filepath: str, opacity: int):
       
        txt_layer = Image.new("RGBA", image.size, (255, 255, 255, 0))

        drawing = ImageDraw.Draw(txt_layer)
        font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 80)
        drawing.text(position, text, fill=(0, 0, 0, opacity), font= font)
        combined = Image.alpha_composite(image, txt_layer)

        
        combined = combined.convert("RGB")
        combined.save(f"{self.folder_name}/{filepath}", quality=100)
        print(f"✅ {filepath} saved.")

    def run(self):
      
        self.write_text(self.image, (50, 50), "Hello World", "full_ink_image.jpg", 255)
        self.write_text(self.image, (50, 100), "Hello World", "faded_ink_image.jpg", 150)

       
        self.write_text(self.empty_image, (50, 50), "Hello World", "full_ink_empty.jpg", 255)
        self.write_text(self.empty_image, (50, 100), "Hello World", "faded_ink_empty.jpg", 150)

def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg"
    folder_name = "text_images"
    pt = PillowText(image_path=image_path, folder_name=folder_name)
    pt.run()

if __name__ == "__main__":
    main()
