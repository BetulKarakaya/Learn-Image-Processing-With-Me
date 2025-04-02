# Image Processing with Pillow

This project demonstrates basic and advanced image processing techniques using the Python **Pillow** library. It includes various operations such as resizing, cropping, rotating, flipping, applying filters, converting to grayscale, adding text, accessing pixel data, and enhancing images using the **ImageEnhance** module. The project is designed to explore and apply essential image manipulation tasks that can be expanded further as new features are added.
## Features

- **Resize Image**: Change the dimensions of an image.
- **Crop Image**: Crop a specific region from the image.
- **Rotate Image**: Rotate the image by a given angle.
- **Flip Image**: Flip the image either horizontally or vertically.
- **Apply Filter**: Apply different image filters like blur, contour, and sharpen.
- **Convert to Grayscale**: Convert the image to grayscale.
- **Add Text**: Add customizable text onto the image.
- **Access Pixels**: Retrieve pixel values at specific coordinates.
- **Enhance Image**: Adjust brightness, contrast, sharpness, and color balance.
- **Image Rolling**: 
- **Draw Shapes**: Create a blank image with a background color and draw basic shapes such as lines, rectangles, circles, and polygons.
- **Rolling Image**: Resize an image and create a repeated pattern to fill a new canvas.
- **Fix Low Image Resolution**: Enhances the resolution and quality of low-resolution images using the Pillow library.
- **Batch Image Processing**: Process multiple images at once with resizing, cropping, rotating, and contrast enhancement.


## Setup

1. **Install Pillow**: You need to install the Pillow library to work with image files.

2. **Image Files**: Ensure that you have an image (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) for testing. You can use any image or download one from free image sources like Pexels or Unsplash.

3. **Directory Structure**: The program creates an `edited_images` folder to save all processed images. Ensure the script has permission to create files and folders.

## Usage


1. Clone or download the repository.
2. Place your image file (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) in the project directory.
3. Run the scripts.
   
### **Basic Image Processing**
```bash
python pillow_basics_github.py
```

The script will:

- Show the original image.
- Perform various transformations on the image and save the results as new files in the **edited_images** folder.

### **Image Enhancement**
To manipulate brightness, contrast, color levels, and sharpness, run:
```bash
python pillow_enhanced_images_github.py
```

The script will:

- Show the original image.
- It manipulates the brightness, contrast, color levels, and sharpness of an image and save the results as new files in the **enhanced_images** folder.

### **Drawing Shapes on an Image**
To create an image with a background color and draw shapes (lines, rectangles, circles, polygons), run:

```bash
python pillow_drawings_github.py
```
This script will:

- Create a blank image with a specified background color.
- Draw various shapes on the image.
- Save the image in the **edited_images** folder.

### **Rolling Image**
To create an image where a resized version of the original is repeated across the canvas, run:

```bash
python pillow_image_rolling_github.py
```
This script will:

- Resize the image to a specified smaller size.
- Repeatedly paste this resized image to fill the entire original canvas.
- Save the output in the **rolled_image** folder.

### **High-Resolution Image Enhancement**
This script enhances the resolution and quality of low-resolution images using the Pillow library. It applies sharpening, contrast enhancement, and color adjustment to improve image clarity. The enhanced images can be saved with high quality or increased DPI (dots per inch) for better print resolution.

```bash
python pillow_fix_resolution_github.py
```
This script will:

- Enhance image sharpness, contrast, and color vibrancy
- Save the image with maximum quality settings
- Save the image with high DPI (300 DPI) for printing purposes
- Save the output in the **higger_resolution** folder.

###  **Color Change Tool**
This script allows you to **replace specific colors in an image** based on an RGB range. It uses **Pillow** and **NumPy** to detect pixels within a given color range and replace them with a new color. 

```bash
python pillow_color_change_github.py
```

This script will:

- Load the Image – Opens the input image and converts it to **RGBA** format.
- Define the Color Range – Specify the **RGB min-max values** to detect specific colors.
- Apply the Color Change – Replaces pixels in the defined range with a **new RGBA color**.
- Save the Processed Image – Stores the modified image in the `color_changed_image` folder.

### **Batch Image Processing**
To apply transformations (resize, rotate, crop, adjust contrast) to multiple images in a folder, run:

```bash
python pillow_batch_image_github.py
```
The script will:

- Load all images from the input_images folder.
- Resize images to 500x500 pixels.
- Rotate images by 30 degrees.
- Crop images to a specific region (50,50 to 450,450).
- Enhance contrast by a factor of 1.5.
- Save processed images in the output_images folder.
#### Resources of input_images folder:
- [Pexels Image of Jean-Daniel Francoeur](https://www.pexels.com/tr-tr/fotograf/30936133/)
- [Pexels Image of lauriphoto](https://www.pexels.com/tr-tr/fotograf/31263848/)
- [Pexels Image of berobscura](https://www.pexels.com/tr-tr/fotograf/30650040/)

## Example Outputs
- Resized image (resized.jpg)
- Cropped image (cropped.jpg)
- Rotated image (rotated.jpg)
- Flipped image (flipped.jpg)
- Filtered image (sharpened.jpg, blur.jpg)
- Grayscale image (grayscale.jpg)
- Image with added text (text_added.jpg)
- Brightness-enhanced image (brighten_3.jpg)
- Contrast-adjusted image (contrast_3.jpg)
- Sharpness-enhanced image (sharped_3.jpg)
- Color-enhanced image (color_level_3.jpg)
- Image with drawn shapes (drawing.jpg)
- Batch processed images (saved in output_images/edited_*.jpg)

## Future Work
This project will be expanded to include more advanced image processing techniques, such as:

- Object detection
- Edge detection
- Image transformation (perspective correction, skewing)
- Batch processing of multiple images

## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests with new features or improvements. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
