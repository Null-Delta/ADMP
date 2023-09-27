import cv2
from custom_blur import *

img = cv2.imread(r'./LR3/RUSSKI_KOT.webp',cv2.IMREAD_GRAYSCALE)

dest = cv2.GaussianBlur(img, (9, 9), 4, 4, cv2.BORDER_WRAP)
customDest = gaussBlur(img, normalizeMatrix(createGaussMatrix(9, 9, 4, 4, 4)))

cv2.namedWindow('funny0', cv2.WINDOW_NORMAL)
cv2.resizeWindow('funny0', 200, 200)
cv2.imshow('funny0',dest)

cv2.namedWindow('funny1', cv2.WINDOW_NORMAL)
cv2.resizeWindow('funny1', 200, 200)
cv2.imshow('funny1',customDest)

cv2.waitKey(0)
cv2.destroyAllWindows()    
