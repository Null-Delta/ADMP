import cv2

img1 = cv2.imread(r'./source/funny.png')
img2 = cv2.imread(r'./source/funny.png')

cv2.namedWindow('funny', cv2.WINDOW_NORMAL)
cv2.namedWindow('funny_hsv', cv2.WINDOW_NORMAL)

cv2.imshow('funny',img1)

hsv = cv2.cvtColor(img2, cv2.COLOR_BGR2HLS)
cv2.imshow('funny_hsv', hsv)

cv2.waitKey(0)
cv2.destroyAllWindows()