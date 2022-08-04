from email import message
from importlib.resources import contents
from select import select
from tkinter import*
from tkinter import ttk
from tkinter import filedialog 
import tkinter.messagebox
import studentDB_backend
import csv,os


#Frontend
class Student:
    def __init__(self, root):
        self.root = root
        blank_space= " "
        self.root.title(200 * blank_space + "Pythonist Student Management System")
        self.root.geometry("1625x600")
#VARIABLES--------------------
        StdId = StringVar()
        Firstname= StringVar()
        Surname= StringVar()
        DoB= StringVar()
        Age= StringVar()
        Gender= StringVar()
        Address= StringVar()
        Mobile= StringVar()
#VARIABLES--------------------

#FUNCTIONS--------------------
        def iExit():
            iExit = tkinter.messagebox.askyesno("Pythonist Student Management System","Do you really want to exit the program?")
            if iExit > 0:
                root.destroy()
                return      
        def iReset():
            self.txtStdID.delete(0, END)
            self.txtFirstname.delete(0, END)
            self.txtSurname.delete(0, END)
            self.txtDoB.delete(0, END)
            self.txtAge.delete(0, END)
            self.cboGender.delete(0, END)
            self.txtAddress.delete(0, END)
            self.txtMobile.delete(0, END)
        
        def iDisplayData():
                result = studentDB_backend.viewStdRecord()
                if len(result) != 0:
                        self.studentlist.delete(*self.studentlist.get_children())
                        for row in result:
                                self.studentlist.insert('',END,values=row)            
                
        def iAddData():
                if(StdId.get() == "" or Firstname.get() == "" or Surname.get() == "" or DoB.get() == "" or Age.get() == "" or Gender.get() == "" or Address.get() == "" or Mobile.get() == ""):
                        tkinter.messagebox.showerror(title="ERROR", message= "Complete all fields!")
                else:
                        studentDB_backend.addStdRecord(StdId.get(),Firstname.get(),Surname.get(),DoB.get(),Age.get(),Gender.get(),Address.get(),Mobile.get()) 
                        iDisplayData()
        def iDeleteData():
                if(StdId.get() == "" or Firstname.get() == "" or Surname.get() == "" or DoB.get() == "" or Age.get() == "" or Gender.get() == "" or Address.get() == "" or Mobile.get() == ""):
                        tkinter.messagebox.showerror(title="ERROR", message= "Complete all fields!")
                else:
                        # x = self.studentlist.selection()[0]
                        # self.studentlist.delete(x)          
                        studentDB_backend.deleteStdRecord(StdId.get()) 
                        iDisplayData()  

        def select_record(event):
                self.txtStdID.delete(0, END)
                self.txtFirstname.delete(0, END)
                self.txtSurname.delete(0, END)
                self.txtDoB.delete(0, END)
                self.txtAge.delete(0, END)
                self.cboGender.delete(0, END)
                self.txtAddress.delete(0, END)
                self.txtMobile.delete(0, END)

                selected = self.studentlist.focus()
                values = self.studentlist.item(selected, 'values')
                self.txtStdID.insert(0, values[0])
                self.txtFirstname.insert(0,values[1])
                self.txtSurname.insert(0,values[2]) 
                self.txtDoB.insert(0,values[3])
                self.txtAge.insert(0,values[4])
                self.cboGender.insert(0,values[5])
                self.txtAddress.insert(0,values[6])
                self.txtMobile.insert(0,values[7]) 

        def iUpdateData():
                        selected = self.studentlist.focus()
                        values = self.studentlist.item(selected, 'values')
                        if(StdId.get() == "" or Firstname.get() == "" or Surname.get() == "" or DoB.get() == "" or Age.get() == "" or Gender.get() == "" or Address.get() == "" or Mobile.get() == ""):
                                tkinter.messagebox.showerror(title="ERROR", message= "Complete all fields!")
                        else:        
                                studentDB_backend.updateStdRecord(values[0],
                                                                        Firstname.get(),
                                                                        Surname.get(),
                                                                        DoB.get(),
                                                                        Age.get(),
                                                                        Gender.get(),
                                                                        Address.get(),
                                                                        Mobile.get(),
                                                                        StdId.get())      
                                # self.studentlist.item(selected, text='', values=(self.txtStdID.get(),
                                #                                                 self.txtFirstname.get(),
                                #                                                 self.txtSurname.get(),
                                #                                                 self.txtDoB.get(),
                                #                                                 self.txtAge.get(),
                                #                                                 self.cboGender.get(),
                                #                                                 self.txtAddress.get(),
                                #                                                 self.txtMobile.get())) 
                                self.txtStdID.delete(0, END)
                                self.txtFirstname.delete(0, END)
                                self.txtSurname.delete(0, END)
                                self.txtDoB.delete(0, END)
                                self.txtAge.delete(0, END)
                                self.cboGender.delete(0, END)
                                self.txtAddress.delete(0, END)
                                self.txtMobile.delete(0, END)
                                iDisplayData()
        def iCSV():
                header = ['Student ID','First Name','Last Name','Birthday','Age','Gender','City','Mobile']
                extension = [('csv', '*.csv')]
                fileLocation = filedialog.asksaveasfilename(initialdir=os.getcwd(),defaultextension=extension, initialfile= 'Studentlist', title="Save CSV", filetypes=(("CSV File", "*.csv"),("All Files", "*.")))
                with open(fileLocation, mode= "w", encoding= 'utf-8') as csvFile:
                        csv_writer = csv.writer(csvFile, delimiter=',')
                        csv_writer.writerow(header)
                        result = studentDB_backend.viewStdRecord()
                        if len(result) < 1:
                                tkinter.messagebox.showerror(title="ERROR", message="No data available!")
                        else:
                                for i in self.studentlist.get_children():
                                        data = self.studentlist.item(i)['values']                                       
                                        csv_writer.writerow(data)

#FRAMES---------------------------------------------------------------------------------------------
        MainFrame = Frame(self.root, bd=10, width =1350,height = 700, relief= RIDGE, bg='#ffa0bf')
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=5, width =1340,height = 50, relief= RIDGE)
        TopFrame1.grid(row = 2, column = 0, pady=8)
        TitleFrame = Frame(MainFrame, bd=7, width =1340,height =100, relief= GROOVE, bg='#ffa0bf')
        TitleFrame.grid(row = 0, column = 0)
        TopFrame3 = Frame(MainFrame, bd=5, width =1340,height = 500, relief= GROOVE,bg='#ffa0bf')
        TopFrame3.grid(row = 3,column = 0)

        LeftFrame = Frame(TopFrame3, bd=5, width =1340,height = 400,padx=2, relief= RIDGE, bg='#ffa0bf')
        LeftFrame.pack(side=LEFT)
        LeftFrame1 = Frame(LeftFrame, bd=5, width =600,height = 180,padx=2, pady=4, relief= GROOVE,bg='#ffa0bf')
        LeftFrame1.pack(side=TOP, padx=0,pady=4)
        
        RightFrame1 = Frame(TopFrame3, bd=5, width =320,height = 400,padx=2, relief= RIDGE, bg='#ffa0bf')
        RightFrame1.pack(side=RIGHT)
        RightFrame1a = Frame(RightFrame1, bd=5, width =310,height = 200,padx=2, pady=2, relief= RIDGE,)
        RightFrame1a.pack(side=TOP)
#FRAMES----------------------------------------------------------------------------------------------


#TITLE-----------------------------------------------------------------------------------------------

        self.lblTitle = Label(TitleFrame, font=('arial', 38, 'bold'),text="Pythonists Student Management System",bd=7,bg='#ffa0bf', fg='white')
        self.lblTitle.grid(row=0,column=0, padx=132)

#TITLE------------------------------------------------------------------------------------------------


#ENTRY
        #Student ID ENTRY-----------------------------------------------------------------------------------------------------------------
        self.lblStdID = Label(LeftFrame1, font=('arial', 12, 'bold'),text="STUDENT ID",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblStdID.grid(row=0,column=0, sticky = W, padx=5)
        self.txtStdID = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=StdId)
        self.txtStdID.grid(row=0,column=1)

        #FIRST NAME ENTRY-----------------------------------------------------------------------------------------------------------------
        self.lblFirstname = Label(LeftFrame1, font=('arial', 12, 'bold'),text="FIRST NAME",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblFirstname.grid(row=1,column=0, sticky = W, padx=5)
        self.txtFirstname = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=Firstname)
        self.txtFirstname.grid(row=1,column=1)
        
        #LAST NAME ENTRY------------------------------------------------------------------------------------------------------------------
        self.lblSurname = Label(LeftFrame1, font=('arial', 12, 'bold'),text="LAST NAME",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblSurname.grid(row=2,column=0, sticky = W, padx=5)
        self.txtSurname = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=Surname)
        self.txtSurname.grid(row=2,column=1)

        #BIRTHDAY ENTRY-------------------------------------------------------------------------------------------------------------------
        self.lblDoB = Label(LeftFrame1, font=('arial', 12, 'bold'),text="BIRTHDAY",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblDoB.grid(row=3,column=0, sticky = W, padx=5)
        self.txtDoB = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=DoB)
        self.txtDoB.grid(row=3,column=1)
        
        #AGE ENTRY-----------------------------------------------------------------------------------------------------------------------
        self.lblAge = Label(LeftFrame1, font=('arial', 12, 'bold'),text="AGE",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblAge.grid(row=4,column=0, sticky = W, padx=5)
        self.txtAge = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=Age)
        self.txtAge.grid(row=4,column=1)

        #GENDER COMBO BOX--------------------------------------------------------------------------------------------------------------
        self.lblGender = Label(LeftFrame1, font=('arial', 12, 'bold'),text="GENDER",fg='white',bg='#ffa0bf',bd=7,)
        self.lblGender.grid(row=5,column=0, sticky = W, padx=5)
        self.cboGender=ttk.Combobox(LeftFrame1,width=39, font=('arial',12,'bold'), state='readonly', textvariable=Gender)
        self.cboGender['values'] =('Male','Female')
        self.cboGender.current(0)
        self.cboGender.grid(row=5,column=1)

        #ADDRESS ENTRY------------------------------------------------------------------------------------------------------------------
        self.lblAddress = Label(LeftFrame1, font=('arial', 12, 'bold'),text="CITY",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblAddress.grid(row=6,column=0, sticky = W, padx=5)
        self.txtAddress = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=Address)
        self.txtAddress.grid(row=6,column=1)

        #MOBILE ENTRY------------------------------------------------------------------------------------------------------------------
        self.lblMobile = Label(LeftFrame1, font=('arial', 12, 'bold'),text="MOBILE",bg='#ffa0bf',fg='white',bd=7, anchor = 'w', justify = LEFT)
        self.lblMobile.grid(row=7,column=0, sticky = W, padx=5)
        self.txtMobile = Entry(LeftFrame1, font=('arial', 12, 'bold'),bd=5,width = 40, justify = 'left', textvariable=Mobile)
        self.txtMobile.grid(row=7,column=1)
#ENTRY

        

#TREEVIEW
        scroll_x = Scrollbar(RightFrame1a, orient = HORIZONTAL)
        scroll_y = Scrollbar(RightFrame1a, orient = VERTICAL)

        self.studentlist = ttk.Treeview(RightFrame1a, height=12, columns=("stdid","firstname","surname","birthday","age","gender","address","mobile"), xscrollcommand = scroll_x.set, \
        yscrollcommand= scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill = X)
        scroll_y.pack(side=RIGHT, fill = Y)

        self.studentlist.heading("stdid",text="Student ID")
        self.studentlist.heading("firstname",text="First Name")
        self.studentlist.heading("surname",text="Last Name")
        self.studentlist.heading("birthday",text="Birthday")
        self.studentlist.heading("age",text="Age")
        self.studentlist.heading("gender",text="Gender")
        self.studentlist.heading("address",text="City")
        self.studentlist.heading("mobile",text="Mobile")

        self.studentlist['show'] ='headings'

        self.studentlist.column("stdid",width=70)
        self.studentlist.column("firstname",width=100)
        self.studentlist.column("surname",width=100)
        self.studentlist.column("birthday",width=100)
        self.studentlist.column("age",width=70)
        self.studentlist.column("gender",width=70)
        self.studentlist.column("address",width=120)
        self.studentlist.column("mobile",width=120)

        self.studentlist.pack(fill=BOTH, expand=1)   
        iDisplayData()
        self.studentlist.bind("<ButtonRelease-1>",select_record)
#TREEVIEW

#BUTTONS

#--------------------------------------ADD-----------------------------------------------------#
        self.btnAddNew =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="ADD NEW",
        width=12, height=2,padx=24, command=iAddData).grid(row=0,column=0,padx=1)

#--------------------------------------DISPLAY-----------------------------------------------------#
        self.btnDisplay =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="UPDATE",
        width=12, height=2,padx=24, command = iUpdateData).grid(row=0,column=1,padx=1)

#--------------------------------------DELETE-----------------------------------------------------#
        self.btnDelete =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="DELETE",
        width=12, height=2,padx=24, command = iDeleteData).grid(row=0,column=2,padx=1)

#--------------------------------------RESET-----------------------------------------------------#
        self.btnReset =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="RESET",
        width=12, height=2,padx=24,command=iReset).grid(row=0,column=3,padx=1)

#--------------------------------------EXIT-----------------------------------------------------#
        self.btnExit =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="CSV",
        width=12, height=2,padx=24, command=iCSV).grid(row=0,column=4,padx=1)

        self.btnExit =Button(TopFrame1, pady =1,bd=4,bg='black',fg='white',font=('arial', 20, 'bold'),text="EXIT",
        width=12, height=2,padx=24, command=iExit).grid(row=0,column=5,padx=1)
        

#BUTTONS
if __name__ =='__main__':
        root = Tk()
        frame_width = 1625
        frame_height = 550
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        x = (screen_width / 2) - (frame_width / 2)
        y = (screen_height / 2) - (frame_height / 2)
        root.geometry(f'{frame_width}x{frame_height}+{int(x)}+{int(y)}')
        root.iconbitmap('icon.ico')
        application = Student(root)
        root.mainloop()

