import numpy as np
import cv2
import tkinter
import PIL
from PIL import Image
from PIL import ImageTk

# Load an color image
img = cv2.imread('8.jpg')

#Rearrang the color channel
b,g,r = cv2.split(img)
img = cv2.merge((r,g,b))

# A root window for displaying objects
root = tkinter.Tk()

# Convert the Image object into a TkPhoto object
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)

# Put it in the display window
tkinter.Label(root, image=imgtk).pack()

root.mainloop() # Start the GUI