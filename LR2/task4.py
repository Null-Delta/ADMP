import cv2 
import numpy as np 

minRed1 = np.array([0, 100, 250]) 
maxRed1 = np.array([15, 255, 255])  

minRed2 = np.array([165, 100, 250]) 
maxRed2 = np.array([180, 255, 255])  

cap = cv2.VideoCapture(0) 

while True: 
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    in_range1 = cv2.inRange(hsv, minRed1, maxRed1) 
    in_range2 = cv2.inRange(hsv, minRed1, maxRed1) 

    red_only1 = cv2.bitwise_and(frame, frame, mask=in_range1) 
    red_only2 = cv2.bitwise_and(frame, frame, mask=in_range2)

    result = cv2.addWeighted(red_only1, 1, red_only2, 1, 1)

    cv2.imshow('window', result) 

    moments1 = cv2.moments(in_range1) 
    moments2 = cv2.moments(in_range2) 
    area = moments1['m00'] + moments2['m00']
    print(area) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

cap.release() 
cv2.destroyAllWindows() 