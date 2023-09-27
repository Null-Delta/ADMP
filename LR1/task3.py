import cv2

cap = cv2.VideoCapture(r'./source/Helicopter.mp4', cv2.CAP_ANY)

while True:
    ret, frame = cap.read()

    if not ret:
        exit()

    frame = cv2.resize(frame, (1280, 720))
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video', gray_frame)

    if cv2.waitKey(1) & 0xFF == 27:
        exit()
