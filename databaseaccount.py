import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('accounts.db')
cursor = conn.cursor()

table_name = "accounts"
id = "id"
username = "username"
password = "password"

def display():
    cursor = conn.execute("SELECT * FROM " + table_name + " ;")
    return cursor

def insert(_id,_username, _password):
    try:
        data= (_id,_username,_password)
        query = "INSERT INTO accounts VALUES(?,?,?)"
        conn.execute(query,data)    
        conn.commit()
        return True 
    except sqlite3.Error:
        messagebox.showerror(title="ERROR", message="Account already exists!")
