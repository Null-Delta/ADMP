import cv2 
import numpy as np 

minRed1 = np.array([0, 100, 250]) 
maxRed1 = np.array([15, 255, 255])  

minRed2 = np.array([165, 100, 250]) 
maxRed2 = np.array([180, 255, 255])  

cap = cv2.VideoCapture(1) 

while True: 
    ret, frame = cap.read() 
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 

    in_range1 = cv2.inRange(hsv, minRed1, maxRed1) 
    in_range2 = cv2.inRange(hsv, minRed1, maxRed1) 
    kernel = np.ones((20, 20), np.uint8) 

    image_opening1 = cv2.morphologyEx(in_range1, cv2.MORPH_OPEN, kernel) 
    image_closing1 = cv2.morphologyEx(in_range1, cv2.MORPH_CLOSE, kernel) 
    image_opening2 = cv2.morphologyEx(in_range2, cv2.MORPH_OPEN, kernel) 
    image_closing2 = cv2.morphologyEx(in_range2, cv2.MORPH_CLOSE, kernel) 

    opening = cv2.addWeighted(image_opening1, 1, image_opening2, 1, 1)
    closing = cv2.addWeighted(image_closing1, 1, image_closing2, 1, 1)

    cv2.imshow("Open", opening) 
    cv2.imshow("Close", closing) 

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

cap.release() 
cv2.destroyAllWindows() 

