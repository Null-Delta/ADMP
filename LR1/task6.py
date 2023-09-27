import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    # cross

    cross_image = np.zeros((height, width, 3), dtype=np.uint8)

    cv2.rectangle(
        cross_image,  
        (width // 2 - 30, height // 2 - 150),
        (width // 2 + 30, height // 2 - 30),
        (0, 0, 255),
        2
    )

    cv2.rectangle(
        cross_image,  
        (width // 2 - 30, height // 2 + 150),
        (width // 2 + 30, height // 2 + 30),
        (0, 0, 255),
        2
    )

    cv2.rectangle(
        cross_image,
        (width // 2 - 150, height // 2 - 30),
        (width // 2 + 150, height // 2 + 30),
        (0, 0, 255),
        2
    )
    
    # blur

    blured_image = cv2.GaussianBlur(
        frame,
        (201, 201),0,0,
        cv2.BORDER_DEFAULT
    )

    frame[
        height // 2 - 30:height // 2 + 30, 
        width // 2 - 150:width // 2 + 150
    ] = blured_image[
        height // 2 - 30:height // 2 + 30,
        width // 2 - 150:width // 2 + 150
    ]

    result_frame = cv2.addWeighted(frame, 1, cross_image, 0.5, 0)

    cv2.imshow("Blur cross", result_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
