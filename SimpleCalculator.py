from tkinter import *
import pyautogui

root = Tk()
root.geometry('242x338')
upFrame = Frame(root)
upFrame.pack(side = TOP,pady=20)
downFrame = Frame(root)
downFrame.pack(side = BOTTOM,pady=20)
root.title('Simple Calculator')


def motion(event):
    x, y = event.x, event.y
    print('{}, {}'.format(x, y))

#root.bind('<Motion>', motion)
expression = ""


equation = StringVar()
equation.set('')
entry = Entry(upFrame,textvariable=equation,width=20)
entry.grid(row=0,column=0)

def addExpression(strings):
    global expression
    expression = expression + strings
    equation.set(expression)

def equalpress():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

button1 = Button(downFrame, text='0',command=lambda: addExpression('0'),width=7 )
button1.grid(row=5,column=0)
button2 = Button(downFrame, text='00',command=lambda: addExpression('00'),width=7 )
button2.grid(row=5,column=1)
button3 = Button(downFrame, text='000',command=lambda: addExpression('000'),width=7 )
button3.grid(row=5,column=2)
button4 = Button(downFrame, text='1',command=lambda: addExpression('1'),width=7 )
button4.grid(row=2,column=0)
button5 = Button(downFrame, text='2',command=lambda: addExpression('2'),width=7 )
button5.grid(row=2,column=1)
button6 = Button(downFrame, text='3',command=lambda: addExpression('3'),width=7 )
button6.grid(row=2,column=2)
button7 = Button(downFrame, text='4',command=lambda: addExpression('4'),width=7 )
button7.grid(row=3,column=0)
button8 = Button(downFrame, text='5',command=lambda: addExpression('5'),width=7 )
button8.grid(row=3,column=1)
button9 = Button(downFrame, text='6',command=lambda: addExpression('6'),width=7 )
button9.grid(row=3,column=2)
button10 = Button(downFrame, text='7',command=lambda: addExpression('7'),width=7 )
button10.grid(row=4,column=0)
button11 = Button(downFrame, text='8',command=lambda: addExpression('8'),width=7 )
button11.grid(row=4,column=1)
button12= Button(downFrame, text='9',command=lambda: addExpression('9'),width=7 )
button12.grid(row=4,column=2)
button13 = Button(downFrame, text='+',command=lambda: addExpression('+'),width=7 )
button13.grid(row=1,column=0)
button14 = Button(downFrame, text='-',command=lambda: addExpression('-'),width=7 )
button14.grid(row=1,column=1)
button15 = Button(downFrame, text='*',command=lambda: addExpression('*'),width=7 )
button15.grid(row=1,column=2)
button16 = Button(downFrame, text='/',command=lambda: addExpression('/'),width=7 )
button16.grid(row=0,column=0)
button17 = Button(downFrame, text='=',command=equalpress,width=7 )
button17.grid(row=0,column=1)
button18= Button(downFrame, text='CLR',command=clear,width=7 )
button18.grid(row=0,column=2)
root.mainloop()