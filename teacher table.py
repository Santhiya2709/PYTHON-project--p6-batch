import sqlite3
from tkinter import *
import tkinter.ttk as ttk
from tkinter.ttk import Treeview
from tkinter import messagebox

def Database():
    con = sqlite3.connect("System.db")
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS teacher(id Integer Primary Key, name text, phone_number interger, classs integer, section text, maths integer, english integer, science integer)")
    con.commit()
    con.close()
root = Tk()
root.title("STUDENT DATABASE MANAGEMENT SYSTEM")
root.geometry("1300x768+0+0")
root.config(bg="#2c3e50")
root.state("zoomed")
global ids,name,phone_number,classs,section,fees_details
id = StringVar()
name=StringVar()
phone_number = StringVar()
classs = StringVar()
section = StringVar()
maths = StringVar()
english = StringVar()
science = StringVar()
#-------------------slider--------------
sliderlbl = Label(root, text="WELCOME TO STUDENT MANAGEMENT SYSTEM", font=("times new roman", 20, "bold"), bg="aquamarine2")
sliderlbl.place(x=300,y=300)
#------------------entry frame--------------

entry_frame = Frame(root, bg="#535c68")
entry_frame.pack(side=TOP, fill=X)
title = Label(entry_frame, text="STUDENT MANAGEMENT SYSTEM", font=("times new roman","20","bold"), bg="aquamarine2", fg="blue")
title.grid(row=0, columnspan=2, padx=10, pady=20,sticky="w")

lblid=Label(entry_frame, text="ID",font=("times new roman","15","bold"), width=10)
lblid.grid(row=1, column=0, padx=10, pady=20,sticky="w")
txtid = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=id , width=10)
txtid.grid(row=1, column=1, padx=10, pady=20,sticky="w")


lblname=Label(entry_frame, text="NAME",font=("times new roman","15","bold"), width=10)
lblname.grid(row=1, column=2, padx=10, pady=20,sticky="w")
txtname = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=name, width=30)
txtname.grid(row=1, column=3, padx=10, pady=20,sticky="w")

lblphone=Label(entry_frame, text="PHONE",font=("times new roman","15","bold"), width=10)
lblphone.grid(row=1, column=4, padx=10, pady=20,sticky="w")
txtphone = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=phone_number, width=30)
txtphone.grid(row=1, column=5, padx=10, pady=20,sticky="w")

lblclass=Label(entry_frame, text="CLASS",font=("times new roman","15","bold"), width=10)
lblclass.grid(row=2, column=0,padx=10,pady=20,sticky="w")
txtclass = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=classs, width=30)
txtclass.grid(row=2, column=1,padx=10,pady=20,sticky="w")

lblsection=Label(entry_frame, text="SECTION",font=("times new roman","15","bold"), width=10)
lblsection.grid(row=2, column=2,padx=10,pady=20,sticky="w")
txtsection = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=section, width=30)
txtsection.grid(row=2, column=3,padx=10,pady=20,sticky="w")

lblfees_details =Label(entry_frame, text="MATHS",font=("times new roman","15","bold"), width=10)
lblfees_details.grid(row=2, column=4,padx=10,pady=20,sticky="w")
txtfees_details = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=maths, width=30)
txtfees_details.grid(row=2, column=5,padx=10,pady=20,sticky="w")

lblfees_details =Label(entry_frame, text="ENGLISH",font=("times new roman","15","bold"), width=10)
lblfees_details.grid(row=4, column=0,padx=10,pady=20,sticky="w")
txtfees_details = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=english, width=30)
txtfees_details.grid(row=4, column=1,padx=10,pady=20,sticky="w")

lblfees_details =Label(entry_frame, text="SCIENCE",font=("times new roman","15","bold"), width=10)
lblfees_details.grid(row=4, column=2,padx=10,pady=20,sticky="w")
txtfees_details = Entry(entry_frame, font=("times new roman","15","bold"), textvariable=science, width=30)
txtfees_details.grid(row=4, column=3,padx=10,pady=20,sticky="w")

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    #print(row)
    id.set(row[0])
    name.set(row[1])
    phone_number.set(row[2])
    classs.set(row[3])
    section.set(row[4])
    maths.set(row[5])
    english.set(row[6])
    science.set(row[7])

def DisplayAll():
    con = sqlite3.connect("System.db")
    cursor = con.cursor()
    cursor.execute("SELECT * FROM teacher")
    res = cursor.fetchall()
    tv.delete(*tv.get_children())
    for row in res:
        tv.insert("",END,values= row)
def add():
    con = sqlite3.connect("System.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO teacher VALUES ('%s','%s','%s','%s','%s','%s','%s','%s')"% (id.get(),name.get(), phone_number.get(), classs.get(), section.get(), maths.get(), english.get(), science.get()))
    con.commit()
    messagebox.showinfo("Notification", "Data Added Successfully")
    DisplayAll()
def update():
    con = sqlite3.connect("System.db")
    cursor = con.cursor()
    cursor.execute("UPDATE teacher SET maths='%s', english='%s', science='%s' WHERE id='%s';" % (maths.get(), english.get(), science.get(), id.get()))
    con.commit()
    messagebox.showinfo("Notification", "Data Updated Successfully")
def delete():
    con = sqlite3.connect("System.db")
    cursor = con.cursor()
    cursor.execute("DELETE FROM teacher WHERE id='%s';" %  (id.get()))
    con.commit()
    messagebox.showinfo("Notification", "Deleted")


btnframe = Frame(entry_frame, bg="#535c68")
btnframe.grid(row=5, column=0, columnspan=4, padx=10,pady=20,sticky="w")
btnadd = Button(btnframe, command=add, text="ADD", width=15,
                font=("times new roman","15","bold"), fg="white",bg="#16a085",bd=0).grid(row=0, column=0, padx=10)
btnupdate = Button(btnframe, command=update, text="UPDATE", width=15,
                font=("times new roman","15","bold"), fg="white",bg="#2980b9",bd=0).grid(row=0, column=1, padx=10)
btndelete = Button(btnframe, command=delete, text="DELETE", width=15,
                font=("times new roman","15","bold"), fg="white",bg="#c0392b",bd=0).grid(row=0, column=2, padx=10)
btnview = Button(btnframe, command=DisplayAll, text="VIEW", width=15,
                font=("times new roman","15","bold"), fg="white",bg="#f39c12",bd=0).grid(row=0, column=3, padx=10)

#----------table frame--------------
tree_frame =Frame(root, bg="#ecf0f1")
tree_frame.place(x=0,y=380,width=1366, height=600)
style=ttk.Style()
style.configure("mystyle.Treeview", font=("times new roman","20","bold"),rowheight=68)
style.configure("mystyle.Treeview.Headings", font=("times new roman","20","bold"))
tv = Treeview(tree_frame, columns=(1,2,3,4,5,6,7,8))
tv.heading("1", text="ID")
tv.column("1", width=25)
tv.heading("2", text="NAME")
tv.heading("3", text="PHONE")
tv.heading("4", text="CLASS")
tv.column("4", width=50)
tv.heading("5", text="SECTION")
tv.column("5", width=50)
tv.heading("6", text="MATHS")
tv.heading("7", text="ENGLISH")
tv.heading("8", text="SCIENCE")

tv['show']='headings'
tv.bind("<ButtonRelease-1>", getData)
tv.pack(fill=X)

root.mainloop()



