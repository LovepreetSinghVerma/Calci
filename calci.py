from tkinter import *
import ast

root=Tk()
#Giving a title to the project
root.title("Calculator")
#adding a label on the top
label1=Label(text="CALCULATOR",bg="black",fg="Red").grid(row=0,columnspan=10,sticky=W + E,ipady=5)
i=0

#func to fetch the digits
def takedigit(text):
    global i
    view.insert(i,text)
    i+=1

#func to fetch operators
def takeop(show):
    global i
    view.insert(i,show)
    i+=1

#func to fetch equal-to operator and provide result
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

#func to clear the entry
def clearall():
    view.delete(0,END)

#func to insert digit(zero)
def zero():
    global i
    view.get()
    view.insert(i,0)

#func to undo the entry
def undo():
    global i
    entire=view.get()
    new=entire[:-1]
    clearall()
    view.insert(0,new)

#adding an entry field
view=Entry(root,bg="pink",fg="Blue")
view.grid(row=1,columnspan=6,sticky=N + S + E + W,ipady=15)

#adding buttons for digits(1 to 9)
counter=0
num=[1,2,3,4,5,6,7,8,9]
for i in reversed(range(3)):
    for j in range(3):
        btext=num[counter]
        Button(text=f"{btext}",width=4,height=4,bg="black",fg="White",command=lambda text=btext:takedigit(text)).grid(row=i+2,column=j)
        counter+=1

#adding buttons for operators
oper=['+','-','*','/','%','.']
count=0
for i in range(3):
    for j in range(2):
        op=oper[count]
        Button(text=f"{op}",width=4,height=4,bg="Black",fg="red",command=lambda show=op: takeop(show)).grid(row=i+2,column=j+3)
        count+=1

#adding other Misc buttons
zer=Button(text='0',height=4,width=4,bg="Black",fg="white",command=zero).grid(row=6,column=1)
undo=Button(text="<-",height=4,width=4,bg="Black",fg="red",command=undo).grid(row=6,column=2)
eq=Button(text="=",height=4,width=9,bg="Black",fg="red",command=equal).grid(row=6,column=3,columnspan=2)
alc=Button(text="AC",height=4,width=4,bg="Black",fg="red",command=clearall).grid(row=6,column=0)

root.mainloop()
