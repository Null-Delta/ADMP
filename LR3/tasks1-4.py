import cv2 
from custom_blur import *

matrix9x9x5 = normalizeMatrix(createGaussMatrix(9, 9, 3, 3, 5))
matrix9x9x1 = normalizeMatrix(createGaussMatrix(9, 9, 3, 3, 1))
matrix5x5x5 = normalizeMatrix(createGaussMatrix(5, 5, 2, 2, 5))
matrix5x5x1 = normalizeMatrix(createGaussMatrix(5, 5, 2, 2, 1))

img = cv2.imread(r'./LR3/RUSSKI_KOT.webp',cv2.IMREAD_GRAYSCALE)

images = [
    ("5x5x1", gaussBlur(img, matrix5x5x1)),
    ("5x5x5", gaussBlur(img, matrix5x5x5)),
    ("9x9x1", gaussBlur(img, matrix9x9x1)),
    ("9x9x5", gaussBlur(img, matrix9x9x5))
]

for image in range(len(images)):
    cv2.namedWindow('funny' + str(images[image][0]), cv2.WINDOW_NORMAL)
    cv2.resizeWindow('funny' + str(images[image][0]), 200, 200)
    cv2.imshow('funny' + str(images[image][0]),images[image][1])

cv2.namedWindow('funny0', cv2.WINDOW_NORMAL)
cv2.resizeWindow('funny0', 200, 200)
cv2.imshow('funny0',img)

cv2.waitKey(0)
cv2.destroyAllWindows()    
    