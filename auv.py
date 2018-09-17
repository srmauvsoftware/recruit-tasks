import cv2
import numpy as np
import matplotlib as plt
import numpy as np
image = cv2.imread("/home/rahil/catkin_ws/src/assignment/scripts/auv.png")
centerx = []



def colordetection():
    while True:
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        mask = cv2.inRange(hsv, (88,100,100), (130, 255, 255))
        inv = cv2.bitwise_not(mask)
        inv_2 = cv2.medianBlur(inv, 15)
        inv_2 = cv2.GaussianBlur(inv_2,(15,15), 0)
                            
        res = cv2.bitwise_and(hsv, hsv, mask = inv_2)
                            
        kernel = np.ones((5,5), np.uint8)
        erosion = cv2.erode(inv_2, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        im2, cnts, h = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        M = cv2.moments(cnts[0])
                
        if M['m00']!=0:
            cX = int(M['m10']/M['m00'])
            cY = int(M["m01"]/M["m00"])
            centerx.append(cX)
            
                               
            cv2.drawContours(hsv, cnts[0], -1, (0,255,0), 2)
            cv2.circle(hsv, (cX, cY), 4, (0,0,0), -1)
            cv2.putText(hsv, "center", (cX-20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            M = cv2.moments(cnts[1])
        if M['m00']!=0:
            cX = int(M['m10']/M['m00'])
            cY = int(M["m01"]/M["m00"])
            centerx.append(cX)
            

            
                                
            cv2.drawContours(hsv, cnts[1], -1, (0,255,0), 2)
            cv2.circle(hsv, (cX, cY), 4, (0,0,0), -1)
            cv2.putText(hsv, "center", (cX-20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
            M = cv2.moments(cnts[2])
        if M['m00']!=0:
            cX = int(M['m10']/M['m00'])
            cY = int(M["m01"]/M["m00"])
           
                    
                           
            centerx.append(cX)
            
            cv2.drawContours(hsv, cnts[2], -1, (0,255,0), 2)
            cv2.circle(hsv, (cX, cY), 4, (0,0,0), -1)
            cv2.putText(hsv, "center", (cX-20, cY-20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 2)
        res_2 = cv2.medianBlur(image, 15)
        res_2 = cv2.GaussianBlur(hsv,(15,15), 0)
                            
        res_2 = cv2.medianBlur(res, 15)
        res_2 = cv2.GaussianBlur(res_2,(15,15), 0)
        kernel = np.ones((5,5), np.uint8)
        smoothed = cv2.filter2D(res, -1, kernel)
        erosion = cv2.erode(smoothed, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        kernel = np.ones((3,3), np.uint8)
        smoothed = cv2.filter2D(closing, -1, kernel)
        erosion = cv2.erode(smoothed, kernel, iterations=1)
        dilation = cv2.dilate(erosion, kernel, iterations=1)
        opening = cv2.morphologyEx(dilation, cv2.MORPH_OPEN, kernel)
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
        hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
     

                            
                                   
        k = cv2.waitKey(20) & 0xff
        cv2.imshow("image", hsv)
        cv2.imwrite("output.png", hsv)
        return centerx
        
def coordinatex():
    center1 = []
    center1 = colordetection()
    return center1

       
                        
                            
   
   






