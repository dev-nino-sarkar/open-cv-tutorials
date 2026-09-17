import cv2 as cv

# reading an image
img = cv.imread('image.jpeg') # returns call-by-value

# displays image
cv.imshow('image', img)

# reading videos
capture = cv.VideoCapture(0) # 0 reads videos path to video reads video

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(40) & 0xFF == ord('d'):
            break

capture.release()
cv.destroyAllWindows() # works as free() in c

# waits indefinitely
cv.waitKey(0)
