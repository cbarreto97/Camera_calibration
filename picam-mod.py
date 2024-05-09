#opencv detect
import cv2
import cv2.aruco as aruco

# Load the image
image = cv2.imread('ArUco_tag.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the dictionary of ArUco markers we're using
