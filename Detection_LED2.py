import cv2
import cv2.aruco as aruco
import numpy as np
import RPi.GPIO as GPIO  # Import the RPi.GPIO library

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the dictionary of ArUco markers we're using
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)

# Define the parameters for the ArUco marker detection
parameters = cv2.aruco.DetectorParameters()

# Set up the GPIO pin for the LED
LED_PIN = 3
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    
    if not ret:
        break
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect the ArUco markers in the grayscale frame
    corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)
    
    # If any markers were found
    if ids is not None:
        # Draw the detected markers on the frame
        frame = aruco.drawDetectedMarkers(frame, corners, ids)
        
        # Calculate the center of the frame
        frame_center = np.array([frame.shape[1] / 2, frame.shape[0] / 2])
        
        # Calculate the center of the ArUco marker
        marker_center = np.mean(corners[0][0], axis=0)
        
        # Calculate the distance from the center of the frame to the center of the ArUco marker
        distance = np.linalg.norm(frame_center - marker_center)
        
        # Calculate the midpoints of each side of the ArUco marker
        midpoints = [(corners[0][0][i] + corners[0][0][(i+1)%4]) / 2 for i in range(4)]
        
        for midpoint in midpoints:
            cv2.arrowedLine(frame, tuple(frame_center.astype(int)), tuple(midpoint.astype(int)), (0, 255, 0), 2)
        
        # Calculate the displacement of each side of the ArUco marker
        #displacements = [np.linalg.norm(frame_center - midpoint) for midpoint in midpoints]
        
        # Print the displacement and direction of each side
       # for i, displacement in enumerate(displacements):
       #     print(f"Side {i+1} is displaced by {displacement} units towards the direction of its midpoint.")
        
        # Draw lines from the center of the frame to the midpoint of each side
        #for midpoint in midpoints:
         #   cv2.line(frame, tuple(frame_center.astype(int)), tuple(midpoint.astype(int)), (0, 255, 0), 2)
        
        # If the distance is below a certain threshold, turn on the LED
        if distance < 25:
            GPIO.output(LED_PIN, GPIO.HIGH)
        else:
            GPIO.output(LED_PIN, GPIO.LOW)
    
    # Display the resulting frame
    cv2.imshow('Frame with ArUco markers', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()

# Clean up the GPIO
GPIO.cleanup()
