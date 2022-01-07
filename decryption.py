import cv2
from tkinter import filedialog, Tk, Button, Label
from PIL import Image, ImageTk
import numpy as np

image_display_size = 500, 350


def decrypt(uploaded_image):
    # Algorithm to decrypt the data from the image
    img = cv2.imread(uploaded_image)
    data = []
    stop = False
    for index_i, i in enumerate(img):
        i.tolist()
        for index_j, j in enumerate(i):
            if((index_j) % 3 == 2):
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                if(bin(j[2])[-1] == '1'):
                    stop = True
                    break
            else:
                # first pixel
                data.append(bin(j[0])[-1])
                # second pixel
                data.append(bin(j[1])[-1])
                # third pixel
                data.append(bin(j[2])[-1])
        if(stop):
            break

    message = []
    # join all the bits to form letters (ASCII Representation)
    for i in range(int((len(data)+1)/8)):
        message.append(data[i*8:(i*8+8)])
    # join all the letters to form the message.
    message = [chr(int(''.join(i), 2)) for i in message]
    message = ''.join(message)
    font = cv2.FONT_HERSHEY_SIMPLEX
  
    # org
    org = (50, 50)
    # fontScale
    fontScale = 1
    # Blue color in BGR
    color = (255, 0, 0)
    # Line thickness of 2 px
    thickness = 2

    image = cv2.putText(img, message, org, font,fontScale, color, thickness, cv2.LINE_AA)
    cv2.imshow("decrypted_image", image)
    cv2.waitKey(0) 
    #closing all open windows 
    cv2.destroyAllWindows() 
