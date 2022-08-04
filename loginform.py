import tkinter as tk
from tkinter import Toplevel, messagebox
import databaseaccount as db
from tkinter import *
from tkinter import ttk
import student_DB_frontend

#centering the window
window = tk.Tk()
window.title('Student Management System')
frame_width = 400
frame_height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width / 2) - (frame_width / 2)
y = (screen_height / 2) - (frame_height / 2)
window.geometry(f'{frame_width}x{frame_height}+{int(x)}+{int(y)}')
window.iconbitmap('icon.ico')

def showMain():
    student_DB_frontend.Main = Toplevel()
    window.withdraw()   

def login():
    if not IDEntry.get() or not UserNameEntry.get() or not Password.get():
        messagebox.showinfo(title = "Missing fields", message= "Please complete all fields")
    else:  
       data = db.display()
       for id,username,password in data:
            if IDEntry.get() in str(id) and UserNameEntry.get() in username and Password.get() in password:          
                messagebox.showinfo(title= "Success", message= "Login Success")
                showMain()
                break
            else:
                messagebox.showinfo(title= "Error", message= "Invalid username or password or ID!")
                break
def register():
    if not IDEntry.get() or not UserNameEntry.get() or not Password.get():
        messagebox.showinfo(title = "Missing fields", message= "Please complete all fields")
        isIDValid = False
    else:
        isIDValid = True
        id = IDEntry.get()
        username = UserNameEntry.get()
        password = Password.get() 
        try:
            int(IDEntry.get())
        except ValueError:
            messagebox.showerror(title="ERROR", message= "Please input numbers on ID only!")
            isIDValid = False
        if(isIDValid):
            db.insert(id, username, password)
  
#HEADING
heading = tk.Label(window, text='Login',font=("Helvetica 12",30))
heading.grid(row = 0, column = 0,padx = 150,pady=10)

# INFO
IdLabel = tk.Label(window, text="ID:",font=("Helvetica",15)).place(x = 30,y = 100)
IDEntry = tk.Entry(window, width= 10)
IDEntry.place(x = 145,y = 105)

UserNameLabel = tk.Label(window, text="Username:",font=("Helvetica",15)).place(x = 30,y = 150)
UserNameEntry = tk.Entry(window, width= 30)
UserNameEntry.place(x = 145,y = 155)

PasswordLabel = tk.Label(window, text="Password:",font=("Helvetica",15)).place(x = 30,y = 200)
Password = tk.Entry(window,show= "*",width= 30)
Password.place(x = 145,y = 205)

# BUTTONS
loginButton = tk.Button(window, text="LOGIN", height= 1, width= 10, command= login)
loginButton.place(x = 50,y = 300)

registerButton = tk.Button(window, text = "REGISTER", height = 1, width= 10, command= register)
registerButton.place(x = 250, y = 300)

window.mainloop()