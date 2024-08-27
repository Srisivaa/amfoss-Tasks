import cv2
import numpy as np
import os

# Directory containing the images
image_dir = 'D:/Dundu/assets'
output_file = 'D:/Dundu/new/dot_coordinates_and_colors.txt'
positions = {}
# Define colour ranges in HSV 
# Example for Red, Green, Blue, White and Black 
color_ranges = { 
#        'red': [(0, 100, 100), (10, 255, 255), (160, 100, 100), (180, 255, 255)], 
#        'green': [(40, 100, 100), (80, 255, 255)], 
#        'blue': [(100, 100, 100), (140, 255, 255)],
        'black': [(0, 0, 0), (180, 255, 30)],
        'yellow': [(22,93,0),(45,255,255)]
}

# Function to find and record the dot in an image
def detect_dot(image_path):
    # Read the image
    image = cv2.imread(image_path)
   
    # Find the colour of the dot
    # Convert the image to HSV color space 
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
    colour='No Dot'
    # Create masks to find contours 
    for color, ranges in color_ranges.items(): 
        # If there are two ranges (like red), combine them 
        mask = None 
        if len(ranges) == 4:  # Red has two ranges 
            lower1 = np.array(ranges[0]) 
            upper1 = np.array(ranges[1]) 
            lower2 = np.array(ranges[2]) 
            upper2 = np.array(ranges[3]) 
             
            mask1 = cv2.inRange(hsv_image, lower1, upper1) 
            mask2 = cv2.inRange(hsv_image, lower2, upper2) 
            mask = cv2.bitwise_or(mask1, mask2) 
        else: 
            lower = np.array(ranges[0]) 
            upper = np.array(ranges[1]) 
            mask = cv2.inRange(hsv_image, lower, upper) 
     
       #Find contours 
        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
     
        # Extract positions 
        positions[color] = [] 
        for contour in contours: 
            colour=''
            M = cv2.moments(contour) 
            if M["m00"] != 0:  # To avoid division by zero 
                cX = int(M["m10"] / M["m00"]) 
                cY = int(M["m01"] / M["m00"]) 
                positions[color].append((cX, cY))
                colour=color
    return positions, colour
    
# Collecting data for all images
filename = ''
filenames = os.listdir(image_dir)
with open(output_file, 'w') as f:
    for filename in filenames:
        if filename.endswith(".png") or filename.endswith(".jpg"):
            image_path = image_dir+'/'+filename
            coordinates = detect_dot(image_path)
            if coordinates:
                if coordinates[1] == 'No Dot':
                     xystring=(0,0)
                else:
                    xystring=str(coordinates[0][coordinates[1]]).strip('[,]')
            print('File Name:',filename, ', Dots\' Colour:',coordinates[1],', Dots\' Position:',xystring, file=f)
print("Dot detection complete. Results saved to:", output_file)
