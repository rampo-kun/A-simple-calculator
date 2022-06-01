from tkinter import *

root = Tk()
root.title("Simple Calculator")
e = Entry(root, width=45, borderwidth=3)
e.grid(row=0, column=0, columnspan=3, padx=10,pady=10)

def buttonclick(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current)+str(number))

def buttonclear():
    e.delete(0,END)

def buttonadd():
    firstnumber = e.get()
    global firstnum
    global math
    math = 'addition'
    firstnum = int(firstnumber)
    e.delete(0,END)

def buttonsubtract():
    firstnumber = e.get()
    global firstnum
    global math
    math = 'subtraction'
    firstnum = int(firstnumber)
    e.delete(0,END)

def buttondivide():
    firstnumber = e.get()
    global firstnum
    global math
    math = 'division'
    firstnum = int(firstnumber)
    e.delete(0, END)

def buttonmultiply():
    firstnumber = e.get()
    global firstnum
    global math
    math = 'multiply'
    firstnum = int(firstnumber)
    e.delete(0, END)

def buttonequals():
    secondnumber = e.get()
    e.delete(0,END)
    if math == 'addition':
        sum = e.insert(0,firstnum + int(secondnumber))
    elif math == 'subtraction':
        sum = e.insert(0, firstnum - int(secondnumber))
    elif math == 'division':
        sum = e.insert(0, firstnum / int(secondnumber))
    elif math == 'multiply':
        sum = e.insert(0, firstnum * int(secondnumber))

#Buttons

button1 = Button(root,text='1',padx=40,pady=20,command=lambda : buttonclick(1))
button2 = Button(root,text='2',padx=40,pady=20,command=lambda : buttonclick(2))
button3 = Button(root,text='3',padx=40,pady=20,command=lambda : buttonclick(3))
button4 = Button(root,text='4',padx=40,pady=20,command=lambda : buttonclick(4))
button5 = Button(root,text='5',padx=40,pady=20,command=lambda : buttonclick(5))
button6 = Button(root,text='6',padx=40,pady=20,command=lambda : buttonclick(6))
button7 = Button(root,text='7',padx=40,pady=20,command=lambda : buttonclick(7))
button8 = Button(root,text='8',padx=40,pady=20,command=lambda : buttonclick(8))
button9 = Button(root,text='9',padx=40,pady=20,command=lambda : buttonclick(9))
button0 = Button(root,text='0',padx=40,pady=20,command=lambda : buttonclick(0))
button_add = Button(root, text='+', padx=39, pady=20, command=buttonadd)
button_equals = Button(root, text='=', padx=91, pady=20, command=buttonequals)
button_clear = Button(root, text='Clear', padx=79, pady=20, command=buttonclear)
button_subtract = Button(root, text='-',padx= 41, pady=20,command=buttonsubtract)
button_multiply = Button(root, text='*',padx= 41, pady=20,command=buttonmultiply)
button_divide = Button(root, text='/',padx= 41, pady=20,command=buttondivide)

'''Grid'''

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)
button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)
button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)
button0.grid(row=4,column=0)
button_clear.grid(row=4,column=1,columnspan=2)
button_add.grid(row=5,column=0)
button_equals.grid(row=5,column=1,columnspan=2)
button_subtract.grid(row=6,column=0)
button_multiply.grid(row=6,column=1)
button_divide.grid(row=6,column=2)


root.mainloop()
