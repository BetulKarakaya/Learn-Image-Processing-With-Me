import numpy as np
import cv2
import os

class MouseAndKeyBoard:
    def __init__(self, image_path: str, output_folder: str):
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")
        self.output_folder = output_folder
        os.makedirs(self.output_folder, exist_ok=True)

        self.x_first, self.y_first = 0, 0
        self.x_last, self.y_last = 0, 0
        self.shape = "circle"  # default shape

    def drawfunction(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.x_first = x
            self.y_first = y
        elif event == cv2.EVENT_LBUTTONUP:
            self.x_last = x
            self.y_last = y
            self.draw()

    def draw(self):
        if self.shape == "circle":
            center = (self.x_first, self.y_first)
            radius = int(np.linalg.norm(np.array([self.x_last, self.y_last]) - np.array([self.x_first, self.y_first])))
            cv2.circle(self.image, center, radius, (255, 0, 0), -1)
        elif self.shape == "rectangle":
            cv2.rectangle(self.image, (self.x_first, self.y_first), (self.x_last, self.y_last), (0, 255, 0), -1)
        elif self.shape == "line":
            cv2.line(self.image, (self.x_first, self.y_first), (self.x_last, self.y_last), (0, 0, 255), 2)

    def show(self):
        cv2.namedWindow("image", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.setMouseCallback('image', self.drawfunction)

        while True:
            cv2.imshow('image', self.image)
            key = cv2.waitKey(1) & 0xFF

            if key == ord('1'):
                self.shape = 'rectangle'
                print("Shape set to rectangle")
            elif key == ord('2'):
                self.shape = 'line'
                print("Shape set to line")
            elif key == ord('3'):
                self.shape = 'circle'
                print("Shape set to circle")
            elif key == ord('s'):
                self.save("open_cv_drawn_image.jpg")
            elif key == 27:  # ESC key
                break

        cv2.destroyAllWindows()

    def save(self, filename: str):
        path = os.path.join(self.output_folder, filename)
        cv2.imwrite(path, self.image)
        print(f"✅ Image saved: {path}")

def main():
    print("="*50)
    print("🖌️  Welcome to Interactive Drawing Tool")
    print("-" * 50)
    print("🎨 Controls:")
    print("    [1] Draw Rectangle")
    print("    [2] Draw Line")
    print("    [3] Draw Circle")
    print("    [s] Save the image")
    print(" [ESC] Exit the program")
    print("="*50)
    print("👉 Click and drag with the left mouse button to draw")
    print("")

    # Image path and output directory
    image_path = "sample.jpg"
    folder_name = "edited_images"
    
    app = MouseAndKeyBoard(image_path=image_path, output_folder=folder_name)
    app.show()


if __name__ == "__main__":
    main()
