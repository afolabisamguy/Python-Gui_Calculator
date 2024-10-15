import math
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()

root.geometry("500x500")
root.title("Calculator")

myentry = tk.Entry(root, width=43, font=("Helvetica", 18))
myentry.pack(padx=100, pady=10)


def onclosing():
    if messagebox.askyesno('Quit', 'Do you really want to quit?'):
        root.destroy()


def arithmetic(arth):
    global fnum
    fnum = myentry.get()
    myentry.delete(0, tk.END)
    global arths
    arths = arth


current_value = 0
operation = ''


def percentage():
    global current_value, operation
    if operation == '':

        current_value = float(myentry.get()) / 100
    else:
        second_number = float(myentry.get())
        if operation == '+':
            current_value += (current_value * second_number / 100)
        elif operation == '-':
            current_value -= (current_value * second_number / 100)
        elif operation == '*':
            current_value *= (second_number / 100)
        elif operation == '/':
            if second_number != 0:
                current_value /= (second_number / 100)
            else:
                current_value = 'Error'

    # Update the display
    myentry.delete(0, tk.END)
    myentry.insert(tk.END, str(current_value))
    operation = ''
def specialButtons(symbol):
    snum = myentry.get()
    if symbol == "sq":
        snum = int(snum)
        myresult = snum * snum
        myentry.delete(0, tk.END)
        myentry.insert(tk.END, str(myresult))
    if symbol == "sroot":
        snum = int(snum)
        myresult = math.sqrt(snum)
        myresult = str(myresult)
        myentry.delete(0, tk.END)
        myentry.insert(tk.END, myresult)


def equals():
    global result
    second = myentry.get()
    myentry.delete(0, tk.END)
    if arths == 'addition':
        result = int(fnum) + int(second)
    elif arths == 'subtraction':
        result = int(fnum) - int(second)
    elif arths == 'multiplication':
        result = int(fnum) * int(second)
    elif arths == 'division':
        try:
            result = int(fnum) / int(second)
        except ZeroDivisionError:
            messagebox.showerror("Error", "Division by Zero is not allowed")
    myentry.insert(tk.END, str(result))


def button_click(number):
    num = myentry.get()
    myentry.delete(0, tk.END)
    myentry.insert(tk.END, str(num) + str(number))


def clear():
    myentry.delete(0, tk.END)


button = tk.Button(root, text="AC", font=('Arial', 20), command=clear)
button.pack(padx=10, pady=10)

buttonframe = tk.Frame(root)
buttonframe.columnconfigure(0, weight=1)
buttonframe.columnconfigure(1, weight=1)
buttonframe.columnconfigure(2, weight=1)

btn1 = tk.Button(buttonframe, text='1', font=('Arial', 20), command=lambda: button_click(1))
btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

btn2 = tk.Button(buttonframe, text='2', font=('Arial', 20), command=lambda: button_click(2))
btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

btn3 = tk.Button(buttonframe, text='3', font=('Arial', 20), command=lambda: button_click(3))
btn3.grid(row=0, column=2, sticky=tk.W + tk.E)

btn4 = tk.Button(buttonframe, text='4', font=('Arial', 20), command=lambda: button_click(4))
btn4.grid(row=1, column=0, sticky=tk.W + tk.E)

btn5 = tk.Button(buttonframe, text='5', font=('Arial', 20), command=lambda: button_click(5))
btn5.grid(row=1, column=1, sticky=tk.W + tk.E)

btn6 = tk.Button(buttonframe, text='6', font=('Arial', 20), command=lambda: button_click(6))
btn6.grid(row=1, column=2, sticky=tk.W + tk.E)

btn7 = tk.Button(buttonframe, text='7', font=('Arial', 20), command=lambda: button_click(7))
btn7.grid(row=2, column=0, sticky=tk.W + tk.E)

btn8 = tk.Button(buttonframe, text='8', font=('Arial', 20), command=lambda: button_click(8))
btn8.grid(row=2, column=1, sticky=tk.W + tk.E)

btn9 = tk.Button(buttonframe, text='9', font=('Arial', 20), command=lambda: button_click(9))
btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

btn0 = tk.Button(buttonframe, text='0', font=('Arial', 20), command=lambda: button_click(0))
btn0.grid(row=3, column=0, sticky=tk.W + tk.E)

btnPercentage = tk.Button(buttonframe, text='%', font=('Arial', 20), command=lambda: percentage())
btnPercentage.grid(row=3, column=1, sticky=tk.W + tk.E)

btnSquare = tk.Button(buttonframe, text='x²', font=('Arial', 20), command=lambda: specialButtons("sq"))
btnSquare.grid(row=3, column=2, sticky=tk.W + tk.E)

btnSquareroot = tk.Button(buttonframe, text=' ²√x', font=('Arial', 20), command=lambda: specialButtons("sroot"))
btnSquareroot.grid(row=4, column=0, sticky=tk.W + tk.E)

btnplus = tk.Button(buttonframe, text='+', font=('Arial', 20), command=lambda: arithmetic('addition'))
btnplus.grid(row=4, column=1, sticky=tk.W + tk.E)

btnminus = tk.Button(buttonframe, text='-', font=('Arial', 20), command=lambda: arithmetic('subtraction'))
btnminus.grid(row=4, column=2, sticky=tk.W + tk.E)

btndivide = tk.Button(buttonframe, text='/', font=('Arial', 20), command=lambda: arithmetic('division'))
btndivide.grid(row=5, column=0, sticky=tk.W + tk.E)

btnmultiply = tk.Button(buttonframe, text='*', font=('Arial', 20), command=lambda: arithmetic('multiplication'))
btnmultiply.grid(row=5, column=1, sticky=tk.W + tk.E)

btnequals = tk.Button(buttonframe, text='=', font=('Arial', 20), command=lambda: equals())
btnequals.grid(row=5, column=2, sticky=tk.W + tk.E)

buttonframe.pack(fill='x')

# anotherbtn = tk.Button(root, text='TESt')
# anotherbtn.place(x=50, y=200, height=100, width=100)

root.protocol('WM_DELETE_WINDOW', onclosing)
root.mainloop()
