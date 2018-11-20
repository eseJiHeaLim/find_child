import tkinter as tk
import cv2
import os
from PIL import Image, ImageTk
a="JiHea"
width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

root = tk.Tk()
root.bind('<Escape>', lambda e: root.quit())
root.geometry("640x400+100+100")
lmain = tk.Label(root)
lmain.pack()


def take ():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "opencv_frame_{}.png".format(0)
    cv2.imwrite(os.path.join(img_name), frame)
    print("{} written!".format(img_name))


bu=tk.Button(root, text="W찍기", command=take)
bu.pack()

def show_frame():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
    lmain.after(100, show_frame)


label=tk.Label(root, text= "이름"+a )
label.pack()
show_frame()
root.mainloop()