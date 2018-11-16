import tkinter

root=tkinter()

def retirve_input():
    input=textBox.get("1.0","end-1c")
    print(input)

textBox=Text(root,hight=2,width=10)
textBox.pack()

buttonCommit=Button(root,height=2,text="finish",command=lambda :retirve_input())

buttonCommit.pack()
root.mainloop()
