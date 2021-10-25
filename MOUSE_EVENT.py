import numpy as np
import cv2

# events = [i for i in dir(cv2) if 'EVENT' in i ]
# print(events)

def click_event(event, x,y,flags,param):
    # if event == cv2.EVENT_LBUTTONDBLCLK:
    #     print(x,' , ', y)
    #     font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    #     strXY = str(x) + '  ,  ' + str(y)
    #     cv2.putText(img,strXY , (x,y), font,1,(255,255,255),4)
    #     cv2.imshow('Image' , img)
    # if event == cv2.EVENT_RBUTTONDOWN:
    #     blue = img[y, x, 0]    
    #     green = img[y, x, 1]    
    #     red = img[y, x, 2]    
    #     font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
    #     strBGR = str(blue) + '  ,  ' + str(green) + ' , ' + str(red)
    #     cv2.putText(img,strBGR , (x,y), font,1,(255,255,255),4)
    #     cv2.imshow('Image' , img)
    if event == cv2.EVENT_LBUTTONDOWN:
       blue = img[x,y,0]  
       green = img[x,y,1]  
       red = img[x,y,2]
       cv2.circle(img, (x,y), 3, (0,0,255), -1)
       mycolorImage = np.zeros((512,512,3), np.uint8)

       mycolorImage[:] = [blue,green,red]

       cv2.imshow('color', mycolorImage)  

# img = np.zeros((512,512,3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('Image',img)
points = []
cv2.setMouseCallback('Image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
