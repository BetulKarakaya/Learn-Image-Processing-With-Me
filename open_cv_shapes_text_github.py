import cv2
import numpy as np
import os

class ShapeAndText:
    def __init__(self, image_path: str, output_folder: str):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)  # Create output folder if not exists

    # COLOR IN BGR FORMAT
    def draw_line(self, start_point: tuple[int, int], end_point: tuple[int, int], color: tuple[int, int, int], thickness: float = 1):
        cv2.line(self.image, start_point, end_point, color, thickness)

    def draw_circle(self, center: tuple[int, int], radius: int, color: tuple[int, int, int], thickness: float = 1):
        cv2.circle(self.image, center, radius, color, thickness)

    def draw_ellipse(self, center: tuple[int, int], axes: tuple[int, int], angle: int, color: tuple[int, int, int],
                     start_angle: int = 0, end_angle: int = 360, thickness: float = 1):
        cv2.ellipse(self.image, center, axes, angle, start_angle, end_angle, color, thickness)

    def draw_rectangle(self, left_top_corner: tuple[int, int], right_bottom_corner: tuple[int, int], color: tuple[int, int, int], thickness: int = 1):
        cv2.rectangle(self.image, left_top_corner, right_bottom_corner, color, thickness)

    def draw_polygon(self, points: list[tuple[int, int]], color: tuple[int, int, int], thickness: int = 1, is_filled: bool = False):
        #True ----> fill the ploygon
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))  # Convert to format suitable for OpenCV
        if is_filled:
            cv2.fillPoly(self.image, [pts], color)
        else:
            cv2.polylines(self.image, [pts], isClosed=True, color=color, thickness=thickness)

    def add_text(self, text: str, position: tuple[int, int], font_scale: float = 1, color: tuple[int, int, int] = (255, 255, 255),
                 thickness: int = 2, font=cv2.FONT_HERSHEY_SIMPLEX):
        
        cv2.putText(self.image, text, position, font, font_scale, color, thickness)

    def save(self, filename: str):
        path = os.path.join(self.output_folder, filename)
        cv2.imwrite(path, self.image)
        print(f"✅ Image saved: {path}")

def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg"  
    folder_name = "edited_images" 
    editor = ShapeAndText(image_path, folder_name)

    editor.draw_line((50, 50), (2780, 50), (0, 255, 0), 10)
    editor.draw_rectangle((100, 100), (1800, 1800), (255, 0, 0), 10)
    editor.draw_circle((4000, 3000), 50, (0, 0, 255), 35)
    editor.draw_ellipse((4000, 2000), (800, 400), 30, (255, 255, 0), 0, 360, 10)

    triangle_points = [(1500, 4000), (1000, 5000), (2000, 5000)]
    editor.draw_polygon(triangle_points, (255,255,255), 20)

    star_points = [(2500, 4000), (2300, 4600), (1800, 4600), (2200, 4900), (2000, 5400),
                   (2500, 5100), (3000, 5400), (2800, 4900), (3200, 4600), (2700, 4600)]
    editor.draw_polygon(star_points, (0, 165, 255), thickness=2, is_filled=True)

    editor.add_text("Hello, OpenCV!", (50, 5500), font_scale=20, color=(255, 255, 255), thickness=10)

    editor.save("open_cv_edited_image.jpg")

if __name__ == "__main__":
    main()
