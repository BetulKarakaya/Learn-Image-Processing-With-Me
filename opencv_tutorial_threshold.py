import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

if __name__ == "__main__":


    img = cv.imread("saltandpeppernoise.jpg",0) # zero parameter load image as grayscale
    img = cv.resize(img,(0,0),fx =0.1,fy=0.1)
    blur = cv.medianBlur(img,7)

    color = ["#E5D94F", "#22E6DB", "#E69D0B","#5825E6","#E64F00"]
    
    simple_methods = [ ("Simple Binary Threshold",cv.THRESH_BINARY), ("Simple Binary Invert Threshold",cv.THRESH_BINARY_INV ), ("Truncated Threshld",cv.THRESH_TRUNC) ,
                       ("ToZero Threshold",cv.THRESH_TOZERO),("ToZero Invert Threshold",cv.THRESH_TOZERO_INV)]
    adaptive_methods = [("Adaptive Mean Method Threshold", cv.ADAPTIVE_THRESH_MEAN_C), ("Adaptive Gaussian Method Threshold", cv.ADAPTIVE_THRESH_GAUSSIAN_C)]


   
    fig = plt.figure()
    plt.subplots_adjust(hspace=1.5, wspace =2)

    
    for i in range(0,len(simple_methods)):
        
        ax = plt.subplot2grid((6,12),(0, 2*i), colspan=2,rowspan =2)
        ret,thresh = cv.threshold(img,85,255,simple_methods[i][1])
        ax.imshow(cv.cvtColor(thresh,cv.COLOR_GRAY2RGB))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel(simple_methods[i][0], color = color[i])
        

        ax = plt.subplot2grid((6,12),(2,(2*i)+2), colspan=2,rowspan =2)
        ret,thresh2 = cv.threshold(blur,155,255,simple_methods[i][1]+cv.THRESH_OTSU)
        ax.imshow(cv.cvtColor(thresh2,cv.COLOR_GRAY2RGB))
        ax.set_xticks([])
        ax.set_yticks([])
        ax.set_xlabel("Filter Applied On Original Image\n{blur}+\n{method}+\n{flag}".format(blur = "Gaussian Blur" , method = simple_methods[i][0], flag = "Otsu Threshold as Flag"), color = color[i-1], multialignment='center', size= 9)

        if i == 0:
            ax = plt.subplot2grid((6,12),(2,0), colspan=2,rowspan =2)
            ax.hist(blur.ravel(),256,[0,256])
            ax.set_xlabel("Histogram Of \nGaussian Blur Applied Image", multialignment = 'center')


    for i in range(0,2):
        for j in range(0,2):

            ax = plt.subplot2grid((6,12),(4,(4*i)+(2*j)), colspan=2,rowspan =2)
            thresh =  cv.adaptiveThreshold(blur,255,adaptive_methods[i][1],simple_methods[j][1],215,2)
            ax.imshow(cv.cvtColor(thresh,cv.COLOR_GRAY2BGR))
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_xlabel("Filter Applied On Original Image\n{blur}\n{adaptive_method}+\n{method}".format(blur = "Median Blur", adaptive_method = adaptive_methods[i][0],method = simple_methods[j][0]), color = color[2*i+j], multialignment='center', size= 8)
    
    plt.show()


    cv.waitKey(0)
    cv.destroyAllWindows()


