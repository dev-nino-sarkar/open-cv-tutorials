import cv2 as cv

img = cv.imread('image.jpeg')
cv.imshow('Image', img)

def rescaleFrame(frame, scale = 0.75):
    # images, videos, live videos
    width = int(frame.shape[1] * scale) # 1 for width
    height = int(frame.shape[0] * scale) # 2 for height
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation = cv.INTER_AREA)

def changeRes(width, height):
    # live videos
    capture.set(3, width)
    capture.set(4, height)

    

cv.waitKey(0)
