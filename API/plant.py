import numpy as np
# import matplotlib.pyplot as plt
import cv2
import os


def get_image(image):
    img = cv2.imread(image,cv2.IMREAD_UNCHANGED)#image2.jpeg or image3.png
    img = img.copy()

    width = 1000
    height = 1000
    dim = (width, height)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # define range of green color in HSV
    lower_green = np.array([26, 15, 15])
    upper_green = np.array([70, 255,255])


    # Threshold the HSV image to get only green colors
    mask = cv2.inRange (hsv, lower_green, upper_green)

    greencnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

    if len(greencnts)>0:
        green_area = max(greencnts, key=cv2.contourArea)
        (xg,yg,wg,hg) = cv2.boundingRect(green_area)
        cv2.rectangle(img,(xg,yg),(xg+wg, yg+hg),(250,0,0),2)

    os.remove(image)
    cv2.imwrite(image, img)

    return hg/100, image