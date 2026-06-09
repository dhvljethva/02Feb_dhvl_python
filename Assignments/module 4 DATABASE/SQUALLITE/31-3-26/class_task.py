import tkinter as tk
from tkinter import messagebox
import pymysql

def get_db_connection():
    return pymysql.connect(host='localhost',user='root',password='',database='tkinterr_app')

db = get_db_connection()
print("Database connected")

cr = db.cursor()

create_tbl = 'create table tkinterr_app (name varchar(20), email varchar(20),mobile varchar(20))'

try:
    cr.execute(create_tbl)
    db.commit()
    print("Table created")
except Exception as e:
    print(e)    

def submit_data():
    name = entry_name.get()
    email = entry_email.get()
    mobile = entry_mobile.get()

    if name == "" or email == "" or mobile == "":
        messagebox.showwarning("Error!","All field are required...")

    try:
        insert_tbl = "insert into tkinterr_app (name,email,mobile) values (%s,%s,%s)"
        values = (name,email,mobile) 

        cr.execute(insert_tbl)
        db.commit()

        messagebox.showinfo("Record inserted ")

        entry_name.delete(0,tk.END)
        entry_email.delete(0,tk.END)
        entry_mobile.delete(0,tk.END)

    except Exception as e:
        print(e)


root = tk.Tk()
root.title("Details")
root.geometry('400x300')

tk.Label(root,text='Name').pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack()

tk.Label(root,text='Email').pack(pady=5)
entry_email = tk.Entry(root)
entry_email.pack()

tk.Label(root,text='Mobile').pack(pady=5)
entry_mobile = tk.Entry(root)
entry_mobile.pack()

tk.Button(root, text="Submit",command= submit_data).pack(pady=20)

root.mainloop()
    
