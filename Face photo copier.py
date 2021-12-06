import face_recognition as fr
import os
import sys
from PIL import Image,ImageTk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

def raise_frame(frame):
	frame.tkraise()

def select_image():
	image_loc = filedialog.askopenfilename(initialdir=os.getcwd(), title="Select Image File",filetypes=(("JPG File","*.jpg"),("PNG File","*.png"),("RAW File","*.cr2"),("All Files","*.*")))
	img = Image(image_loc)
	img.thumbnail((350,350))
	img = ImageTk.PhotoImage(img)
	view_image.configure(image=img)
	view_image = img
root = Tk()
#main = Frame(root)

#for frame in (main):
#	frame.grid(row=0,column=0,sticky=news)

root.geometry("600x400+120+120")
root.title("Face Photo Copier")

Label(root, text="Upload Your Photo",font=("Times New Roman",15,"bold")).pack(side=LEFT,fill=X)
view_image=Label(root)
view_image.pack()
User_Image=Button(root,text="Select Image",font=("Times New Roman",10,"bold"),command=select_image)
User_Image.pack(side=LEFT,fill=X)
root.mainloop()