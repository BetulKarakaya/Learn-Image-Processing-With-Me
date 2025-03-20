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

## Setup

1. **Install Pillow**: You need to install the Pillow library to work with image files.

2. **Image Files**: Ensure that you have an image (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) for testing. You can use any image or download one from free image sources like Pexels or Unsplash.

3. **Directory Structure**: The program creates an `edited_images` folder to save all processed images. Ensure the script has permission to create files and folders.

## Usage

1. Clone or download the repository.
2. Place your image file (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) in the project directory.
3. Run the script.

```bash
python pillow_basics_github.py
```

The script will:

- Show the original image.
- Perform various transformations on the image and save the results as new files in the **edited_images** folder.

```bash
python pillow_enhanced_images_github.py
```

The script will:

- Show the original image.
- It manipulates the brightness, contrast, color levels, and sharpness of an image and save the results as new files in the **enhanced_images** folder.


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
