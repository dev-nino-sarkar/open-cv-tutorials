import cv2 as cv2

img = cv.imread('image.jpeg')
cv.imshow('Image', img)

def rescaleFrame(frame, scale = 0.75):
    # images, videos, live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # live videos
    capture.set(3, width)
    capture.set(4, height)

    

cv.waitKey(0)
