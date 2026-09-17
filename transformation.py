import cv2 as cv
import numpy as np

img = cv.imread('image.jpeg')

cv.imshow('Image', img)

# translation
def translate(image, x, y):
    # -x ---> left
    # -y ---> up
    #  x ---> right
    #  x ---> down

    transMat = np.float32([[1, 0, x], [0, 1, 7]])
    dimensions = (img.shape[1], img.shape[0])
    
    return cv.warpAffine(img, transMat, dimensions)

# rotation
def rotate(img, deg, rotPt = None):
    (height, width) = img.shape[: 2]
    
    if rotPt is None:
        rotPoint = (width // 2, height // 2)

    rotMat = cv.getRotationMatrix2D(rotPoint, deg, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('rotated', rotated)

translated = translate(img, 100, 100)
cv.imshow('translated', translated)

# flip
flip = cv.flip(img, 1)
cv.imshow('flipped', flip)

cv.waitKey(0)
