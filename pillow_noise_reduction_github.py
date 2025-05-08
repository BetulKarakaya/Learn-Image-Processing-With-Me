import os
from PIL import Image, ImageFilter

class NoiseReduction:
    def __init__(self, image_path:str, folder_name:str):
        self.image = Image.open(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  #Create Directory

    def noise_reduction(self, kernel_size:int=3):
        # Apply median filter with a kernel size 
        self.filtered_image = self.image.filter(ImageFilter.MedianFilter(size=kernel_size))

    def show(self):
        self.filtered_image.show()

    def save(self, file_name:str):
        path = f"{self.folder_name}/{file_name}"
        self.filtered_image.save(path, dpi=(300, 300))
        print(f"✅ Noise removed image saved as {path}")

def main():
    image_path = "noise.jpg" 
    folder_name = "enhanced_images"
    app = NoiseReduction(image_path= image_path,folder_name=folder_name )
    app.noise_reduction(kernel_size=3)
    app.save(file_name="noise_reduction.jpg")
    app.show()

if __name__ == "__main__":
    main()