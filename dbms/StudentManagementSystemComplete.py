from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
import tkinter as tk
import tkinter as tk
from tkinter import ttk
import pymysql

from dbms.example import accentbutton

# Function to connect to the database
def Connectdb():
    def submitdb():
        global con, mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            con = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()
        except:
            messagebox.showerror('Notifications', 'Data is incorrect please try again', parent=dbroot)
            connection_status.set("Not Connected")
            current_host.set("Host: N/A")
            current_user.set("User: N/A")
            return
        try:
            strr = 'CREATE DATABASE IF NOT EXISTS studentmanagementsystem1'
            mycursor.execute(strr)
            strr = 'USE studentmanagementsystem1'
            mycursor.execute(strr)
            strr = '''
               CREATE TABLE IF NOT EXISTS studentdata1(
                   studid VARCHAR(10) NOT NULL,
                   surname VARCHAR(20),
                   firstname VARCHAR(20),
                   birthdate CHAR(8),
                   sex CHAR(1),
                   PRIMARY KEY (studid)
               )
               '''
            mycursor.execute(strr)
            messagebox.showinfo('Notification', 'Database created and now you are connected to the database.',
                                parent=dbroot)
            connection_status.set("Connected")
            current_host.set(f"Host: {host}")
            current_user.set(f"User: {user}")

        except Exception as e:
            messagebox.showerror('Error', f"Error while creating table: {e}", parent=dbroot)
            return

        dbroot.destroy()

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.resizable(False, False)

    # Connectdb Labels
    hostlabel = ttk.Label(dbroot, text="Enter Host:")
    hostlabel.place(x=10, y=10)

    userlabel = ttk.Label(dbroot, text="Enter User:")
    userlabel.place(x=10, y=70)

    passwordlabel = ttk.Label(dbroot, text="Enter Password:")
    passwordlabel.place(x=10, y=130)

    # Connectdb Entries
    hostval = StringVar()
    hostval.set('localhost')
    userval = StringVar()
    userval.set('root')
    passwordval = StringVar()
    passwordval.set('Shuthefuckup69')

    hostentry = ttk.Entry(dbroot, textvariable=hostval)
    hostentry.place(x=250, y=10)

    userentry = ttk.Entry(dbroot, textvariable=userval)
    userentry.place(x=250, y=70)

    passwordentry = ttk.Entry(dbroot, textvariable=passwordval, show='*')
    passwordentry.place(x=250, y=130)

    # Connectdb Button
    submitbutton = ttk.Button(dbroot, text='Submit', command=submitdb)
    submitbutton.place(x=150, y=190)

    dbroot.mainloop()
# Function to add a new student
def addstudent():
    def submitadd():
        id = idval.get()
        surname = surnameval.get()
        firstname = firstnameval.get()
        birthdate = birthdateval.get()
        sex = sexval.get()
        if id == "" or surname == "" or firstname == "" or birthdate == "" or sex == "":
            messagebox.showerror('Error', 'All fields are required', parent=addroot)
            return

        try:
            # Insert data into the studentdata1 table
            strr = 'INSERT INTO studentdata1 (studid, surname, firstname, birthdate, sex) VALUES (%s, %s, %s, %s, %s)'
            mycursor.execute(strr, (id, surname, firstname, birthdate, sex))
            con.commit()
            messagebox.showinfo('Notification', 'Student data added successfully', parent=addroot)
            addroot.destroy()
        except Exception as e:
            messagebox.showerror('Error', f'Error while adding data: {e}', parent=addroot)
        strr = 'SELECT * FROM studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            studenttable.insert('', END, values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('480x380+100+100')
    addroot.title('Student Management System')
    addroot.resizable(False, False)

    # Add student labels
    idlabel = ttk.Label(addroot, text='Enter ID:')
    idlabel.place(x=10, y=10)

    surnamelabel = ttk.Label(addroot, text='Enter Surname:')
    surnamelabel.place(x=10, y=70)

    firstnamelabel = ttk.Label(addroot, text='Enter Firstname:')
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = ttk.Label(addroot, text='Enter Birthdate:')
    birthdatelabel.place(x=10, y=190)

    sexlabel = ttk.Label(addroot, text='Enter Sex:')
    sexlabel.place(x=10, y=250)

    # Student Entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    identry = ttk.Entry(addroot, textvariable=idval)
    identry.place(x=250, y=10)

    surnameentry = ttk.Entry(addroot, textvariable=surnameval)
    surnameentry.place(x=250, y=70)

    firstnameentry = ttk.Entry(addroot, textvariable=firstnameval)
    firstnameentry.place(x=250, y=130)

    birthdateentry = ttk.Entry(addroot, textvariable=birthdateval)
    birthdateentry.place(x=250, y=190)

    sexentry = ttk.Entry(addroot, textvariable=sexval)
    sexentry.place(x=250, y=250)

    # Submit button
    submitbtn = ttk.Button(addroot, text='Submit', command=submitadd)
    submitbtn.place(x=160, y=310)

    addroot.mainloop()
# Function to search for a student
def searchstudent():
    def search():
        id = idval.get()
        surname = surnameval.get()
        firstname = firstnameval.get()
        birthdate = birthdateval.get()
        sex = sexval.get()
        if (id != ''):
            strr = 'SELECT * FROM studentdata1 where studid=%s'
            mycursor.execute(strr, (id,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)
        elif (surname != ''):
            strr = 'SELECT * FROM studentdata1 where surname=%s'
            mycursor.execute(strr, (surname,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)
        elif (firstname != ''):
            strr = 'SELECT * FROM studentdata1 where firstname=%s'
            mycursor.execute(strr, (firstname,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)
        elif (birthdate != ''):
            strr = 'SELECT * FROM studentdata1 where birthdate=%s'
            mycursor.execute(strr, (birthdate,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)
        elif (sex != ''):
            strr = 'SELECT * FROM studentdata1 where sex=%s'
            mycursor.execute(strr, (sex,))
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)


    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('480x380+100+100')
    searchroot.title('Student Management System')
    searchroot.resizable(False, False)

    # Search student labels
    idlabel = ttk.Label(searchroot, text='Enter ID:')
    idlabel.place(x=10, y=10)

    surnamelabel = ttk.Label(searchroot, text='Enter Surname:')
    surnamelabel.place(x=10, y=70)

    firstnamelabel = ttk.Label(searchroot, text='Enter Firstname:')
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = ttk.Label(searchroot, text='Enter Birthdate:')
    birthdatelabel.place(x=10, y=190)

    sexlabel = ttk.Label(searchroot, text='Enter Sex:')
    sexlabel.place(x=10, y=250)

    # Student entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    identry = ttk.Entry(searchroot, textvariable=idval)
    identry.place(x=250, y=10)

    surnameentry = ttk.Entry(searchroot, textvariable=surnameval)
    surnameentry.place(x=250, y=70)

    firstnameentry = ttk.Entry(searchroot, textvariable=firstnameval)
    firstnameentry.place(x=250, y=130)

    birthdateentry = ttk.Entry(searchroot, textvariable=birthdateval)
    birthdateentry.place(x=250, y=190)

    sexentry = ttk.Entry(searchroot, textvariable=sexval)
    sexentry.place(x=250, y=250)

    # Search button
    submitbtn = ttk.Button(searchroot, text='Search', command=search)
    submitbtn.place(x=160, y=310)

    searchroot.mainloop()
# Delete Function
def deletestudent():
    try:
        # Get the selected item
        cc = studenttable.focus()
        if not cc:  # Check if focus returned an item
            messagebox.showerror('Error', 'No student selected for deletion')
            return

        content = studenttable.item(cc)
        pp = content.get('values', [])

        if not pp:
            messagebox.showerror('Error', 'No student selected for deletion')
            return

        studid_to_delete = pp[0]

        # Ensure the student ID is a valid string and within expected length
        if not isinstance(studid_to_delete, (str, int)):
            messagebox.showerror('Error', 'Invalid student ID format')
            return

        # Perform the deletion
        strr = 'DELETE FROM studentdata1 WHERE studid=%s'
        mycursor.execute(strr, (str(studid_to_delete),))
        con.commit()
        messagebox.showinfo('Notifications', f'StudentID {studid_to_delete} deleted successfully')

        # Refresh the table
        strr = 'SELECT * FROM studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            studenttable.insert('', END, values=vv)

    except IndexError:
        messagebox.showerror('Error', 'No student selected for deletion')
    except (pymysql.MySQLError, ValueError, TypeError) as e:
        messagebox.showerror('Error', f'Error while deleting data: {e}')
    except Exception as e:
        messagebox.showerror('Error', f'An unexpected error occurred: {e}')
#Update Function
def updatestudent():
    def update():
        old_id = original_id.get()
        new_id = idval.get()
        surname = surnameval.get()
        firstname = firstnameval.get()
        birthdate = birthdateval.get()
        sex = sexval.get()

        if not new_id:
            messagebox.showerror('Error', 'Student ID cannot be empty', parent=updateroot)
            return

        try:
            strr = 'UPDATE studentdata1 SET studid=%s, surname=%s, firstname=%s, birthdate=%s, sex=%s WHERE studid=%s'
            mycursor.execute(strr, (new_id, surname, firstname, birthdate, sex, old_id))
            con.commit()
            messagebox.showinfo('Notifications', 'StudentID {} updated successfully to {}'.format(old_id, new_id))

            # Refresh the table
            strr = 'SELECT * FROM studentdata1'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4]]
                studenttable.insert('', END, values=vv)
        except Exception as e:
            messagebox.showerror('Error', f'Error while updating data: {e}', parent=updateroot)

    def check_selection():
        cc = studenttable.focus()
        content = studenttable.item(cc)
        pp = content['values']
        if len(pp) == 0:
            update_button.configure(state=tk.DISABLED)
            idval.set('')
            surnameval.set('')
            firstnameval.set('')
            birthdateval.set('')
            sexval.set('')
            messagebox.showerror('Error', 'Please select a student to update.', parent=updateroot)
        else:
            update_button.configure(state=tk.NORMAL)
            original_id.set(pp[0])  # Store original student ID
            idval.set(pp[0])
            surnameval.set(pp[1])
            firstnameval.set(pp[2])
            birthdateval.set(pp[3])
            sexval.set(pp[4])

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('480x380+100+100')
    updateroot.title('Student Management System')
    updateroot.resizable(False, False)

    original_id = StringVar()  # Variable to store the original student ID

    # Update student labels
    ttk.Label(updateroot, text='Enter ID:').place(x=10, y=10)
    ttk.Label(updateroot, text='Enter Surname:').place(x=10, y=70)
    ttk.Label(updateroot, text='Enter Firstname:').place(x=10, y=130)
    ttk.Label(updateroot, text='Enter Birthdate:').place(x=10, y=190)
    ttk.Label(updateroot, text='Enter Sex:').place(x=10, y=250)

    # Student entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    ttk.Entry(updateroot, textvariable=idval).place(x=250, y=10)
    ttk.Entry(updateroot, textvariable=surnameval).place(x=250, y=70)
    ttk.Entry(updateroot, textvariable=firstnameval).place(x=250, y=130)
    ttk.Entry(updateroot, textvariable=birthdateval).place(x=250, y=190)
    ttk.Entry(updateroot, textvariable=sexval).place(x=250, y=250)

    # Update button
    update_button = ttk.Button(updateroot, text='Update', command=update)
    update_button.place(x=160, y=310)

    # Check if a student is selected before enabling the 'Update' button
    check_selection()

    updateroot.mainloop()
#Show the tables
def showstudent():
    try:
        strr = 'SELECT * FROM studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        if not datas:
            messagebox.showinfo('Information', 'No student data available in the database.')
            return
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            studenttable.insert('', END, values=vv)
    except Exception as e:
        messagebox.showerror('Error', f'Error while fetching data: {e}')
def exportstudent():
    print('Student export')
def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()



# Initialize Tkinter window
root = tk.Tk()
root.title('Student Management System')
root.geometry('1150x700+300+10')
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.tk.call("source", "forest-dark.tcl")
ttk.Style().theme_use('forest-dark')

# Variables for the slider
ss = 'Student Management System '
count = 0
text = ''
connection_status = StringVar()
connection_status.set("Not Connected")
current_host = StringVar()
current_host.set("Host: N/A")
current_user = StringVar()
current_user.set("User: N/A")


#main menu frame
DataEntryFrame = Frame(root, bg='gray')
DataEntryFrame.place(x=10, y=80, width=300, height=550)

frontlabel = Label(DataEntryFrame, text='Main Menu', font=("Arial", 16, "bold"))
frontlabel.pack(side=TOP, expand=TRUE, fill=BOTH)

addbtn = ttk.Button(DataEntryFrame, text='1. Add Student',  style='Accent.TButton',command=addstudent)
addbtn.pack(side=TOP, expand=TRUE, fill=BOTH)

searchbtn = ttk.Button(DataEntryFrame, text='2. Search Student', style='Accent.TButton',command=searchstudent)
searchbtn.pack(side=TOP, expand=TRUE, fill=BOTH)

deletebtn = ttk.Button(DataEntryFrame, text='3. Delete Student',style='Accent.TButton', command=deletestudent)
deletebtn.pack(side=TOP, expand=TRUE, fill=BOTH)

updatebtn = ttk.Button(DataEntryFrame, text='4. Update Student', style='Accent.TButton',command=updatestudent)
updatebtn.pack(side=TOP, expand=TRUE, fill=BOTH)

showallbtn = ttk.Button(DataEntryFrame, text='5. Show All',style='Accent.TButton', command=showstudent)
showallbtn.pack(side=TOP, expand=TRUE, fill=BOTH)

exportbtn = ttk.Button(DataEntryFrame, text='6. Export Data',style='Accent.TButton', command=exportstudent)
exportbtn.pack(side=TOP, expand=TRUE, fill=BOTH)

exitbtn = ttk.Button(DataEntryFrame, text='7. Exit', style='Accent.TButton',command=exitstudent)
exitbtn.pack(side=TOP, expand=TRUE, fill = BOTH)

# Show Data Frame
ShowDataFrame = Frame(root, bg='white')
ShowDataFrame.place(x=350, y=80, width=800, height=550)

# Scrollbars

scroll_x = ttk.Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = ttk.Scrollbar(ShowDataFrame, orient=VERTICAL)


studenttable = Treeview(ShowDataFrame, columns=('Student ID', 'Surname', 'First Name', 'Birthdate', 'Sex'),
                        yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)

scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.config(command=studenttable.xview)
scroll_y.config(command=studenttable.yview)

studenttable.heading('Student ID', text='Student ID')
studenttable.heading('Surname', text='Surname')
studenttable.heading('First Name', text='First Name')
studenttable.heading('Birthdate', text='Birthdate')
studenttable.heading('Sex', text='Sex')

studenttable.column('Student ID', width=100)
studenttable.column('Surname', width=100)
studenttable.column('First Name', width=100)
studenttable.column('Birthdate', width=100)
studenttable.column('Sex', width=100)

studenttable['show'] = 'headings'
studenttable.pack(fill=BOTH, expand=1)

# Slider label
SliderLabel = ttk.Label(root, text=ss, font=('arial', 30, 'bold'))
SliderLabel.place(x=290, y=0)

# Connect to database button
connectbutton = ttk.Button(root, text='Connect to Database', style = 'Accent.TButton', command=Connectdb)
connectbutton.place(x=980 , y=20)

StatusFrame = Frame(root, bg='white', relief=GROOVE)
StatusFrame.place(x=10, y=5, width=180, height=70)

if(connection_status == "Not Connected"):
    status_label = ttk.Label(StatusFrame, textvariable=connection_status, font=("Arial", 12,))
    status_label.pack(side=TOP, expand=TRUE, fill=BOTH)
else:
    status_label = ttk.Label(StatusFrame, textvariable=connection_status, font=("Arial", 12))
    status_label.pack(side=TOP, expand=TRUE, fill=BOTH)


host_label = ttk.Label(StatusFrame, textvariable=current_host, font=("Arial", 12))
host_label.pack(side=TOP, expand=TRUE, fill=BOTH)

user_label = ttk.Label(StatusFrame, textvariable=current_user, font=("Arial", 12))
user_label.pack(side=TOP, expand=TRUE, fill=BOTH)

# Run the Tkinter main loop
root.mainloop()
