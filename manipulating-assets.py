import cv2 as cv

img = cv.imread('assets/images/cat.jpg')
cv.imshow('Cat', img)

def changeRes(width, height):
    # Live Video
    capture.set(3, width)
    capture.set(4, height)


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

cv.imshow('Image', rescaleFrame(img))

# Reading Videos
capture = cv.VideoCapture('assets/videos/dog.mp4');

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=0.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)