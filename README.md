# Image Processing with Pillow

This project demonstrates basic and advanced image processing techniques using the Python **Pillow** and **OpenCV** libraries. It includes various operations such as resizing, cropping, rotating, flipping, applying filters, converting to grayscale, adding text, accessing pixel data, drawing shapes, and enhancing images. It also includes a **Super Resolution** module to upscale low-resolution images using deep learning models.

## 📂 Project Structure

```bash
├── edited_images/              # Stores images edited with Pillow
├── enhanced_images/            # Stores brightness/contrast/sharpness edits
├── rolled_image/               # Stores repeated pattern images
├── higger_resolution/          # Stores Pillow-enhanced resolution images
├── color_changed_image/        # Output for replaced color images
├── output_images/              # Batch processed images
├── input_images/               # Sample input images from Pexels
├── SuperResolution/
│   ├── models/                 # Pre-trained .pb models (LapSRN, ESPCN, etc.)
│   ├── low_resolution/         # Example low-res image(s)
│   ├── super_resolve.py        # Script for enhancing low-res images
│   └── README.md               # Details about models and license
├── pillow_basics_github.py     # Pillow basic manipulations
├── pillow_enhanced_images_github.py
├── open_cv_trackbar_enhancement_github.py
├── pillow_drawings_github.py
├── pillow_image_rolling_github.py
├── pillow_fix_resolution_github.py
├── pillow_color_change_github.py
├── pillow_batch_image_github.py
├── open_cv_mouse_key_events_github.py
├── open_cv_shapes_text_github.py
├── open_cv_edge_detection_github.py
└── README.md                
```

---

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
- **Noise Reduction**: Removes the noice from an image using the ImageFilter.MedianFilter()
- **Batch Image Processing**: Process multiple images at once with resizing, cropping, rotating, and contrast enhancement.
- **Edge Detection**: Detects the edges of the image using OpenCv.
- **Super Resolution (Deep Learning Upscaling)**: AI-assisted image enhancement with OpenCV.


## Setup

1. **Install Pillow**:
   You need to install the Pillow library to work with image files.
   💻 Installation (Recommended):
   ```bash
   pip install pillow
   ```
3. **Install OpenCV:**
You need to install the OpenCV (cv2) library with contrib modules to access advanced functionalities like super resolution (DNN module), trackbars, interactive drawing, and edge detection.

💻 Installation (Recommended):
```bash
pip install opencv-contrib-python
```

3. **Image Files**: Ensure that you have an image (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) for testing. You can use any image or download one from free image sources like Pexels or Unsplash.

4. **Directory Structure**: The program creates an `edited_images` folder to save all processed images. Ensure the script has permission to create files and folders.

## Usage


1. Clone or download the repository.
2. Place your image file (e.g., [sample.jpg](https://www.pexels.com/tr-tr/fotograf/dinamik-isik-efektleriyle-soyut-portre-31208192/) ) in the project directory.
3. Run the scripts.
   
### 📸 **Basic Image Processing**
```bash
python pillow_basics_github.py
```

The script will:

- Show the original image.
- Perform various transformations on the image and save the results as new files in the **edited_images** folder.

### ✨ **Image Enhancement**
To manipulate brightness, contrast, color levels, and sharpness, run:
```bash
python pillow_enhanced_images_github.py
```
```bash
python open_cv_trackbar_enhancement_github.py
```

The script will:
- Pillow Version:
   - Show the original image.
   - It manipulates the brightness, contrast, color levels, and sharpness of an image and save the results as new files in the **enhanced_images** folder.
- OpenCV version:
  - Display an image in fullscreen mode with interactive controls
  - Provide real-time adjustment of:
     - Contrast (via trackbar, scaled between 0.0 and 2.0)
     - Brightness (via trackbar, scaled between 0 and 100)
     - Gaussian Blur (adjustable blur intensity with odd kernel sizes)
  - Apply all effects live while you adjust the sliders
  - Save the enhanced image by pressing the s key
  - Exit the tool anytime by pressing the ESC key
  - Automatically create an output folder if it doesn't exist
  - Maintain original image untouched; all edits are based on a copy

### 🧠 Super Resolution Module with OpenCV

The `SuperResolution/` folder contains:

- ✅ Low-resolution example image(s)
- ✅ Code to upscale using `cv2.dnn_superres`
- ✅ Pre-trained models (LapSRN, ESPCN, FSRCNN)
- ❌ EDSR models not included due to GitHub file size limits

You can run:

```bash
python SuperResolution/super_resolve.py
```
The script will:
- Load the selected super-resolution model (e.g., ESPCN, LapSRN, or EDSR) in .pb format.
- Read a low-resolution input image from the low_resolution_images folder.
- Automatically detect model scaling factor (e.g., ×2, ×4).
- Upscale the input image using the specified deep learning model.
- Display the original and enhanced images side by side for visual comparison.
- Allow the user to save the enhanced image in the super_resolution_outputs folder by pressing the s key.
- Exit the image display window with the ESC key.

#### Model Source & License

Model files originate from the [OpenCV dnn_superres](https://github.com/opencv/opencv_contrib) module.  
They are shared under the **Apache 2.0 License**.  
More details are in `SuperResolution/models/README.md`.


### 🟣🟪 **Drawing Shapes on an Image**
To create an image with a background color and draw shapes (lines, rectangles, circles, polygons), run:

```bash
python open_cv_shapes_text_github.py
```
or

```bash
python pillow_drawings_github.py
```

This script will:

- Create a blank image with a specified background color. (pillow) or draws on the given file (open_cv)
- Draw various shapes on the image.
- Save the image in the **edited_images** folder.

### 🎞️ **Rolling Image**
To create an image where a resized version of the original is repeated across the canvas, run:

```bash
python pillow_image_rolling_github.py
```
This script will:

- Resize the image to a specified smaller size.
- Repeatedly paste this resized image to fill the entire original canvas.
- Save the output in the **rolled_image** folder.

### 🖼️ **High-Resolution Image Enhancement**
This script enhances the resolution and quality of low-resolution images using the Pillow library. It applies sharpening, contrast enhancement, and color adjustment to improve image clarity. The enhanced images can be saved with high quality or increased DPI (dots per inch) for better print resolution.

```bash
python pillow_fix_resolution_github.py
```
This script will:

- Enhance image sharpness, contrast, and color vibrancy
- Save the image with maximum quality settings
- Save the image with high DPI (300 DPI) for printing purposes
- Save the output in the **higger_resolution** folder.

### 🎨 **Color Change Tool**
This script allows you to **replace specific colors in an image** based on an RGB range. It uses **Pillow** and **NumPy** to detect pixels within a given color range and replace them with a new color. 

```bash
python pillow_color_change_github.py
```

This script will:

- Load the Image – Opens the input image and converts it to **RGBA** format.
- Define the Color Range – Specify the **RGB min-max values** to detect specific colors.
- Apply the Color Change – Replaces pixels in the defined range with a **new RGBA color**.
- Save the Processed Image – Stores the modified image in the `color_changed_image` folder.

### ✂️ **Batch Image Processing**
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


### 🎨 **Interactive Drawing Tool with OpenCV**
This script provides a simple graphical interface that allows users to draw shapes (rectangle, line, circle) on an image using mouse events and keyboard input. The image can be saved with a single keystroke and opened in full screen for high-resolution editing.

```bash
python open_cv_mouse_key_events_github.py
```
This script will:
- Draw shapes interactively using your mouse
- Choose between rectangle, line, or circle
- Open image in full screen mode for better drawing experience
- Save the edited image to a folder with a single key press
- Mouse Controls
  - Click & Drag the left mouse button to draw the selected shape
- Keyboard Controls
   - Key	Action
     - 1	Draw Rectangle
     - 2	Draw Line
     - 3	Draw Circle
     - s	Save Image
     - ESC	Exit Program
- Full Screen Support
   - The window launches in fullscreen mode, allowing better handling of high-resolution images without resizing or distortion.
 
### 📏 **Edge Detection With OpenCV**
This tool is useful for interactively viewing edge detection results in a clean fullscreen interface. This script use [low_resolution_sample.jpg](https://unsplash.com/photos/gray-concrete-road-between-green-trees-during-daytime-D9SJWE89GyU)

```bash
python open_cv_edge_detection_github.py
```
This script will:
- Load an image from a given file path.
- Resize and pad the image to fit fullscreen without distortion.
- Apply Canny edge detection to highlight edges in the image.
- Display the original and edge-detected images side by side.
- Allow the user to save the edge-detected image by pressing the 's' key.
- Exit the program with the 'ESC' key.


#### 📸 **Low Light Image Enhancement With CLAHE**
This tool is designed to enhance images with low light conditions using the CLAHE (Contrast Limited Adaptive Histogram Equalization) method. This script can be used for both grayscale and colorful images, improving visibility in poorly lit areas.

[Test Images](https://www.kaggle.com/datasets/yasserh/sample-lowlight-images)

```bash
python open_cv_CLAHE_hist_equalization_github.py
```

This script will:

- Load an image from a given file path.
- Check if the image is grayscale or colorful.
- Apply CLAHE enhancement to the image based on its type (grayscale or colorful).
- Optionally upscale the image by a given scale factor.
- Display the enhanced image in fullscreen.
- Allow the user to save the enhanced image by pressing the 's' key.
- Exit the program with the 'ESC' key.

#### 🎨 **Color Palette Analyzer**
Extracts dominant colors from an image and visualizes them as a sleek palette. Uses KMeans clustering to detect and display the most representative colors of the image.

```bash
python open_cv_color_palette_github.py
```

This script will:
- Load an image from a given path
- Reshape the image pixels and apply KMeans clustering to detect dominant colors
- Display a horizontal palette bar that visualizes the dominant colors
- Return the dominant colors in hexadecimal format for design or web use
- Allow easy customization (image path & number of colors)

#### 🟡 Corner Detection Tool
Detects and visualizes prominent corners in an image using OpenCV’s goodFeaturesToTrack() algorithm. Ideal for feature point extraction in computer vision applications like tracking, object recognition, or image registration.

```bash
python open_cv_corner_detection.py
```
This script will:

- Load an image from a given file path
- Convert the image to grayscale and detect up to 300 strong corners
- Display the image with detected corners marked in green
- Resize and pad the display to fit nicely in a 1280x720 window
- Let you save the original image with red-marked corners by pressing s
- Exit the window with the ESC key

#### 🧼 Noise Reduction with Median Filtering
This tool is designed to reduce noise from images using the Median Filter technique, which is particularly effective in removing salt-and-pepper noise. The script uses the Pillow (PIL) library and supports easy saving and previewing of the filtered output.

```bash
python pillow_noise_reduction_github.py
```

This script will:
- Load an image from a given file path.
- Apply Median Filter with customizable kernel size.
- Save the enhanced image in high-quality (300 DPI).
- Preview the denoised image using your default image viewer.
- Automatically creates a folder for saving results.




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
- Image transformation (perspective correction, skewing)

## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests with new features or improvements. Any contributions are welcome!

## License
This project is licensed under the MIT License - see the LICENSE file for details.
