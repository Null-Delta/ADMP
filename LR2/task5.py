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
    in_range2 = cv2.inRange(hsv, minRed2, maxRed2) 

    moments1 = cv2.moments(in_range1) 
    moments2 = cv2.moments(in_range2) 
    area = moments1['m00'] + moments2['m00']
    if area > 0: 
        size = int(np.sqrt(area)) 
        xInd = int((moments1["m10"] + moments2["m10"]) / area) 
        yInd = int((moments1["m01"] + moments2["m01"]) / area) 

        cv2.ellipse(
            frame,
            (xInd, yInd),
            (size // 10, size // 20),
            0,0,360,(255, 0, 0), 5
        )

    cv2.imshow('rect', frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

cap.release() 
cv2.destroyAllWindows() 