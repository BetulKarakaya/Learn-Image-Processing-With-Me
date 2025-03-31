import cv2
import matplotlib.pyplot as plt

class ImageProcessor:
    def __init__(self, image_path: str):
        
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")

        # Convert BGR to RGB for proper color display
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

    def show_image(self):
        # Use matplotlib for high-quality display
        plt.figure(figsize=(8, 6))  
        plt.imshow(self.image)
        plt.axis("off")  
        plt.show()

def main():
    image_path = "sample.jpg"
    processor = ImageProcessor(image_path)
    processor.show_image()

if __name__ == "__main__":
    main()
