from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import random
  
global path_image1
global path_image2
image_display_size = 300, 300
# Encryption function

def encrypt(image1,image2):
    img1 = cv2.imread(image1)
    img2 = cv2.imread(image2)

    for i in range(img2.shape[0]):
        for j in range(img2.shape[1]):
            for l in range(3):
                  
                # v1 and v2 are 8-bit pixel values
                # of img1 and img2 respectively
                v1 = format(img1[i][j][l], '08b')
                v2 = format(img2[i][j][l], '08b')
                  
                # Taking 4 MSBs of each image
                v3 = v1[:4] + v2[:4] 
                  
                img1[i][j][l]= int(v3, 2)
                  
    cv2.imwrite('pic3in2.png', img1)
    font = cv2.FONT_HERSHEY_SIMPLEX
  
    # org
    org = (50, 50)
    # fontScale
    fontScale = 1
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2

    image = cv2.putText(img1, 'Encryption Complete', org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("encrypted_image", image)
    cv2.waitKey(0) 
    #closing all open windows 
    cv2.destroyAllWindows() 