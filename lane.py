import cv2
import numpy as np
import math
cap=cv2.VideoCapture("raw_front.avi")

while True:
        ret,frame = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = np.array([10,80,0])
        upper = np.array([190,255,20])
        mask = cv2.inRange(hsv,lower,upper)
        vertices= np.array([[200,550],[200,550],[370,400],[400,400],[600,550],[600,550]])
        b = cv2.fillPoly(mask, [vertices],190)
        radius=(math.sqrt((600*600-200*200))*0.3)/70
        center = (600/2-200/2)
        cv2.putText(mask, "Mean Radius(in m):"+str(radius),(0,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
        
        imshape = mask.shape
       
        lower_left = [imshape[1]/9,imshape[0]]
        lower_right = [imshape[1]-imshape[1]/9,imshape[0]]
        top_left = [imshape[1]/2-imshape[1]/8,imshape[0]/2+imshape[0]/10]
        top_right = [imshape[1]/2+imshape[1]/8,imshape[0]/2+imshape[0]/10]
        
        diff_1=top_right[0]-top_left[0]
  
        
        edges=cv2.Canny(mask,50,150)
       
        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 180,20,15)
        for line in lines:
            coord = lines[0]
            diff=center-(coord[0][2]-coord[0][1])        
        if (diff-152)==0:
            cv2.putText(mask, "Center",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("mask",mask)
        if diff>152:
            cv2.putText(mask, "Right",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("mask",mask)
        if diff<152:
            cv2.putText(mask, "Left",(650,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (100,110,150), 2)
            cv2.imshow("mask",mask)
   
        
               
        k = cv2.waitKey(20)&0xff
        if k==27:
            break

cv2.destroyAllWindows()

