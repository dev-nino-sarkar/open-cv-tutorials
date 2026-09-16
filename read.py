import cv2 as cv

#image processing
img = cv.imread('image.jpeg')

cv.imshow('image', img)

# reading videos
capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(40) & 0xFF == ord('d'):
            break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
