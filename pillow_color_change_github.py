from PIL import Image
import os
import numpy as np

class ColorChange:
    
    def __init__(self, image_path: str, folder_name: str):
        
        self.image = Image.open(image_path).convert("RGBA")  # Convert image to RGBA format
        self.image_data = np.array(self.image)  # Convert image to a NumPy array
        self.folder_name = folder_name
        os.makedirs(self.folder_name, exist_ok=True)  # Create output folder if it doesn't exist

    def change_color(self, r_range: tuple[int, int], g_range: tuple[int, int], b_range: tuple[int, int], new_color: tuple[int, int, int, int]):
        """
        Change the pixels within the specified RGB range to a new color.
        r_range: (min_R, max_R) - Red channel range
        g_range: (min_G, max_G) - Green channel range
        b_range: (min_B, max_B) - Blue channel range
        new_color: (R, G, B, A) - Target color
        """

        # Create a copy of the image data
        new_image_data = self.image_data.copy()

        # Generate a mask for pixels within the specified RGB range
        mask = (
            (new_image_data[:, :, 0] >= r_range[0]) & (new_image_data[:, :, 0] <= r_range[1]) &  # Red range
            (new_image_data[:, :, 1] >= g_range[0]) & (new_image_data[:, :, 1] <= g_range[1]) &  # Green range
            (new_image_data[:, :, 2] >= b_range[0]) & (new_image_data[:, :, 2] <= b_range[1])    # Blue range
        )
        
        # Apply the new color to the selected pixels
        new_image_data[mask] = new_color

        # Convert the modified data back to an image
        self.image = Image.fromarray(new_image_data, "RGBA")

    def save_image(self, filename: str):
        
        path = os.path.join(self.folder_name, filename)
        self.image.save(path)
        print(f"✅ Color-changed image saved at: {path}")

def main():
    
    image_path = "sample.jpg" 
    folder_name = "color_changed_image"

    # Define the target pink-purple color range (RGB Min-Max)
    r_range = (150, 255)  # Red between 150 and 255
    g_range = (0, 100)    # Green between 0 and 100
    b_range = (150, 255)  # Blue between 150 and 255

    # Define the new color (Orange: RGBA)
    new_color = (255, 148, 8, 255)  # #ff9408

    cc = ColorChange(image_path=image_path, folder_name=folder_name)
    cc.change_color(r_range, g_range, b_range, new_color)
    cc.save_image("color_changed_img.png")

if __name__ == "__main__":
    main()
