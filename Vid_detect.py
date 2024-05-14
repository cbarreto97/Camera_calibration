#Not working
import cv2 
import time

cam = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))
duration = 5

end_time = time.time() + duration

while time.time() < end_time:
    ret, frame = cam.read()
    out.write(frame)

    cv2.imshow('Preview', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
out.release()
cv2.destroyAllWindows()

