import cv2
import matplotlib.pyplot as plt
import os

class ImageResizer:
    def __init__(self, image_path: str, scale: float, output_folder: str = "edited_images"):
        
        self.image = cv2.imread(image_path)
        if self.image is None:
            raise FileNotFoundError("⚠️ Image not found. Check the path.")

        # Convert BGR to RGB for correct color representation
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2RGB)

        # Resize the image
        self.resized_image = cv2.resize(self.image, None, fx=scale, fy=scale, interpolation=cv2.INTER_LINEAR)
        
        # Create output folder if not exists
        os.makedirs(output_folder, exist_ok=True)
        self.output_folder = output_folder
        self.image_path = image_path  # Store original path for naming

    def show_images(self):
        
        plt.figure(figsize=(10, 6))
        plt.imshow(self.image)
        plt.title("Original Image")
        plt.axis("off")
        plt.show()

        #Show resized image in a smaller figure
        plt.figure(figsize=(6, 4))
        plt.imshow(self.resized_image)
        plt.title("Resized Image")
        plt.axis("off")
        plt.show()

    def save_resized_image(self):
        filename = os.path.basename(self.image_path)
        save_path = os.path.join(self.output_folder, f"opencv_resized_{filename}")
        
        # Convert RGB back to BGR before saving
        cv2.imwrite(save_path, cv2.cvtColor(self.resized_image, cv2.COLOR_RGB2BGR))
        print(f"✅ Resized image saved at: {save_path}")

def main():
    image_path = "sample.jpg"
    scale_factor = 0.5  # Resize to 50% of original size
    
    resizer = ImageResizer(image_path, scale_factor)
    resizer.show_images()
    resizer.save_resized_image()

if __name__ == "__main__":
    main()
