import cv2 as cv
import numpy as np

# creates a blank canvas of height 500 width 500 and 3 channels aka 3 x 3 matrix
# type is unsigned 8 bit integer
blank = np.zeros((500, 500, 3), dtype = 'uint8')
cv.imshow('Blank', blank)

img = cv.imread('image.jpeg')
cv.imshow('Image', img)

# 1.paint the entire canvas black
blank[:] = 0, 255, 0
cv.imshow('Green', blank)

# 2. draw a rectangle
cv.rectangle(blank, (0, 0), (250, 500), (0, 0, 255), thickness=2)
cv.imshow('Rectangle', blank)

# 3. draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0, 0, 255), thickness=1)
cv.imshow('Circle', blank)

# 4. draw a line
cv. line(blank, (0, 0), (blank.shape[1] // 2, blank.shape[0] // 2), (0, 255, 0), thickness = 1)
cv.imshow('Line', blank)

# 5. write a text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)
cv.imshow('Text', blank)

cv.waitKey(0)
