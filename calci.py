from tkinter import *
import ast

root=Tk()

root.title("Calculator")
label1=Label(text="CALCULATOR",bg="black",fg="Red").grid(row=0,columnspan=10,sticky=W + E,ipady=5)
i=0

def takedigit(text):
    global i
    view.insert(i,text)
    i+=1

def takeop(show):
    global i
    view.insert(i,show)
    i+=1

def equal():
    entire=view.get()
    try:
        node=ast.parse(entire,mode="eval")
        result=eval(compile(node,'<string>','eval'))
        clearall()
        view.insert(0,result)
    except Exception:
        clearall()
        view.insert(0,"ERRORRRR")

def clearall():
    view.delete(0,END)

def zero():
    global i
    view.get()
    view.insert(i,0)

def undo():
    global i
    entire=view.get()
    new=entire[:-1]
    clearall()
    view.insert(0,new)

view=Entry(root,bg="pink",fg="Blue")
view.grid(row=1,columnspan=6,sticky=N + S + E + W,ipady=15)
counter=0
num=[1,2,3,4,5,6,7,8,9]
for i in reversed(range(3)):
    for j in range(3):
        btext=num[counter]
        Button(text=f"{btext}",width=4,height=4,bg="black",fg="White",command=lambda text=btext:takedigit(text)).grid(row=i+2,column=j)
        counter+=1

oper=['+','-','*','/','%','.']
count=0
for i in range(3):
    for j in range(2):
        op=oper[count]
        Button(text=f"{op}",width=4,height=4,bg="Black",fg="red",command=lambda show=op: takeop(show)).grid(row=i+2,column=j+3)
        count+=1

zer=Button(text='0',height=4,width=4,bg="Black",fg="white",command=zero).grid(row=6,column=1)
undo=Button(text="<-",height=4,width=4,bg="Black",fg="red",command=undo).grid(row=6,column=2)
eq=Button(text="=",height=4,width=9,bg="Black",fg="red",command=equal).grid(row=6,column=3,columnspan=2)
alc=Button(text="AC",height=4,width=4,bg="Black",fg="red",command=clearall).grid(row=6,column=0)

root.mainloop()