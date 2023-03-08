# Learn-Opencv-With-programmewithkarsan

# SUMMARY
This is a tutorial-like place that aim to  be simple but understandable. For me, most of the OpenCV source was complicated at first, so i want to make a simple source explain OpenCV and teach basic but important stuff.  Thank you to  check this out ☺


## WHAT IS AN IMAGE IN IMAGE PROCESSING
Image are not visual element for computer, but matrix of pixels. So computer handle a image as mathematical element.

![what_is_a_image](https://user-images.githubusercontent.com/106507209/223547355-bd3e9998-b02d-4e68-ba96-dc3fb92dbb17.gif)  <a href="https://www.flaticon.com/free-icons/arrow" title="arrow icons">Arrow icons created by Stockio - Flaticon</a>


## WHAT IS COLOR FORMAT OF OPENCV

![RGBvsBGR](https://user-images.githubusercontent.com/106507209/223425985-6bcc4797-80f0-4da6-943d-d797d3ab8107.gif)


## LINES AND SHAPES
##### CREATE AN EMPTY SCREEN

``` python
 screen_base = np.zeros((screen_width,screen_height,3), dtype = "uint8") # 3,channel count(B G R) 
 
```
This line of code create an empty screen. Images are multi-dimensional array.  So can create a screen with numpy array without use a image.


## BLURRING FILTER

#### 🔥🔥WARNING🔥🔥
##### General template. Usually we will write our codes in the appropriate part of this template.
``` python

import cv2 as cv

if __name __ == "__main__":
    
    #Read images
    img = cv.imread("saltandpeppernoise.jpg")


    #The part where the image is processed
    
    
    #Show processed image
    cv.imshow(img)
   
   
    #Waiting a key press to close all the windows and release used sources
    cv.waitKey(0)
    cv.destroyAllWindows()
 ```
🔥🔥🔥🔥🔥🔥🔥🔥🔥



 
To be continued, stay tuned :)

----

Thank you to be part of this learning journey with me 😺
