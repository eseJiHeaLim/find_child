import tkinter
from math import*

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.gedfmetry("640x480+100+100")
window.resizable(False, False)
temp_child_name=0
temp_par_name=0
temp_contact1=0
temp_contact2=0

def save_child_name(event):
    child_name=str(entry_name.get())

def save_par_name(event):
    par_name=str(entry_Parname.get())

def save_contact1(event):
    contact1=str(entry_contact1.get())

def save_contact2(event):
    contact2=str(entry_contact2.get())


#아이이름 entry
entry_name=tkinter.Entry(window, width=25,bd=5)
entry_name.bind("<Return>", save_child_name)

entry_name.pack()

entry_Parname=tkinter.Entry(window, width=25,bd=5)
entry_Parname.bind("<Return>", save_par_name)
entry_Parname.pack( padx=70)

entry_contact1=tkinter.Entry(window, width=25,bd=5)
entry_contact1.bind("<Return>", save_contact1)
entry_contact1.pack()

entry_contact2=tkinter.Entry(window, width=25,bd=5)
entry_contact2.bind("<Return>", save_contact2)
entry_contact2.pack()

window.mainloop()