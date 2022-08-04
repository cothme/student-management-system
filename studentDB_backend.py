import sqlite3
from tkinter import messagebox

#Backend
def studentData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID, Firstname text, Surname text,\
                DoB text, Age text, Gender text, Address text, Mobile text)")
    con.commit
    con.close

def addStdRecord(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):  
    try:       
        int(StdID)
        int(Age)
        con = sqlite3.connect("student.db")
        cur = con.cursor() 
        data = (StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile)
        query = "INSERT INTO student VALUES (?,?,?,?,?,?,?,?)" 
        cur.execute(query,data)
        messagebox.showinfo(title = "SUCCESS", message = "Student added successfully!")
        con.commit()
        con.close()
        return True  
    except sqlite3.IntegrityError:
        messagebox.showerror(title = "ERROR", message = "Rows must be unique!")
    except ValueError:
        messagebox.showerror(title = "ERROR", message = "ID and Age must be numbers!")
    
    
def viewStdRecord(): 
    con = sqlite3.connect("student.db") 
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteStdRecord(id): 
    con = sqlite3.connect("student.db") 
    cur = con.cursor()
    query = "DELETE FROM student WHERE StdID = " + id
    cur.execute(query)
    messagebox.showinfo(title="Success", message= "Student deleted successfully")
    con.commit()
    con.close()

def updateStdRecord(StdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, newStdID):
    try:
        int(StdID)
        int(Age)
        con = sqlite3.connect("student.db")
        cur = con.cursor()
        query = ("UPDATE student SET StdID = ?, Firstname = ?, Surname = ?, DoB = ?, Age = ?, Gender = ?, Address = ?, Mobile = ? WHERE StdID = ?")
        data = (newStdID, Firstname, Surname, DoB, Age, Gender, Address, Mobile, StdID)
        cur.execute(query,data)
        messagebox.showinfo(title="Success", message="Student updated successfully!")
        con.commit()
        con.close()
        return True
    except sqlite3.IntegrityError:
        messagebox.showerror(title = "ERROR", message = "Student already exists!")
    except sqlite3.OperationalError:
        messagebox.showerror(title = "ERROR", message = "Something Wrong Happened!")
