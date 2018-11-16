import numpy as np
import cv2
import tkinter
import PIL
import os
from PIL import Image
from PIL import ImageTk
# 정보
info=[[0]*30 for i in range(4)]
index=0

temp_child_name = []
temp_par_name = []
temp_contact1 = []
temp_contact2 = []



#메인 페이지
window=tkinter.Tk()
window.title("main")
window.geometry("640x400+100+100")
window.resizable(False, False)
label=tkinter.Label(window, text="미아 방지")
label.pack()

width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)



def take ():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "opencv_frame_{}.png".format(0)
    cv2.imwrite(os.path.join(img_name), frame)
    print("{} written!".format(img_name))

def show_frame(lmain):
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)

def save_child_name(entry_name):
    global temp_child_name
    temp_child_name=str(entry_name.get())
    print(temp_child_name)

def save_par_name(entry_Parname):
    global temp_par_name
    temp_par_name=str(entry_Parname.get())

def save_contact1(entry_contact1):
    global temp_contact1
    temp_contact1=str(entry_contact1.get())

def save_contact2(entry_contact2):
    global temp_contact2
    temp_contact2=str(entry_contact2.get())

def save_input(entry_name,entry_Parname,entry_contact1,entry_contact2):
    global index
    global info
    global temp_child_name
    global temp_par_name
    global temp_contact1
    global temp_contact2
    temp_child_name= entry_name.get("1.0","end-1c")
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
    index=index+1


# add information about child
def enrollment_information():


    popup_enrollInformation=tkinter.Toplevel(window)
    popup_enrollInformation.geometry("800x800+100+100")
    popup_enrollInformation.title("정보입력")

    image = tkinter.PhotoImage(file="opencv_frame_0.png")

    label = tkinter.Label(popup_enrollInformation, image=image)
    label.pack()

    entry_name = tkinter.Text(popup_enrollInformation,height=1,width=10)
    entry_name.pack()

    entry_Parname = tkinter.Text(popup_enrollInformation,height=1,width=10)
    entry_Parname.pack()

    entry_contact1 = tkinter.Text(popup_enrollInformation,height=1,width=10)
    entry_contact1.pack()

    entry_contact2 = tkinter.Text(popup_enrollInformation,height=1,width=10)
    entry_contact2.pack()

    buttonCommit = tkinter.Button(popup_enrollInformation, height=2, text="finish", command=lambda: save_input(entry_name,entry_Parname,entry_contact1,entry_contact2))

    buttonCommit.pack()

    popup_enrollInformation.mainloop()

#미아 등록 함수
def enrollment():
    popup_enrollment = tkinter.Toplevel(window)
    popup_enrollment.wm_title("enrollment")
    popup_enrollment.geometry("640x400+100+100")
    popup_enrollment.tkraise(window)  # This just tells the message to be on top of the root window.
    takeP=tkinter.Button(popup_enrollment, text="사진찍기", command=take)
    reTakeP=tkinter.Button(popup_enrollment, text="다시찍기", command=take)
    turnNext = tkinter.Button(popup_enrollment, text="다음", command=enrollment_information)
    takeP.pack()
    reTakeP.pack()
    turnNext.pack()
    lmain = tkinter.Label(popup_enrollment)
    lmain.pack()
    lmain.after(1, show_frame(lmain))
    popup_enrollment.mainloop()


#미아등록 버튼
button_enrollment= tkinter.Button(window, text="미아등록" , command=enrollment)
button_enrollment.pack()


def findPar():
    popup_findPar = tkinter.Toplevel(window)
    popup_findPar.wm_title("findPAr")
    popup_findPar.geometry("640x400+100+100")
    popup_findPar.tkraise(window)  # This just tells the message to be on top of the    root window.
    tkinter.Button(popup_findPar, text="Okay", command=popup_findPar.destroy).pack()

#보호자 찾기
button_find= tkinter.Button(window, text="보호자 찾기" , command=findPar)
button_find.pack()
window.mainloop()

