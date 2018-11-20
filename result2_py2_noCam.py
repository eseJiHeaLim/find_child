import numpy as np
import cv2
import tkinter as tk
import PIL
import os
from PIL import Image
from PIL import ImageTk
#import face_recognition
# 정보
info=[[0]*30 for i in range(4)]
index=0
find_index=-1;
temp_child_name = []
temp_par_name = []
temp_contact1 = []
temp_contact2 = []



# main window
window=tk.Tk()
window.title("main")
window.geometry("640x400+100+100")
window.resizable(False, False)
label=tk.Label(window, text="미아 방지")
label.pack()

'''
width, height = 300, 300
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
'''
'''
# take image to upload data
def enroll_take ():
    global index
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "data{}.png".format(index)
    cv2.imwrite(os.path.join(img_name), frame)
    print("{} written!".format(img_name))

# take image to find child- test data
def enroll_test_take ():
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    img_name = "test_data{}.png".format(0)
    cv2.imwrite(os.path.join(img_name), frame)
    print("{} written!".format(img_name))

# camera preview
def show_frame(lmain):
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
    img = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image=img)
    lmain.imgtk = imgtk
    lmain.configure(image=imgtk)
'''

# update imformation
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

# save imformation
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


# enrollment window
def enrollment_information():
    global index
    popup_enrollInformation=tk.Toplevel(window)
    popup_enrollInformation.geometry("800x800+100+100")
    popup_enrollInformation.title("정보입력")

    image = tk.PhotoImage(file="test_data{}.png".format(index))

    label = tk.Label(popup_enrollInformation, image=image)
    label.pack()

    entry_name = tk.Text(popup_enrollInformation,height=1,width=10)
    entry_name.pack()

    entry_Parname = tk.Text(popup_enrollInformation,height=1,width=10)
    entry_Parname.pack()

    entry_contact1 = tk.Text(popup_enrollInformation,height=1,width=10)
    entry_contact1.pack()

    entry_contact2 = tk.Text(popup_enrollInformation,height=1,width=10)
    entry_contact2.pack()

    buttonCommit = tk.Button(popup_enrollInformation, height=2, text="finish", command=lambda: save_input(entry_name,entry_Parname,entry_contact1,entry_contact2))

    buttonCommit.pack()

    popup_enrollInformation.mainloop()

# to upload imformation of image window
def enrollment():
    popup_enrollment = tk.Toplevel(window)
    popup_enrollment.wm_title("enrollment")
    popup_enrollment.geometry("640x400+100+100")
    popup_enrollment.tkraise(window)  # This just tells the message to be on top of the root window.
    takeP=tk.Button(popup_enrollment, text="사진찍기")
    reTakeP=tk.Button(popup_enrollment, text="다시찍기")
    turnNext = tk.Button(popup_enrollment, text="다음", command=enrollment_information)
    takeP.pack()
    reTakeP.pack()
    turnNext.pack()

    popup_enrollment.mainloop()


# show find result window
def show_information():
    global find_index
    global info

    popup_result=tk.Toplevel(window)
    popup_result.geometry("800x800+100+100")
    popup_result.title("got it ")

    # 찾은 이미지
    image = tk.PhotoImage(file="test_data0.png")
    label = tk.Label(popup_result, image=image)
    label.pack()

    label_name = tk.Label(popup_result, text="아이 이름 : " + info[find_index][0])
    label_name.pack()

    label_parname = tk.Label(popup_result, text="부모 이름 : " + info[find_index][1])
    label_parname.pack()

    label_num1 = tk.Label(popup_result, text="보호자 번호1     : " + info[find_index][2])
    label_num1.pack()

    label_num2 = tk.Label(popup_result, text="보호자 번호2 : " + info[find_index][3])
    label_num2.pack()

    popup_result.mainloop()

def check_imformation():
    global find_index
    picture_of_me = face_recognition.load_image_file("test_data.png")
    my_face_encoding = face_recognition.face_encodings(picture_of_me)[0]

    for root, dirs, files in os.walk('/home/odroid/Desktop/test_facerecognition/inforamtion'):
        for fname in files:
            full_fname = os.path.join(root, fname)
            unknown_picture = face_recognition.load_image_file(full_fname)
            unknown_face_encoding = face_recognition.face_encodings(unknown_picture)[0]
            results = face_recognition.compare_faces([my_face_encoding], unknown_face_encoding)
            if results[0] == True:
                find_index=int(fname.split('.')[0])
            else:
                print("not exist child")
    show_information()

def findPar():

    popup_findPar = tk.Toplevel(window)
    popup_findPar.wm_title("findPAr")
    popup_findPar.geometry("640x400+100+100")
    popup_findPar.tkraise(window)  # This just tells the message to be on top of the    root window.
    takenP = tk.Button(popup_findPar, text="사진찍기")
    reTakenP = tk.Button(popup_findPar, text="다시찍기")
    Next = tk.Button(popup_findPar, text="다음")
    takenP.pack()
    reTakenP.pack()
    Next.pack()

    popup_findPar.mainloop()

# main window upload child imformation
button_enrollment= tk.Button(window, text="미아등록" , command=enrollment)
button_enrollment.pack()

#main window find child button
button_find= tk.Button(window, text="보호자 찾기" , command=findPar)
button_find.pack()

window.mainloop()

