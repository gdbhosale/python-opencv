import numpy as np
import cv2

img = cv2.imread("messi5.jpg")

# Draw a circle with center coordinates, radius and color
cv2.circle(img, (100,63), 63, (0,0,255), -1)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()