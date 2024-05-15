#This one works
import cv2
import cv2.aruco as aruco

# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Define the dictionary of ArUco markers we're using
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)

# Define the parameters for the ArUco marker detection
parameters = cv2.aruco.DetectorParameters()

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
    
    # Display the resulting frame
    cv2.imshow('Frame with ArUco markers', frame)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()