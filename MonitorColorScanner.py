# This code is made to run on the user's computer. Not on the server unit

import numpy as np, cv2, requests
from PIL import ImageGrab

def mostFrequent(colorList):
    highestFreq = 0
    if colorList: # Check if the colorList has any RGB values in it
        color = colorList[0] # initiate color variable with the first RGB value

        for i in colorList: # Iterate through the list
            currFreq = colorList.count(i) # Count how many times the current color occurs in the list
            if currFreq > highestFreq: # Check if it appears more often than all other colors checked
                highestFreq = currFreq # Set new value for highest frequency
                color = i # Save the color in the variable that will be returned
        return color # Return the most frequent color
    return [0, 0, 0] # Return black if the list of colors is empty

step = 30 # How many pixels to skip in both x and y direction when sampling colors
xPixels = 1344 # Number of pixels in the x direction of the checked area
yPixels = 756 # Number of pixels in the y direction of the checked area
serverAddress = "http://192.168.1.124:3000" # Address for the main server that controls all info about the LED strip

while True: # Main script loop
    if requests.get(f"{serverAddress}/modes/current") != "screenSync": # Check if the LED strip is currently in the right mode
        requests.get(f"{serverAddress}/modes/set?mode=screenSync") # Change the mode if it is wrong

    img = ImageGrab.grab(bbox=(192, 108, 1536, 864)) # Take a screenshot of the screen for processing
    imgNP = np.array(img) # Turn the image into a numPy array of all RGB values for easier processing

    imArr = np.frombuffer(img.tobytes(), dtype=np.uint8) # Encode image as bytes
    imArr = imArr.reshape((img.size[1], img.size[0], 3)) # reshape encoded image
    pixelArray = [] # Initiate an empty list for saving all pixels that will be analyzed

    for y in range(0, yPixels, step): # Iterate through all pixels in the y direction, skipping the amount specified in step for every iteration
        for x in range(0, xPixels, step): # Iterate through all pixels in the x direction, skipping the amount specified in step for every iteration
            px = imArr[y][x] # Grab pixel at current x and y coordinates

            if px[0] != 0 and px[1] != 0 and px[2] != 0:
                pixelArray.append([px[0], px[1], px[2]]) # Add the color if it is not complete black

    mostFrequentColor = mostFrequent(pixelArray) # Get most frequent color in list
    print(mostFrequentColor)
    requests.get(f"{serverAddress}/rgb?br=1000&r={mostFrequentColor[0]}&g={mostFrequentColor[1]}&b={mostFrequentColor[2]}") # Send the most frequent color to the main server