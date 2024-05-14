import cv2
import time

cam = cv2.VideoCapture(0)

num_images = 1 

for i in range(num_images):
    ret,frame = cam.read()
    cv2.imshow('Preview', frame)
    cv2.waitKey(3000)

    cv2.imwrite(f'ArUco_6x6.jpg', frame)
    time.sleep(1)

cam.release()
cv2.destroyAllWindows()