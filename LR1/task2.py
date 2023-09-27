import cv2

img1 = cv2.imread(r'./source/funny.jpg',cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread(r'./source/funny.png',cv2.IMREAD_REDUCED_COLOR_8)
img3 = cv2.imread(r'./source/funny.bmp',cv2.IMREAD_ANYDEPTH)
cv2.namedWindow('funny1', cv2.WINDOW_NORMAL)
cv2.namedWindow('funny2', cv2.WINDOW_NORMAL)
cv2.namedWindow('funny3', cv2.WINDOW_NORMAL)
cv2.imshow('funny1',img1)
cv2.imshow('funny2', img2)
cv2.imshow('funny3', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

