from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math


def encrypt_data_into_image(uploaded_image,txt):
    # Step 2
    # global path_image
    # data = txt.get(1.0, "end-1c")
    data = txt
    # load the image
    img = cv2.imread(uploaded_image)
    # break the image into its character level. Represent the characyers in ASCII.
    data = [format(ord(i), '08b') for i in data]
    _, width, _ = img.shape
    # algorithm to encode the image
    PixReq = len(data) * 3

    RowReq = PixReq/width
    RowReq = math.ceil(RowReq)

    count = 0
    charCount = 0
    # Step 3
    for i in range(RowReq + 1):
        # Step 4
        while(count < width and charCount < len(data)):
            char = data[charCount]
            charCount += 1
            # Step 5
            for index_k, k in enumerate(char):
                if((k == '1' and img[i][count][index_k % 3] % 2 == 0) or (k == '0' and img[i][count][index_k % 3] % 2 == 1)):
                    img[i][count][index_k % 3] -= 1
                if(index_k % 3 == 2):
                    count += 1
                if(index_k == 7):
                    if(charCount*3 < PixReq and img[i][count][2] % 2 == 1):
                        img[i][count][2] -= 1
                    if(charCount*3 >= PixReq and img[i][count][2] % 2 == 0):
                        img[i][count][2] -= 1
                    count += 1
        count = 0

    cv2.imwrite("encrypted_image.png", img)
    # font = cv2.FONT_HERSHEY_SIMPLEX
  
    # # org
    # org = (50, 50)
    # # fontScale
    # fontScale = 1
    # # Blue color in BGR
    # color = (255, 0, 0)
    # # Line thickness of 2 px
    # thickness = 2

    # image = cv2.putText(img, 'Encryption Complete', org, font,fontScale, color, thickness, cv2.LINE_AA)
    # cv2.imshow("encrypted_image", image)
    # cv2.waitKey(0) 
    # #closing all open windows 
    # cv2.destroyAllWindows() 
