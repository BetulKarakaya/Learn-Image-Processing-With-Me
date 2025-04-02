from PIL import Image, ImageEnhance
import os

class BatchImageEditor:
    def __init__(self, input_folder: str, output_folder: str, resize_size: tuple[int, int], rotation: int, crop_box: tuple[int, int, int, int], contrast_factor: float):
       
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.resize_size = resize_size
        self.rotation = rotation
        self.crop_box = crop_box
        self.contrast_factor = contrast_factor

        os.makedirs(self.output_folder, exist_ok=True)  # Create output folder if not exists

    def process_images(self):
        """Process all images in the input folder."""
        for filename in os.listdir(self.input_folder):
            if filename.lower().endswith((".jpg", ".jpeg", ".png")):
                input_path = os.path.join(self.input_folder, filename)
                output_path = os.path.join(self.output_folder, f"edited_{filename}")

                # Load image
                image = Image.open(input_path)

                # Apply transformations
                image = image.resize(self.resize_size)  # Resize
                image = image.rotate(self.rotation)  # Rotate
                image = image.crop(self.crop_box)  # Crop
                image = ImageEnhance.Contrast(image).enhance(self.contrast_factor)  # Adjust contrast

                # Save processed image
                image.save(output_path)
                print(f"✅ Processed and saved: {output_path}")

def main():
    input_folder = "input_images"  # Folder containing images
    output_folder = "output_images"  # Folder to save edited images
    resize_size = (500, 500)  # Resize to 500x500 pixels
    rotation_angle = 30  # Rotate images by 30 degrees
    crop_box = (50, 50, 450, 450)  # Crop area (left, upper, right, lower)
    contrast_factor = 1.5  # Increase contrast by 1.5x

    editor = BatchImageEditor(input_folder, output_folder, resize_size, rotation_angle, crop_box, contrast_factor)
    editor.process_images()

if __name__ == "__main__":
    main()


#Photo: Jean-Daniel Francoeur: https://www.pexels.com/tr-tr/fotograf/30936133/
#Photo: lauriphoto: https://www.pexels.com/tr-tr/fotograf/31263848/
#Photo: berobscura: https://www.pexels.com/tr-tr/fotograf/30650040/