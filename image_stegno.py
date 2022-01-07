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

def encrypt():
    global path_image1
    global path_image2
    # img1 and img2 are the
    # two input images
    path_image1 = filedialog.askopenfilename()
    img1 = Image.open(path_image1)
    img1.thumbnail(image_display_size, Image.ANTIALIAS)
    img1 = np.asarray(img1)
    img1 = Image.fromarray(np.uint8(img1))
    render = ImageTk.PhotoImage(img1)
    img_1 = Label(app, image=render)
    img_1.image = render
    img_1.place(x=10, y=50)
    img1 = np.asarray(img1)

    path_image2 = filedialog.askopenfilename()
    img2 = Image.open(path_image2)
    img2.thumbnail(image_display_size, Image.ANTIALIAS)
    img2 = np.asarray(img2)
    img2 = Image.fromarray(np.uint8(img2))
    render = ImageTk.PhotoImage(img2)
    img_2 = Label(app, image=render)
    img_2.image = render
    img_2.place(x=290, y=50)
    img2 = np.asarray(img2)

    # img1 = cv2.imread('pic1.jpg')
    # img2 = cv2.imread('pic2.jpg')

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
  
      
# Decryption function
def decrypt():
      
    # Encrypted image
    img = cv2.imread('pic3in2.png') 
    width = img.shape[0]
    height = img.shape[1]
      
    # img1 and img2 are two blank images
    img1 = np.zeros((width, height, 3), np.uint8)
    img2 = np.zeros((width, height, 3), np.uint8)
      
    for i in range(width):
        for j in range(height):
            for l in range(3):
                v1 = format(img[i][j][l], '08b')
                v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
                v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4
                  
                # Appending data to img1 and img2
                img1[i][j][l]= int(v2, 2)
                img2[i][j][l]= int(v3, 2)
      
    # These are two images produced from
    # the encrypted image
    cv2.imwrite('pic2_re.png', img1)
    cv2.imwrite('pic3_re.png', img2)
      
      
# Driver's code
# encrypt()
# decrypt()
app = Tk()
app.configure(background='lavender')
app.title("Encrypt")
app.geometry('600x600')
# create a button for calling the function on_click
on_click_button = Button(app, text="Choose Image", bg='white', fg='black', command=encrypt)
on_click_button.place(x=250, y=10)
app.mainloop()

decrypt()