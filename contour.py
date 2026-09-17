import cv2 as cv
import numpy as np

img = cv.imread('image.jpeg')

cv.imshow('image', img)

blank = np.zeros(img.shape, dtype = 'uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('canny edges', canny)

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)

contours, hierachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
print(f'{len(contours)} contours found')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow('contours', blank)

cv.waitKey(0)
