import cv2 as cv

img = cv.imread('image.jpeg')
cv.imshow('image', img)


# averaging
average = cv.blur(img, (3, 3))
cv.imshow('average blur', average)

# gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('gaussian blur', gauss)

# median blur
median = cv.medianBlur(img, 3)
cv.imshow('median', median)

# bilateral
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('bilateral', bilateral)

cv.waitKey(0)
