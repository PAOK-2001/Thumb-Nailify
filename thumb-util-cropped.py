#Generate image preview by cropping image from the center
import cv2 as cv
import os
# User input for thumb nail dimensions
t_height = int(input("Introduce Thumbnail Height: "))
t_width = int(input("Introduce ThumbnailW Width: "))

#Read image from which to generate thumb nail
inputPath = "/home/paok/Documents/Thumbn-util/Input/"
pictures = os.listdir(inputPath)
for pic in pictures:
    #Read image from imput folder
    currentPic = cv.imread(inputPath+pic)
    # Crop thumbnail from center 
    thumbNail  = currentPic[int((currentPic.shape[0]/2) -(t_height/2)):int((currentPic.shape[0]/2) + (t_height/2)),int((currentPic.shape[1]/2) -(t_width/2)):int((currentPic.shape[1]/2)+(t_width/2))]
    # Write to output folder
    cv.imwrite("/home/paok/Documents/Thumbn-util/Output/thumb_"+pic,thumbNail)
print(pictures)