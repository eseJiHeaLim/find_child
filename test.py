import tkinter

window=tkinter.Tk()
window.title("YUN DAE HEE")
window.geometry("640x400+100+100")
window.resizable(True, True)

image=tkinter.PhotoImage(file="opencv_frame_0.png")

label=tkinter.Label(window, image=image)
label.pack()

window.mainloop()