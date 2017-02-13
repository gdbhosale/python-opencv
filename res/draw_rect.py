import numpy as np
import cv2

img = cv2.imread("messi5.jpg")

# Draw a green rectangle from (top left) to (bottom-right) corner
cv2.rectangle(img, (10,10), (100,100), (0,255,0), 3)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()