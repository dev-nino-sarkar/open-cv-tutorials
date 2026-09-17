import cv2 as cv

img = cv.imread('image.jpeg')
cv.imshow('Image', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dialating the image
dilated = cv.dilate(canny, (3, 3), iterations = 1)
cv.imshow('Dilated', dilated)

# eroding
eroded = cv.erode(dilated, (3, 3), iterations = 1)
cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500, 500))
cv.imshow('Resized', resized)

# crop
cropped = img[50 : 200, 200 : 400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
