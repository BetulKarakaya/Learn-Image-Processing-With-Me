import os
from PIL import Image

class GIFMaker:
    def __init__(self, image_folder: str):
        self.image_folder = image_folder
        self.output_folder = os.path.join(self.image_folder, "outputs")
        os.makedirs(self.output_folder, exist_ok=True)

        valid_extensions = (".png", ".jpg", ".jpeg", ".bmp")
        self.image_paths = sorted([
            os.path.join(self.image_folder, f)
            for f in os.listdir(self.image_folder)
            if f.lower().endswith(valid_extensions) and os.path.isfile(os.path.join(self.image_folder, f))
        ])

        if not self.image_paths:
            raise FileNotFoundError("⚠️ No image found in the folder.")

        # Open the first image and set its size to canvas
        first_image = Image.open(self.image_paths[0]).convert("RGBA")
        self.canvas_size = first_image.size

        # Center other images
        self.image_list = [self.center_image(Image.open(path)) for path in self.image_paths]

    def center_image(self, img):
        img = img.convert("RGBA")
        canvas = Image.new("RGBA", self.canvas_size, (0, 0, 0, 0))
        img_w, img_h = img.size
        canvas_w, canvas_h = self.canvas_size
        offset = ((canvas_w - img_w) // 2, (canvas_h - img_h) // 2)
        canvas.paste(img, offset, img if img.mode == "RGBA" else None)
        return canvas

    def create_gif(self, output_name="output.gif", duration=100):
        output_path = os.path.join(self.output_folder, output_name)

        self.image_list[0].save(
            output_path,
            save_all=True,
            append_images=self.image_list[1:], 
            duration=duration,
            loop=0,
            disposal=2,
            transparency=0
        )

        print(f"✅ : The animated GIF file has been created and saved successfully{output_path}")

def main():
    app = GIFMaker(image_folder="gif_images")
    app.create_gif()

if __name__ == "__main__":
    main()
