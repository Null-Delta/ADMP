import requests
import cv2
import numpy as np
import imutils

#url = "rtsp://192.168.43.218:8554/live"

url = "rstp://192.168.204.1:8080/h264_ulaw"

while True:
    img_resp = requests.get(url)

    img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)

    img = cv2.imdecode(img_arr, -1)

    img = imutils.resize(img, width=1000, height=1800)
    cv2.imshow("camera", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()