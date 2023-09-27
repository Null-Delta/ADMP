import cv2 
import numpy as np 

minRed1 = np.array([90, 100, 100]) 
maxRed1 = np.array([135, 255, 255])  

minRed2 = np.array([0, 100, 250])
maxRed2 = np.array([0, 255, 255])

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    red_only1 = cv2.bitwise_and(frame, frame, mask=cv2.inRange(hsv, minRed1, maxRed1)) 
    red_only2 = cv2.bitwise_and(frame, frame, mask=cv2.inRange(hsv, minRed2, maxRed2)) 

    result = cv2.addWeighted(red_only1, 1, red_only2, 1, 1)
    cv2.imshow('window', frame) 
    cv2.imshow('window2', result) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

cap.release() 
cv2.destroyAllWindows()

