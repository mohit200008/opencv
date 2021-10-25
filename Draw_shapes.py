import numpy as np
import cv2



img = cv2.imread('lena.jpg',1)
# img = np.zeros([512,512,5], np.uint8)

img = cv2.line(img, (0,0), (255,255), (255,0,255),  15)
img = cv2.arrowedLine(img, (0,0), (0,255), (255,0,255),  15)

img = cv2.rectangle(img, (214,84), (0,455), (0,0,255),-1)
img = cv2.circle(img, (255,255), 65, (0,255,255), -1)
font = cv2.FONT_HERSHEY_SCRIPT_COMPLEX
img = cv2.putText(img, 'Opencv', (10,500), font, 5, (255,255,255), 15, cv2.LINE_AA)

cv2.imshow('Image of lena', img)

cv2.waitKey(0)
cv2.destroyAllWindows()