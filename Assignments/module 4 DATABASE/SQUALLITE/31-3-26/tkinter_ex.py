import tkinter 
from tkinter import messagebox

tk = tkinter.Tk()
tk.title("CALCULATOR")
tk.geometry('400x300')
tk.config(bg='lightyellow')

for i in range(5):
    tk.grid_rowconfigure(i,weight=1)
for j in range(3):
    tk.grid_columnconfigure(j,weight=1)    

tkinter.Label(text="Enter Number1:",bg='lightyellow').grid(row=1,column=0)
tkinter.Label(text="Enter Number2:",bg='lightyellow').grid(row=2,column=0)

textbox1 = tkinter.Entry(tk)
textbox1.grid(row=1,column=1)

textbox2 = tkinter.Entry(tk)
textbox2.grid(row=2,column=1)

def get_number():
    try:
        num1 = float(textbox1.get)
        num2 = float(textbox2.get)
        return num1,num2
    except:
        messagebox.showerror("Error","Please enter a valid number")
        return None,None

def addition():
    total = int(textbox1.get()) + int(textbox2.get())
    messagebox.showinfo("Result",total)


def subtraction():
    total = int(textbox1.get()) - int(textbox2.get())
    messagebox.showinfo("Result",total)


def multiply():
    total = int(textbox1.get()) * int(textbox2.get())
    messagebox.showinfo("Result",total)


def divide():
    total = int(textbox1.get()) / int(textbox2.get())
    messagebox.showinfo("Result",total)

tkinter.Button(tk,text='Addition',command=addition).grid(row=3,column=0)
tkinter.Button(tk,text='Subtraction',command=subtraction).grid(row=3,column=1)
tkinter.Button(tk,text='Multiply',command=multiply).grid(row=3,column=2)
tkinter.Button(tk,text='Divide',command=divide).grid(row=4,column=1)




tkinter.mainloop()