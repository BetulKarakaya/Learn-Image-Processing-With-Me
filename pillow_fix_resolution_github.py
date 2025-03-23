import os
from PIL import Image, ImageEnhance

#Photo by <a href="https://unsplash.com/@mianismusic?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Myan Nguyen</a> on <a href="https://unsplash.com/photos/gray-concrete-road-between-green-trees-during-daytime-D9SJWE89GyU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>

class ImageResolution:
    def __init__(self, folder_name:str, image_path:str):
        self.image = Image.open(image_path)
        self.folder_name = folder_name
        self.image_path =image_path
        os.makedirs(self.folder_name, exist_ok=True)  #Create Directory

    def show_image(self):
        self.image.show()

    def higger_resolution(self):
        enhancer = ImageEnhance.Sharpness(self.image)
        sharpened_image = enhancer.enhance(2.2) 
        enhancer = ImageEnhance.Contrast(sharpened_image)
        contrast_image = enhancer.enhance(1.2)
        enhancer = ImageEnhance.Color(contrast_image)
        self.final_image = enhancer.enhance(1.3)


    def save_with_resolution(self,filename:str):
        path = f"{self.folder_name}/{filename}"
        self.final_image.save(path, quality=100) 
        print(f"✅ Higher resolution image saved as {path} (Default quality is 95)")

    def save_with_dpi(self,filename:str):
        path = f"{self.folder_name}/{filename}"
        self.final_image.save(path, dpi=(300, 300))
        print(f"✅ Higher dpi image saved as {path} (Default dpi is 75)")

def main():
    #Photo by <a href="https://unsplash.com/@mianismusic?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Myan Nguyen</a> on <a href="https://unsplash.com/photos/gray-concrete-road-between-green-trees-during-daytime-D9SJWE89GyU?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash">Unsplash</a>
    image_path = "low_resolution_sample.jpg" 
    folder_name = "higger_resolution"
    pillow_resolution = ImageResolution(image_path=image_path, folder_name=folder_name)
    pillow_resolution.higger_resolution()
    pillow_resolution.save_with_resolution("save_with_resolution.jpg")
    pillow_resolution.save_with_dpi("save_with_dpi.jpg")

   
if __name__ == "__main__":
    main()