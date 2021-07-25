import cv2 as cv

img = cv.imread('assets/images/husky.jpg')

cv.imshow('Husky', img)

cv.waitKey(0)