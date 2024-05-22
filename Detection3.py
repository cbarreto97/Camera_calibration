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

# Camera calibration parameters
camera_matrix = np.array([[1.39738870e+03, 0, 7.09700723e+02], [0, 1.08480951e+03, 5.04363018e+02], [0, 0, 1]])  # Replace fx, fy, cx, cy with your values
dist_coeffs = np.zeros((4,1))  # Replace with your values if you have them

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
        
        # Calculate the midpoints of each side of the ArUco marker
        midpoints = [(corners[0][0][i] + corners[0][0][(i+1)%4]) / 2 for i in range(4)]
        
        # Draw displacement vectors from the center of the frame to the midpoint of each side
        for midpoint in midpoints:
            cv2.arrowedLine(frame, tuple(frame_center.astype(int)), tuple(midpoint.astype(int)), (0, 255, 0), 2)
        
        # Estimate the pose of the ArUco marker
        rvecs, tvecs, _ = cv2.aruco.estimatePoseSingleMarkers(corners, 127, camera_matrix, dist_coeffs)  # Replace marker_size with your value
        
        # Draw the axes on the ArUco marker
        for i in range(len(ids)):
            cv2.aruco.drawAxis(frame, camera_matrix, dist_coeffs, rvecs[i], tvecs[i], 0.1)  # The last parameter is the length of the axes
        
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
