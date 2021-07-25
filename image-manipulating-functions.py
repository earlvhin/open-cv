import cv2 as cv

img = cv.imread('assets/images/cat.jpg')
# cv.imshow('Cat', img)

# Converting to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=5)
cv.imshow('Dilated', dilated)

# Eroding
eroded = cv.erode(dilated, (7,7), iterations=5)
cv.imshow('Eroded', eroded)

# Resizing
resize = cv.resize(img, (250, 250), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resize)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)