#Generate image preview by resizing to fit template dimensions
import cv2 as cv
import os
# User input for thumb nail dimensions
template             = cv.imread("reference.jpg")
t_height, t_width, c = template.shape

#Read image from which to generate thumb nail
inputPath = "/home/paok/Documents/Thumb-Nailify/Input/"
pictures = os.listdir(inputPath)
for pic in pictures:
    #Read image from imput folder
    currentPic = cv.imread(inputPath+pic)
    #Get scale factor
    h_factor = abs(t_height/currentPic.shape[0])
    w_factor = abs(t_width/currentPic.shape[1])
    # Establish New Dimensions
    dimensions = (int(currentPic.shape[1]*w_factor), int(currentPic.shape[0]*h_factor))
    # Resize picture
    thumbNail = cv.resize(currentPic, dimensions, interpolation = cv.INTER_AREA)
    # Write to output folder
    cv.imwrite("/home/paok/Documents/Thumb-Nailify/Output/"+pic,thumbNail)
print(pictures)