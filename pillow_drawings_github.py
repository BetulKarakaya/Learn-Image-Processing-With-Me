from PIL import Image, ImageDraw

class ImageDrawing:
    def __init__(self, saving_path:str, size: tuple, background_color: str):
        self.image = Image.new("RGB", size, background_color)
        self.draw = ImageDraw.Draw(self.image)
        self.saving_path = saving_path

    def draw_line(self, start: tuple, end: tuple, color: str, width: int = 5):
        self.draw.line([start, end], fill=color, width=width)

    def draw_rectangle(self, top_left: tuple, bottom_right: tuple, color: str, outline_width: int = 5, fill_color:str = None):
        self.draw.rectangle([top_left, bottom_right], fill=fill_color, outline=color, width=outline_width)

    def draw_circle(self, center: tuple, radius: int,color: str, outline_width: int = 5,  fill_color:str = None):
        x0, y0 = center[0] - radius, center[1] - radius
        x1, y1 = center[0] + radius, center[1] + radius
        self.draw.ellipse([x0, y0, x1, y1], fill = fill_color, outline=color, width=outline_width)

    def draw_polygon(self, points: list, color: str, outline_width: int = 5, fill_color:str = None):
        self.draw.polygon(points, fill=fill_color, outline=color, width=outline_width)

    def save_image(self):
        self.image.save(self.saving_path)
        print(f"✅ Drawing saved as {self.saving_path}")

def main():
    image_path = "drawing.jpg" 
    folder_name = "edited_images"
    path = f"{folder_name}/{image_path}"
    pillow_draw = ImageDrawing(saving_path=path, size=(500, 500), background_color="#c0f1fc")

    pillow_draw.draw_line((50, 451), (450, 451), color="green", width=5)
    pillow_draw.draw_rectangle((100, 250), (400, 450), color="blue", outline_width=5)
    pillow_draw.draw_circle((80, 80), radius=50, color="#fffb0d", outline_width=5, fill_color= "#fffb0d")
    pillow_draw.draw_polygon([(100, 249), (250, 150), (400, 249)], color="red", outline_width=5, fill_color= "red")

    pillow_draw.save_image()

if __name__ == "__main__":
    main()
