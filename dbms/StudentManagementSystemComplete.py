from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview, Style
import tkinter as tk
import tkinter as tk
from tkinter import ttk
import pymysql
import csv
import re


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
        except Exception as e:
            messagebox.showerror('Notifications', f'Data is incorrect please try again: {e}', parent=dbroot)
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
                   birthdate CHAR(10),
                   sex CHAR(1),
                   address VARCHAR(255),
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
    dbroot.geometry('450x250+800+50')
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
    submitbutton = ttk.Button(dbroot, text='Submit',style='Accent.TButton' ,command=submitdb)
    submitbutton.place(x=170, y=190)

    dbroot.mainloop()

# Function to add a new student
def addstudent():
    def submitadd():
        id = idval.get()
        surname = surnameval.get()
        firstname = firstnameval.get()
        birthdate = birthdateval.get()
        sex = sexval.get()
        address = addressval.get()

        # Basic validation for empty fields
        if id == "" or surname == "" or firstname == "" or birthdate == "" or sex == "" or address == "":
            messagebox.showerror('Error', 'All fields are required', parent=addroot)
            return

        # Validate the birthdate format
        date_pattern = re.compile(r"^(0[1-9]|1[0-2])/[0-2][0-9]|(3[01])/\d{4}$")
        if not date_pattern.match(birthdate):
            messagebox.showerror('Error', 'Date must be in format mm/dd/yyyy', parent=addroot)
            return

        # Validate the sex field
        if sex not in ['M', 'F']:
            messagebox.showerror('Error', "Sex must be 'm' or 'f'", parent=addroot)
            return

        try:
            # Adjust the INSERT statement to reflect the actual columns in your database scheme
            strr = 'INSERT INTO studentdata1 (studid, surname, firstname, birthdate, sex, address) VALUES (%s, %s, %s, %s, %s, %s)'
            mycursor.execute(strr, (id, surname, firstname, birthdate, sex, address))
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
            vv = list(i)  # Handles any number of columns returned
            studenttable.insert('', 'end', values=vv)

    addroot = Toplevel(master=DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('430x420+100+100')
    addroot.title('Student Management System')
    addroot.resizable(False, False)

    # Add student labels
    idlabel = ttk.Label(addroot, text='Enter ID:')
    idlabel.place(x=10, y=10)

    surnamelabel = ttk.Label(addroot, text='Enter Surname:')
    surnamelabel.place(x=10, y=70)

    firstnamelabel = ttk.Label(addroot, text='Enter Firstname:')
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = ttk.Label(addroot, text='Enter Birthdate (MM/DD/YYYY):')
    birthdatelabel.place(x=10, y=190)

    sexlabel = ttk.Label(addroot, text='Enter Sex (M/F):')
    sexlabel.place(x=10, y=250)

    addresslabel = ttk.Label(addroot, text='Enter Address:')
    addresslabel.place(x=10, y=310)

    # Student Entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()
    addressval = StringVar()

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

    addressentry = ttk.Entry(addroot, textvariable=addressval)
    addressentry.place(x=250, y=310)

    # Submit button
    submitbtn = ttk.Button(addroot, text='Submit', style='Accent.TButton', command=submitadd)
    submitbtn.place(x=170, y=360)

    addroot.mainloop()

# Function to search for a student
def searchstudent():
    def search():
        id = idval.get()
        surname = surnameval.get()
        firstname = firstnameval.get()
        birthdate = birthdateval.get()
        sex = sexval.get()
        address = addressval.get()

        if id != '':
            strr = 'SELECT * FROM studentdata1 WHERE studid=%s'
            mycursor.execute(strr, (id,))
        elif surname != '':
            strr = 'SELECT * FROM studentdata1 WHERE surname=%s'
            mycursor.execute(strr, (surname,))
        elif firstname != '':
            strr = 'SELECT * FROM studentdata1 WHERE firstname=%s'
            mycursor.execute(strr, (firstname,))
        elif birthdate != '':
            strr = 'SELECT * FROM studentdata1 WHERE birthdate=%s'
            mycursor.execute(strr, (birthdate,))
        elif sex != '':
            strr = 'SELECT * FROM studentdata1 WHERE sex=%s'
            mycursor.execute(strr, (sex,))
        elif address != '':
            strr = 'SELECT * FROM studentdata1 WHERE address=%s'
            mycursor.execute(strr, (address,))
        else:
            messagebox.showerror('Error', 'At least one field must be filled', parent=searchroot)
            return

        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
            studenttable.insert('', END, values=vv)

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('430x420+100+100')
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

    addresslabel = ttk.Label(searchroot, text='Enter Address:')
    addresslabel.place(x=10, y=310)

    # Student entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()
    addressval = StringVar()

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

    addressentry = ttk.Entry(searchroot, textvariable=addressval)
    addressentry.place(x=250, y=310)

    # Search button
    submitbtn = ttk.Button(searchroot, text='Search', style='Accent.TButton',command=search)
    submitbtn.place(x=160, y=360)

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

        # Ensure the student ID is a valid string or int
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
            vv = [i[0], i[1], i[2], i[3], i[4]]  # Assuming i[4] is the address
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
        address = addressval.get()

        # Basic validation for empty fields
        if not new_id or not surname or not firstname or not birthdate or not sex or not address:
            messagebox.showerror('Error', 'All fields are required', parent=updateroot)
            return

        # Validate the birthdate format
        date_pattern = re.compile(r"^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/\d{4}$")
        if not date_pattern.match(birthdate):
            messagebox.showerror('Error', 'Date must be in format MM/DD/YYYY', parent=updateroot)
            return

        # Validate the sex field
        if sex not in ['M', 'F']:
            messagebox.showerror('Error', "Sex must be 'M' or 'F'", parent=updateroot)
            return

        try:
            strr = 'UPDATE studentdata1 SET studid=%s, surname=%s, firstname=%s, birthdate=%s, sex=%s, address=%s WHERE studid=%s'
            mycursor.execute(strr, (new_id, surname, firstname, birthdate, sex, address, old_id))
            con.commit()
            messagebox.showinfo('Notification', f'Student ID {old_id} updated successfully to {new_id}',
                                parent=updateroot)

            # Refresh the table
            strr = 'SELECT * FROM studentdata1'
            mycursor.execute(strr)
            datas = mycursor.fetchall()
            studenttable.delete(*studenttable.get_children())
            for i in datas:
                vv = [i[0], i[1], i[2], i[3], i[4], i[5]]
                studenttable.insert('', 'end', values=vv)
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
            addressval.set('')
            messagebox.showerror('Error', 'Please select a student to update.', parent=updateroot)
        else:
            update_button.configure(state=tk.NORMAL)
            original_id.set(pp[0])  # Store original student ID
            idval.set(pp[0])
            surnameval.set(pp[1])
            firstnameval.set(pp[2])
            birthdateval.set(pp[3])
            sexval.set(pp[4])
            addressval.set(pp[5])  # Set address

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('430x420+100+100')
    updateroot.title('Student Management System')
    updateroot.resizable(False, False)

    original_id = StringVar()  # Variable to store the original student ID

    # Update student labels
    ttk.Label(updateroot, text='Enter ID:').place(x=10, y=10)
    ttk.Label(updateroot, text='Enter Surname:').place(x=10, y=70)
    ttk.Label(updateroot, text='Enter Firstname:').place(x=10, y=130)
    ttk.Label(updateroot, text='Enter Birthdate (MM/DD/YYYY):').place(x=10, y=190)
    ttk.Label(updateroot, text='Enter Sex (M/F):').place(x=10, y=250)
    ttk.Label(updateroot, text='Enter Address:').place(x=10, y=310)

    # Student entry fields
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()
    addressval = StringVar()

    ttk.Entry(updateroot, textvariable=idval).place(x=250, y=10)
    ttk.Entry(updateroot, textvariable=surnameval).place(x=250, y=70)
    ttk.Entry(updateroot, textvariable=firstnameval).place(x=250, y=130)
    ttk.Entry(updateroot, textvariable=birthdateval).place(x=250, y=190)
    ttk.Entry(updateroot, textvariable=sexval).place(x=250, y=250)
    ttk.Entry(updateroot, textvariable=addressval).place(x=250, y=310)

    # Update button
    update_button = ttk.Button(updateroot, text='Update', style='Accent.TButton', command=update)
    update_button.place(x=170, y=370)

    # Check if a student is selected before enabling the 'Update' button
    check_selection()

    updateroot.mainloop()


#Show the tables
def showstudent():
    try:
        mycursor.execute('SELECT * FROM studentdata1')
        datas = mycursor.fetchall()
        studenttable.delete(*studenttable.get_children())
        for i in datas:
            vv = [i[0], i[1], i[2], i[3], i[4]]
            studenttable.insert('', 'end', values=vv)
        apply_sort()
    except Exception as e:
        messagebox.showerror('Error', f'Error while fetching data: {e}')

#Export to a csv file function
def exportstudent():
    try:
        strr = 'SELECT * FROM studentdata1'
        mycursor.execute(strr)
        datas = mycursor.fetchall()

        if not datas:
            messagebox.showinfo('Information', 'No student data available to export.')
            return

        with open("student_data.csv", "w", newline='') as file:
            writer = csv.writer(file)
            # Writing the header
            writer.writerow(["Student ID", "Surname", "First Name", "Birthdate", "Sex", "Address"])
            # Writing the data
            for record in datas:
                writer.writerow(record)

        messagebox.showinfo('Success', 'Data exported successfully to student_data.csv')

    except Exception as e:
        messagebox.showerror('Error', f'Error while exporting data: {e}')

#Exits the code
def exitstudent():
    res = messagebox.askyesnocancel('Notification', 'Do you want to exit?')
    if (res == True):
        root.destroy()



# Initialize Tkinter main  window
root = tk.Tk()
root.title('Student Management System')
root.geometry('1150x700+300+10')
root.resizable(False, False)
root.iconbitmap('icon.ico')
root.tk.call("source", "forest-dark.tcl")
ttk.Style().theme_use('forest-dark')

# Variables for the header, title
ss = 'Student Management System '
count = 0
text = ''
connection_status = StringVar()
connection_status.set("Not Connected")
current_host = StringVar()
current_host.set("Host: N/A")
current_user = StringVar()
sort_var = StringVar(value="Default (ID)")

# Sort Options
def apply_sort():
    sort_option = sort_var.get()
    query = 'SELECT * FROM studentdata1'
    try:
        mycursor.execute(query)
        data = mycursor.fetchall()

        if sort_option == "Surname (A-Z)":
            sorted_data = sorted(data, key=lambda x: x[1].lower())
        elif sort_option == "Surname (Z-A)":
            sorted_data = sorted(data, key=lambda x: x[1].lower(), reverse=True)
        else:  # Default sort (Student ID)
            sorted_data = sorted(data, key=lambda x: x[0])

        studenttable.delete(*studenttable.get_children())
        for student in sorted_data:
            studenttable.insert('', 'end', values=student)

    except Exception as e:
        messagebox.showerror('Error', f"Error while sorting data: {e}")


# Change sort menu options
sort_options = ["Sort by Default", "Surname (A-Z)", "Surname (Z-A)", "Default ( ID )"]
sort_menu = ttk.OptionMenu(root, sort_var, *sort_options, style='Accent.TButton', command=lambda _: apply_sort())
sort_menu.place(x=1010, y=45)

#main menu frame
DataEntryFrame = Frame(root)
DataEntryFrame.place(x=10, y=80, width=300, height=550)
border_frame = tk.Frame(root, highlightthickness=1, bd=0)
border_frame.pack(padx=10, pady=10)
frontlabel = tk.Label(DataEntryFrame, text='Main Menu', font=("Arial", 20, "bold"))
frontlabel.pack()

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

scroll_y = ttk.Scrollbar(ShowDataFrame, orient=VERTICAL)
scroll_x = ttk.Scrollbar(ShowDataFrame, orient=HORIZONTAL)

studenttable = Treeview(ShowDataFrame, columns=(
'Student ID', 'Surname', 'First Name', 'Birthdate', 'Sex',  'Address'),
                        yscrollcommand=scroll_y.set,
                        xscrollcommand=scroll_x.set)
scroll_y.pack(side=RIGHT, fill=Y)
scroll_x.pack(side=BOTTOM, fill=X)

studenttable.heading('Student ID', text='Student ID')
studenttable.heading('Surname', text='Surname')
studenttable.heading('First Name', text='First Name')
studenttable.heading('Birthdate', text='Birthdate')
studenttable.heading('Sex', text='Sex')
studenttable.heading('Address', text='Address')

studenttable.column('Student ID', width=100)
studenttable.column('Surname', width=100)
studenttable.column('First Name', width=100)
studenttable.column('Birthdate', width=100)
studenttable.column('Sex', width=50)
studenttable.column('Address', width=200)

studenttable['show'] = 'headings'
studenttable.pack(fill=BOTH, expand=1)

# Slider label
SliderLabel = ttk.Label(root, text=ss, font=('arial', 30, 'bold'))
SliderLabel.place(x=330, y=0)
sss = "Jaaseia Gian R. Abenoja FDS Laboratory Exercise "
SliderLabel = ttk.Label(root, text=sss, font=('arial', 7))
SliderLabel.place(x=480, y=45)

# Connect to database button
connectbutton = ttk.Button(root, text='Connect to Database', style = 'Accent.TButton', command=Connectdb)
connectbutton.place(x=155 , y=8)

StatusFrame = Frame(root, bg='white', relief=GROOVE)
StatusFrame.place(x=10, y=5, width=120, height=70)

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
