# -*- coding: utf-8 -*-
import numpy as np
import cv2
import tkinter as tk
import PIL
import os
from PIL import Image
from PIL import ImageTk
#import face_recognition

# 정보
info = [[0] * 30 for i in range(4)]
index = 0
find_index = 100;
temp_child_name = []
temp_par_name = []
temp_contact1 = []
temp_contact2 = []

# main window
window = tk.Tk()
window.title("main window")
window.geometry("640x550+100+100")
window.configure(background='white')

width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


class CamView():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.geometry("640x550+100+100")
        self.a = tk.Label(self.window, text='얼굴을 가까이 찍으세요').pack()
        self.lmain2 = tk.Label(self.window)
        self.lmain2.pack()
        self.takeP = tk.Button(self.window, text="사진찍기", command=enroll_take)
        self.takeP.pack()
        self.reTakeP = tk.Button(self.window, text="다시찍기", command=enroll_take)
        self.reTakeP.pack()
        self.turnNext = tk.Button(self.window, text="다음", command=self.enrollment_information)
        self.turnNext.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.show_frame()

    def show_frame(self):
        imgtk = ImageTk.PhotoImage(image=self.parent.img)
        self.lmain2.imgtk = imgtk
        self.lmain2.configure(image=imgtk)

    def close(self):
        self.parent.test_frame = None
        self.window.destroy()

    # enrollment window
    def enrollment_information(self):
        self.popup_enrollInformation = tk.Toplevel(window)
        self.popup_enrollInformation.geometry("640x550+100+100")
        self.popup_enrollInformation.title("정보입력")

        image = tk.PhotoImage(file="C:/github/find_child/data/{}.png".format(index))
        a = tk.Label(self.popup_enrollInformation, text='미아등록').pack(side="top")
        self.label = tk.Label(self.popup_enrollInformation, image=image)
        self.label.pack()

        self.entry_name = tk.Text(self.popup_enrollInformation, height=1, width=10)
        self.entry_name.pack()

        self.entry_Parname = tk.Text(self.popup_enrollInformation, height=1, width=10)
        self.entry_Parname.pack()

        self.entry_contact1 = tk.Text(self.popup_enrollInformation, height=1, width=10)
        self.entry_contact1.pack()

        self.entry_contact2 = tk.Text(self.popup_enrollInformation, height=1, width=10)
        self.entry_contact2.pack()

        self.buttonCommit = tk.Button(self.popup_enrollInformation, height=2, text="finish",
                                      command=lambda: save_input(self.entry_name, self.entry_Parname,
                                                                 self.entry_contact1, self.entry_contact2))

        self.buttonCommit.pack()

        self.popup_enrollInformation.mainloop()


class CamView2():
    def __init__(self, parent):
        self.parent = parent
        self.window = tk.Toplevel(parent)
        self.window.geometry("850x400+100+100")
        self.lmain2 = tk.Label(self.window)
        self.lmain2.pack()
        self.takeP = tk.Button(self.window, text="사진찍기", command=enroll_test_take)
        self.takeP.pack()
        self.reTakeP = tk.Button(self.window, text="다시찍기", command=enroll_test_take)
        self.reTakeP.pack()
        self.turnNext = tk.Button(self.window, text="다음", command=check_imformation)
        self.turnNext.pack()
        self.window.protocol("WM_DELETE_WINDOW", self.close)
        self.show_frame()

    def show_frame(self):
        imgtk = ImageTk.PhotoImage(image=self.parent.img)
        self.lmain2.imgtk = imgtk
        self.lmain2.configure(image=imgtk)

    def close(self):
        self.parent.test_frame = None
        self.window.destroy()


class Main(tk.Frame):
    def __init__(self, parent):

        self.lmain = tk.Label(parent)
        self.lmain.place()
        self.test_frame = None
        frame = tk.Frame.__init__(self, parent)
        enrollment = tk.Button(frame, text='미아등록', width=15, height=20, command=self.load_window, bg="#F1C40F")
        enrollment.place(x=150, y=100)
        _find = tk.Button(frame, text='보호자 찾기', width=15, height=20, command=self.load_window2, bg="#3498DB")
        _find.place(x=350, y=100)
        self.do_stuff()

    def do_stuff(self):
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        self.img = Image.fromarray(cv2image)
        if self.test_frame != None:
            self.test_frame.show_frame()
        self.lmain.after(10, self.do_stuff)

    def load_window(self):
        if self.test_frame == None:
            self.test_frame = CamView(self)

    def load_window2(self):
        if self.test_frame == None:
            self.test_frame = CamView2(self)


def enroll_take():
    global index
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "{}.png".format(index)
    path = 'C:/github/find_child/data'
    cv2.imwrite(os.path.join(path, img_name), frame)
    print("{} written!".format(img_name))


# take image to find child- test data
def enroll_test_take():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "test_data.png"
    cv2.imwrite(os.path.join(img_name), frame)
    print("{} written!".format(img_name))


# update imformation
def save_child_name(entry_name):
    global temp_child_name
    temp_child_name = str(entry_name.get())
    print(temp_child_name)


def save_par_name(entry_Parname):
    global temp_par_name
    temp_par_name = str(entry_Parname.get())


def save_contact1(entry_contact1):
    global temp_contact1
    temp_contact1 = str(entry_contact1.get())


def save_contact2(entry_contact2):
    global temp_contact2
    temp_contact2 = str(entry_contact2.get())


# save imformation
def save_input(entry_name, entry_Parname, entry_contact1, entry_contact2):
    global index
    global info
    global temp_child_name
    global temp_par_name
    global temp_contact1
    global temp_contact2
    temp_child_name = entry_name.get("1.0", "end-1c")
    temp_par_name = entry_Parname.get("1.0", "end-1c")
    temp_contact1 = entry_contact1.get("1.0", "end-1c")
    temp_contact2 = entry_contact2.get("1.0", "end-1c")
    info[index][0] = temp_child_name
    info[index][1] = temp_par_name
    info[index][2] = temp_contact1
    info[index][3] = temp_contact2
    print(info[index][0])
    print(info[index][1])
    print(info[index][2])
    print(info[index][3])
    index = index + 1


def destory(frame):
    frame.destory()


class showInformation():
    # show find result window
    def __init__(self):
        global find_index
        global info

        self.popup_result = tk.Toplevel(window)
        self.popup_result.geometry("640x550+100+100")
        self.popup_result.title("found Child")
        a = tk.Label(self.popup_result, text='보호자 찾기').pack(side="top")
        # 찾은 이미지
        self.image = tk.PhotoImage(file="/home/pi/Desktop/findChild/data/{}.png".format(find_index))
        self.label = tk.Label(self.popup_result, image=self.image)
        self.label.pack()

        self.label_name = tk.Label(self.popup_result, text="아이 이름 : " + str(info[find_index][0]))
        self.label_name.pack()

        self.label_parname = tk.Label(self.popup_result, text="부모 이름 : " + str(info[find_index][1]))
        self.label_parname.pack()

        self.label_num1 = tk.Label(self.popup_result, text="보호자 번호1 : " + str(info[find_index][2]))
        self.label_num1.pack()

        self.label_num2 = tk.Label(self.popup_result, text="보호자 번호2 : " + str(info[find_index][3]))
        self.label_num2.pack()

        self.finish = tk.Button(self.popup_result, text="finish", command=self.closeWindow)
        self.finish.pack()
        self.popup_result.mainloop()

    def closeWindow(self):
        self.popup_result.destroy()


def check_imformation():
    """
    global find_index
    picture_of_me = face_recognition.load_image_file("/home/pi/Desktop/findChild/test_data.png")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    for root, dirs, files in os.walk('/home/pi/Desktop/findChild/data'):
        for fname in files:
            full_fname = os.path.join(root, fname)
            unknown_picture = face_recognition.load_image_file(full_fname)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
            if results[0] == True:
                find_index = int(fname.split('.')[0])
                find_index = int(find_index)
                print (find_index)
            else:
                print("not exist child")
    """
    showInformation()


Main(window)
window.mainloop()