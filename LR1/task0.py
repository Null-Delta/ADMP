import cv2

def print_cam():
    cap = cv2.VideoCapture("http://admin:admin@192.168.43.218:8081/video")
    cap.set(3, 1280)
    cap.set(4, 720)
    while True:
        ret, frame = cap.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

print_cam()
