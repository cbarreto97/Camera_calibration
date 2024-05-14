#opencv detect
import cv2
import cv2.aruco as aruco

# Load the image
image = cv2.imread('ArUco_6x6.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the dictionary of ArUco markers we're using
aruco_dict = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_6X6_100)

# Define the parameters for the ArUco marker detection
parameters = cv2.aruco.DetectorParameters()

# Detect the ArUco markers in the image
corners, ids, rejected = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

# If any markers were found
if len(corners) > 0:
    # Draw the detected markers on the image
    image = aruco.drawDetectedMarkers(image, corners, ids)

# Display the image with the detected markers
cv2.imshow('Image with ArUco markers', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
