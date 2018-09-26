import cv2

import numpy as np
img = cv2.imread("auv.png")
while True:

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

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

    for c in cnts:

        M = cv2.moments(c)

        if M['m00']!=0:

            cX = int(M['m10']/M['m00'])

            cY = int(M["m01"]/M["m00"])

            

        else:

            cX, cY = 0, 0

        cv2.drawContours(hsv, [c], -1, (0,0,255), 2)

        cv2.circle(hsv, (cX, cY), 4, (0,0,0), -1)

        


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

    cv2.imshow("Image processed !!!!", hsv)

    cv2.imwrite("output.png", hsv)

cv2.destroyAllWindows()
