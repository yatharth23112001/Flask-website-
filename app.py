from flask import Flask, redirect,request
from flask.templating import render_template
import paint
from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
import cv2
import numpy as np
import math
import sudoku_testing
import encrypt
import decryption

app = Flask(__name__)
app_tk = Tk()
txt = Text()
@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route('/video_feed')
def video_feed():
    paint.painting()
    return redirect("/")

@app.route('/stegano')
def stegano():
    return render_template("steganography.html")

@app.route('/encryptmes', methods = ['POST'])
def encryptmes():
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)  
        f1 = request.form['text'] 
        encrypt.encrypt_data_into_image(f.filename,f1)
    return redirect("/stegano")

@app.route('/decrypt', methods = ['POST'])
def decrypt():
    if request.method == 'POST':  
        f = request.files['file']  
        f.save(f.filename)   
        decryption.decrypt(f.filename)
    return redirect("/stegano")

@app.route('/sudoku')
def sudoku():
    sudoku_testing.solve_soduku()
    return redirect("/")

@app.route('/information')
def info():
    return render_template("info.html")


if __name__ == "__main__":  
    app.run(host="59.88.162.5",port=5000)
