import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


#Fotoğraf: Ali mnttzri: https://www.pexels.com/tr-tr/fotograf/adam-kisi-siluet-pencere-7904047/

if __name__ == '__main__':

    img = cv.imread("saltandpeppernoise.jpg")
    img = cv.resize(img,(0,0),fx=0.1,fy=0.1) # 90 percent smaller image -> size of img is 10 persent of original image

    median_blur = []
    average_mean_blur =[]
    gaussian_blur = []
    bilateral_blur = []
    kernel_size = [1,3,5,7,9,11,13,15]
    
    
    for i in kernel_size:
        
        median_blur.append(cv.medianBlur(img,i))
        average_mean_blur.append(cv.blur(img,(i,i)))
        gaussian_blur.append(cv.GaussianBlur(img,(i,i),0))
        bilateral_blur.append(cv.bilateralFilter(img,i,50,20))
        
       
    #CREATE A FIGURE AND SUBPLOTS TO DISPLAY ALL BLURRED IMAGES IN ONE FRAME

    fig, axs = plt.subplots(4,8, sharex = True, sharey = True)
    fig.suptitle("Blurring Method Comparison", fontsize = 16, color = "#126116")
    

    # SET THE Y-AXIS LABEL
    
    axs[0,0].set_ylabel("Median Blurring Method", color = "#2d8532", fontsize = 8)
    axs[1,0].set_ylabel("Average Mean Blurring Method", color = "#2d8532", fontsize = 8)
    axs[2,0].set_ylabel("Gaussian Blurring Method", color = "#2d8532", fontsize = 8)
    axs[3,0].set_ylabel("Bilateral Blurring", color = "#2d8532", fontsize = 8)
   

    #CONFIGURE SUBLOTS SPACING
    
    plt.subplots_adjust(left=0.05,
                    bottom=0.05,
                    right=0.95,
                    top=0.95,
                    wspace=0.04,
                    hspace=0.04)


    #ADD IMAGES TO SUBPLOTS
    
    for i in range(0,len(kernel_size)):
        axs[0,i].imshow(cv.cvtColor(median_blur[i],cv.COLOR_BGR2RGB))
        axs[1,i].imshow(cv.cvtColor(average_mean_blur[i],cv.COLOR_BGR2RGB))
        axs[2,i].imshow(cv.cvtColor(gaussian_blur[i],cv.COLOR_BGR2RGB))
        axs[3,i].imshow(cv.cvtColor(bilateral_blur[i],cv.COLOR_BGR2RGB))

        # If kernelsize[i] bigger then one it means blur filter applied to image but if it2s 1 it means original image. kernel_size describe searching space or neighboors and
        # 1 size scearching space represent original version
        # [original pixel] 1*1 size searching space
        # [n1 n2 n3
        #  n4 original n5
        #  n6 n7 n8] 3*3 searching space
        
        axs[3,i].set_xlabel("Kernel size = {size}'s result".format(size = kernel_size[i]), color = "#2d8532") if kernel_size[i] > 1 else  axs[3,i].set_xlabel("Original",fontsize=12)
       
        
       
    plt.show()
  
    cv.waitKey(0)
    cv.destroyAllWindows()
