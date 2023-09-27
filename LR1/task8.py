import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    cross_image = np.zeros((height, width, 3), dtype=np.uint8)

    rect_start_v = (width // 2 - 30, height // 2 - 150)
    rect_end_v = (width // 2 + 30, height // 2 + 150)
    rect_start_h = (width // 2 - 150, height // 2 - 30)
    rect_end_h = (width // 2 + 150, height // 2 + 30)

    central_pixel_color = frame[height // 2, width // 2]

    color_distances = [
        np.linalg.norm(central_pixel_color - np.array([0, 0, 255])),
        np.linalg.norm(central_pixel_color - np.array([0, 255, 0])),
        np.linalg.norm(central_pixel_color - np.array([255, 0, 0]))
    ]

    closest_color_index = np.argmin(color_distances)

    result_color = (0, 0, 0)
    if closest_color_index == 0:
        result_color = (0, 0, 255)
    elif closest_color_index == 1:
        result_color = (0, 255, 0)
    else:
        result_color = (255, 0, 0)

    cv2.rectangle(cross_image, rect_start_h, rect_end_h, result_color, -1)
    cv2.rectangle(cross_image, rect_start_h, rect_end_h, result_color, -1)
    cv2.rectangle(cross_image, rect_start_v, rect_end_v, result_color, -1)

    result_frame = cv2.addWeighted(frame, 1, cross_image, 0.5, 0)

    cv2.imshow("colored_cross", result_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
