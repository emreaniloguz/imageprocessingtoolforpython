import cv2

import sys


a=cv2.imread("C:/Users/emrea/Desktop/Untitled.jpg",0)
ret, a = cv2.threshold(a, 155,255, cv2.THRESH_BINARY)

cv2.imshow("a",a)

if cv2.waitKey(0) & 0xFF == ord('q'):
    sys.exit()


cv2.destroyAllWindows()

