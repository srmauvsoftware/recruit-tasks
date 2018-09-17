import cv2
import numpy as np

img = cv2.imread('image.png', 1)
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
mask = cv2.inRange(hsv,(88,100,100),(130,255,255))
inv = cv2.bitwise_not(mask)
inv = cv2.GaussianBlur(inv,(15,15),0)
res = cv2.bitwise_and(hsv,hsv,mask = inv)
kernel = np.ones((5,5),np.uint8)
res = cv2.erode(res,kernel,iterations=1)

_, contours , _ = cv2.findContours(res,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x = cv2.moments(contour)
    if x['m00']!=0:
        cX = int(x['m10']/x['m00'])
        cY = int(x['m01']/x['m00'])
    else:
        cX,cY = 0,0
    cv2.drawContours(hsv,[contour],-1,(0,255,0),2)
    cv2.circle(hsv,(cX,cY),4,(0,0,0),-1)
    cv2.line(hsv, (cX, cY), (511, 230), (0,255,0), 2)
cv2.circle(hsv,(511,230),4,(0,0,0),-1)
res = cv2.cvtColor(hsv , cv2.COLOR_HSV2BGR)


cv2.imshow('Image',res)
cv2.imwrite('Result.png',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
