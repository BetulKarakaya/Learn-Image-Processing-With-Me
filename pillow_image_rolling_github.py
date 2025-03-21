import os
from PIL import Image, ImageEnhance

class PillowRolling:
    def __init__(self, image_path: str, folder_name: str, sub_img_size:tuple):
        self.image = Image.open(image_path)
        self.sub_img_size = sub_img_size
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  #Create Directory

    def show_image(self):
        self.image.show()

    def resize_image(self):
        self.resized_image = self.image.resize(self.sub_img_size)
    
    def rolling_and_merging(self, filename: str):
        new_image = Image.new("RGB",(self.image.width, self.image.height))
        for i in range((self.image.width // self.sub_img_size[0]) +1):
            for j in range((self.image.height // self.sub_img_size[1])+1):
                new_x = i*self.sub_img_size[0]
                new_y = j *self.sub_img_size[1]
                new_image.paste(self.resized_image, (new_x, new_y ))
        
        path = f"{self.folder_name}/{filename}"
        new_image.save(path)
        print(f"✅ Rolled image saved as {path}")

def main():
    #Photo: Ekam Juneja: https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/
    image_path = "sample.jpg" 
    folder_name = "rolled_image"
    sub_img_size = (600,600)
    pb = PillowRolling(image_path=image_path,folder_name=folder_name,sub_img_size=sub_img_size)

    pb.show_image()
    pb.resize_image()
    pb.rolling_and_merging("rolled.jpg")

if __name__ == "__main__":
    main()