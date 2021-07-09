import cv2

import sys


a=cv2.imread("C:/Users/emrea/Desktop/Film Shots/Three Colors-Blue/Screenshot 2021-05-22 124018.png")
a = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
#ret, a = cv2.threshold(a, 155,255, cv2.THRESH_BINARY)

cv2.imshow("a",a)

if cv2.waitKey(0) & 0xFF == ord('q'):
    sys.exit()


cv2.destroyAllWindows()

