from tkinter import *
root=Tk()
root.geometry("300x600")
root.maxsize(300,650)
root.title("My Calculator")
root.wm_iconbitmap("calculator.ico")
def click(event):
    global scvalue
    text=event.widget.cget("text")   # cget--To extract the text from button widget
    print(text)
    if text=="=":
        if scvalue.get().isdigit():
            value=scvalue.get()
        else:
            try:
                value=eval(scvalue.get())
            except Exception as e:
                print(e)
                value="Error"
        scvalue.set(value)
        screen.update()

    elif text=="C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()                     #------------------screen.update function update the value in the screen

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 40 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
f.pack()

b=Button(f,text="9",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="8",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="7",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)


f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
b=Button(f,text="6",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="5",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="4",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
b=Button(f,text="3",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="2",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="1",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
b=Button(f,text="0",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=13,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="-",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="*",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()

f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
b=Button(f,text="/",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="%",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="=",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()


f=Frame(root,bg="grey",borderwidth=5,relief=SUNKEN)
b=Button(f,text="C",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text=".",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
b=Button(f,text="00",font="lucida 15 bold",padx=15,pady=5)
b.pack(side=LEFT,padx=10,pady=12)
b.bind("<Button-1>",click)
f.pack()
root.mainloop()
