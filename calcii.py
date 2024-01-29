from tkinter import *


def calculate():
    a = int(n1.get())
    b = int(n2.get())
    result = str(a+b)
    answer.config(text="Answer is :  " + result)


window = Tk()
window.configure(bg="grey")
head = Label(window, text="Calculator", bg="grey", fg="green", font='Arial')
head.pack()

n1 = Entry(window)
n1.pack()
n2 = Entry(window)
n2.pack()

button = Button(text="Calculate", bg="grey", fg="green", command=calculate)
button.pack()

answer = Label(window)
answer.pack()
window.mainloop()
