import tkinter
from tkinter import ttk,messagebox

tk=tkinter.Tk()
tk.geometry("400x500")
tk.config(bg='lightblue')
tk.title("MyApp")


"""l1=tkinter.Label(text="Firstname")
l1.pack()
l2=tkinter.Label(text="Lastname")
l2.pack()"""

"""l1=tkinter.Label(text="Firstname")
l1.grid(row=0,column=0)
l2=tkinter.Label(text="Lastname")
l2.grid(row=1,column=0)"""

"""l1=tkinter.Label(text="Firstname")
l1.place(x=0,y=0)
l2=tkinter.Label(text="Lastname")
l2.place(x=0,y=40)"""

# ------------------------------------ #
l1=tkinter.Label(text="Firstname",bg='lightblue',fg='red',font='Courier 15 bold')
l1.grid(row=0,column=0,sticky='w')
l2=tkinter.Label(text="Lastname",bg='lightblue',fg='red',font='Courier 15 bold')
l2.grid(row=1,column=0,sticky='w')

t1=tkinter.Entry()
t1.grid(row=0,column=1)
t2=tkinter.Entry()
t2.grid(row=1,column=1)

m=tkinter.Radiobutton(value=0,text="Male",bg='lightblue',fg='red',font='Courier 15 bold')
m.grid(row=2,column=0,sticky='w')
f=tkinter.Radiobutton(value=1,text="Female",bg='lightblue',fg='red',font='Courier 15 bold')
f.grid(row=2,column=1,sticky='w')

ch1=tkinter.Checkbutton(text="Gujrati",bg='lightblue',fg='red',font='Courier 15 bold')
ch1.grid(row=3,column=0,sticky='w')

ch2=tkinter.Checkbutton(text="Hindi",bg='lightblue',fg='red',font='Courier 15 bold')
ch2.grid(row=4,column=0,sticky='w')

ch3=tkinter.Checkbutton(text="English",bg='lightblue',fg='red',font='Courier 15 bold')
ch3.grid(row=5,column=0,sticky='w')

city=['Rajkot','Ahmedabad','Baroda','Surat','Jamnagar']

dd=ttk.Combobox(values=city)
dd.grid(row=6,column=0,sticky='w')

def btnclick():
    #print("Button clicked!")
    #messagebox.showerror("Error","Something went wrong...")
    #messagebox.showinfo("Success","Form submitted successfully!")
    #messagebox.showwarning("Warning","Your disk is full!")
    print("Firstname:",t1.get())
    print("Lastname:",t2.get())
    

btn=tkinter.Button(text="Submit",bg='lightblue',fg='red',font='Courier 15 bold',command=btnclick)
btn.place(x=160,y=250)

tk.mainloop()