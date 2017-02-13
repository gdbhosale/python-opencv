import numpy as np
import cv2

img = cv2.imread("messi5.jpg")

font = cv2.FONT_HERSHEY_SIMPLEX

# Text with position from bottom-left corner,
# Font type, Font Size, color, thickness, lineType
cv2.putText(img, 'OpenCV', (10,60), font, 2, (255,255,255), 2, cv2.CV_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()