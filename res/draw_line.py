import numpy as np
import cv2

img = cv2.imread("messi5.jpg")

# Draw a diagonal blue (BGR) line with thickness of 5 px
cv2.line(img, (0,0), (100,100), (255,0,0), 5)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()