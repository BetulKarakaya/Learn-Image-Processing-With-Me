import os
from PIL import Image, ImageEnhance

class PillowBasics:
    def __init__(self, image_path: str, folder_name: str):
        self.image = Image.open(image_path)
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  #Create Directory

    def show_image(self):
        self.image.show()

    def brighten_image(self, filename:str, enhance_factor:float = 2):
        #Enhance Factor 0 ---> Full Black Image
        #Enhance Factor 1 ---> Original Image
        current_image = ImageEnhance.Brightness(self.image)
        brigthen_image = current_image.enhance(enhance_factor)
        path = f"{self.folder_name}/{filename}"
        brigthen_image.save(path)
        print(f"✅ Brigthen image saved as {path}")

    def color_image(self, filename:str, enhance_factor:float = 2):
        #Enhance Factor 0 ---> Black & White Image (Greyscale Image)
        #Enhance Factor 1 ---> Original Image
        current_image = ImageEnhance.Color(self.image)
        color_image = current_image.enhance(enhance_factor)
        path = f"{self.folder_name}/{filename}"
        color_image.save(path)
        print(f"✅ Color level editted image saved as {path}")
    
    def contrast_image(self, filename:str, enhance_factor:float = 2):
        #Enhance Factor 0 ---> Full Grey Image
        #Enhance Factor 1 ---> Original Image
        current_image = ImageEnhance.Contrast(self.image)
        contrast_image = current_image.enhance(enhance_factor)
        path = f"{self.folder_name}/{filename}"
        contrast_image.save(path)
        print(f"✅ Contrast level editted image saved as {path}")

    def sharped_image(self, filename:str, enhance_factor:float = 2):
        current_image = ImageEnhance.Sharpness(self.image)
        sharped_image = current_image.enhance(enhance_factor)
        path = f"{self.folder_name}/{filename}"
        sharped_image.save(path)
        print(f"✅ Sharped image saved as {path}")


def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg" 
    folder_name = "enhanced_images"
    pb = PillowBasics(image_path, folder_name)

    pb.show_image()
    pb.brighten_image("brighten_3.jpg",enhance_factor = 3)
    pb.color_image("color_level_3.jpg",enhance_factor = 3)
    pb.contrast_image("contrast_3.jpg", enhance_factor = 3)
    pb.sharped_image("sharped_3.jpg", enhance_factor = 3)

    pb.brighten_image("brighten_0.jpg",enhance_factor = 0)
    pb.color_image("color_level_0.jpg",enhance_factor = 0)
    pb.contrast_image("contrast_0.jpg", enhance_factor = 0)
    pb.sharped_image("sharped_0.jpg", enhance_factor = 0)

if __name__ == "__main__":
    main()
