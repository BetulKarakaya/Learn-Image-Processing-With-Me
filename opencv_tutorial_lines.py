import cv2 
import numpy as np


def DrawLine(image,start_position,end_position, color, thickness):

    cv2.line(image,start_position,end_position,color,thickness)


def DrawCircle(image,centre_of_circle, radius, color, thickness):

    cv2.circle(image,centre_of_circle, radius, color, thickness)


def DrawRectangle(image, top_left_corner, bottom_right_corner,color, thickness):
    
    cv2.rectangle(image,top_left_corner, bottom_right_corner, color, thickness)


def DrawEllipse(image,center_of_ellipse,axes_length,rotation_angle,start_angle,end_angle,color,thickness):

    cv2.ellipse(image,center_of_ellipse,axes_length,rotation_angle,start_angle,end_angle,color,thickness)


def DrawPolygon(image,nparray_point_polygon, color):

    if isinstance(nparray_point_polygon, np.ndarray):
        cv2.fillPoly(image, [nparray_point_polygon], color)
    else:
        print("Polygon can not be drawn. Please check np array")


def DrawText(image,text,left_bottom_corner,font,font_scale,color,thickness):

    cv2.PutText(image,text,left_bottom_corner,font,font_scale,color,thickness,cv2.LINE_AA) #cv2.LINE_AA use as default value, it is most common usage



if __name__ == "__main__":

    #CREATE A EMPTY SCREEN WITH NUMPY
    screen_width = 500
    screen_height = 500

    screen_base = np.zeros((screen_width,screen_height,3), dtype = "uint8") # 3,channel count(B G R)

    DrawRectangle(screen_base,(0,0),(screen_width,screen_height),(130,162,217),-1) #BGR(130,162,217) -> RGB(217,162,130) -> HEX= #d9a282

    DrawRectangle(screen_base,(75,150),(200,325),(96,166,111),-1)
    DrawEllipse(screen_base,(138,150),(62,75),0,180,360,(96,166,111),-1)

    points_for_first_stair = np.array([[150,225],[250,225],[250,275],[300,275],[300,300],[350,300],[350,325],[400,325],[400,425],[150,425]])
    DrawPolygon(screen_base,points_for_first_stair,(49,38,166))

    DrawRectangle(screen_base,(225,375),(300,425),(130,162,217),-1)
    DrawEllipse(screen_base,(262,375),(37,50),0,180,360,(130,162,217),-1)


    points_for_second_stair = np.array([[300,350],[350,350],[350,450],[250,450],[250,400],[275,400],[275,375],[300,375]])
    DrawPolygon(screen_base,points_for_second_stair,(66,128,140))

    DrawCircle(screen_base,(400,150),50,(244,227,255),-1)
    DrawCircle(screen_base,(440,150),50,(130,162,217),-1)

    for i in range(0,4):
            
        DrawLine(screen_base,(0,0+(i*12)),(screen_width,60+(i*12)),(150,52,20),1)
        DrawLine(screen_base,(41+(30*i),60),(57+(30*i),333),(0,0,0),1)

    for i in range(0,5):

        DrawCircle(screen_base,(60+(i*100),30),5,(194,164,76),-1)
        DrawCircle(screen_base,(90+(i*100),45),5,(194,164,76),-1)
        DrawCircle(screen_base,(30+(i*100),35),11,(194,164,76),-1)
        DrawLine(screen_base,(450+(i*5),250+(i*15)),(300+(i*5),325+(i*15)),(0,0,0),1)


    DrawCircle(screen_base,(340,113),17,(0,0,5),-1)
        

    
    cv2.imshow("Github OpenCV by programmewithkarsan",screen_base)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
