from tkinter import *

root = Tk()
root.title("Calculator")
root.configure(background="lightsteelblue4")
root.geometry("390x290")
root.resizable("False","False")

def clear_entry():
    userin.delete(0,END)

def btn_pressed(num):
    digit_pressed = userin.get()
    userin.delete(0,END)
    userin.insert(0,digit_pressed+str(num))

def operation_selected(operator):
    num1 = userin.get()
    global operation
    operation = operator
    global f_num
    f_num=int(num1)
    userin.delete(0,END)

def result():
    num2 = userin.get()
    userin.delete(0, END)
    if operation == "+":
        userin.insert(0,f_num+int(num2))
    elif operation == "-":
        userin.insert(0, f_num - int(num2))
    elif operation == "x":
        userin.insert(0, f_num * int(num2))
    elif operation == "/":
        userin.insert(0, f_num / int(num2))


#create
clear = Button(root,text="C",padx=30,pady=5,bg="dodgerblue4",fg="white",font="bold",command=clear_entry)

userin = Entry(root,width=18,font=("Arial",18,"bold"))

btn_0 = Button(root,text="0",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(0))
btn_eq = Button(root,text="=",padx=76,pady=5,bg="lightgray",font="bold",command=result)

btn_1 = Button(root,text="1",padx=30,pady=5,bg="black",fg="white",font="bold", command=lambda:btn_pressed(1))
btn_2 = Button(root,text="2",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(2))
btn_3 = Button(root,text="3",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(3))

btn_4 = Button(root,text="4",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(4))
btn_5 = Button(root,text="5",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(5))
btn_6 = Button(root,text="6",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(6))

btn_7 = Button(root,text="7",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(7))
btn_8 = Button(root,text="8",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(8))
btn_9 = Button(root,text="9",padx=30,pady=5,bg="black",fg="white",font="bold",command=lambda:btn_pressed(9))

btn_add = Button(root,text="+",padx=28,pady=5,bg="dodgerblue4",fg="white",font="bold",command=lambda:operation_selected("+"))
btn_sub = Button(root,text="-",padx=30,pady=5,bg="dodgerblue4",fg="white",font="bold",command=lambda:operation_selected("-"))
btn_mul = Button(root,text="x",padx=29,pady=5,bg="dodgerblue4",fg="white",font="bold",command=lambda:operation_selected("x"))
btn_div = Button(root,text="/",padx=31,pady=5,bg="dodgerblue4",fg="white",font="bold",command=lambda:operation_selected("/"))


#display
clear.grid(row=0,column=3)

userin.grid(row=0,column=0,columnspan=3,pady=8,ipadx=10,ipady=10)

btn_7.grid(row=1,column=0,padx=3,pady=2)
btn_8.grid(row=1,column=1,padx=3,pady=2)
btn_9.grid(row=1,column=2,padx=3,pady=2)

btn_4.grid(row=2,column=0,padx=3,pady=2)
btn_5.grid(row=2,column=1,padx=3,pady=2)
btn_6.grid(row=2,column=2,padx=3,pady=2)

btn_1.grid(row=3,column=0,padx=3,pady=2)
btn_2.grid(row=3,column=1,padx=3,pady=2)
btn_3.grid(row=3,column=2,padx=3,pady=2)

btn_0.grid(row=4,column=0,padx=3,pady=2)
btn_eq.grid(row=4,column=1,columnspan=2)

btn_add.grid(row=4,column=3,padx=3,pady=2)
btn_sub.grid(row=3,column=3,padx=3,pady=2)
btn_mul.grid(row=2,column=3,padx=3,pady=2)
btn_div.grid(row=1,column=3,padx=3,pady=2)

root.mainloop()