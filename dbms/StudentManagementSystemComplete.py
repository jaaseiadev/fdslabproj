from tkinter import *
from tkinter import Toplevel
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter import ttk
import pymysql
import time
from tokenize import String

from jmespath import search


####################Connection to database function
def Connectdb():
    def connect():
        global con,mycursor
        host = hostval.get()
        user = userval.get()
        password = passwordval.get()
        try:
            connection = pymysql.connect(host=host, user=user, password=password)
            mycursor = con.cursor()

        except:
            messagebox.showerror('Notification', 'Data is Incorrect please try again')
            return

    dbroot = Toplevel()
    dbroot.grab_set()
    dbroot.geometry('470x250+800+230')
    dbroot.iconbitmap()
    dbroot.resizable(False,False)
    dbroot.config(bg = 'white')
    ##################Connect db labels
    hostlabel = Label(dbroot,text = 'Enter Host ',bg='white',font=('arial',18),relief=GROOVE , width= 13, anchor= 'w')
    hostlabel.place(x= 10, y = 10)

    userlabel = Label(dbroot, text='Enter Username  ', bg='white', font=('arial', 18 ), relief=GROOVE , width=13, anchor='w')
    userlabel.place(x=10, y=70)

    passwordlabel = Label(dbroot, text='Enter Password  ', bg='white', font=('arial', 18), relief=GROOVE , width=13, anchor='w')
    passwordlabel.place(x=10, y=130)

    ###################connectordb entry
    hostval = StringVar()
    userval = StringVar()
    passwordval = StringVar()

    hostentry= Entry(dbroot, font=('arial', 15), textvariable= hostval)
    hostentry.place(x = 220, y = 10)

    userentry = Entry(dbroot, font=('arial', 15),textvariable= userval)
    userentry.place(x=220, y=70)

    passwordentry = Entry(dbroot, font=('arial', 15),textvariable= passwordval)
    passwordentry.place(x=220, y=130)

    ###########Submit button / Connect to db
    submitbutton = Button(dbroot,text = 'Submit', font = ('arial', 15, 'bold'), width=20, command = connect)
    submitbutton.place(x = 110, y = 190)
    dbroot.mainloop()
#####################################

def addstudent():
    def submitadd():
        print('submit add')
        print('student submit')
    addroot = Toplevel(master = DataEntryFrame)
    addroot.grab_set()
    addroot.geometry('480x380+100+100')
    addroot.title('Student Manangement System')
    addroot.config(bg = 'white')
    addroot.iconbitmap()
    addroot.resizable(False,False)
    ########_________________________________add student labels
    idlabel = Label(addroot,text='Enter ID : ',bg = 'white',font=('arial',18))
    idlabel.place(x=10,y=10)

    surnamelabel = Label(addroot, text='Enter Surname : ', bg='white', font=('arial', 18))
    surnamelabel.place(x=10, y=70)

    firstnamelabel = Label(addroot, text='Enter Firstname : ', bg='white', font=('arial', 18))
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = Label(addroot, text='Enter Birthdate : ', bg='white', font=('arial', 18))
    birthdatelabel.place(x=10, y=190)

    sexlabel = Label(addroot, text='Enter Sex : ', bg='white', font=('arial', 18))
    sexlabel.place(x=10, y=250)

######--------------------------------------------->Student Entry
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    identry = Entry(addroot, font=('arial', 15),textvariable=idval)
    identry.place(x=250, y = 10)

    surnameentry = Entry(addroot, font=('arial', 15), textvariable= surnameval)
    surnameentry.place(x=250, y=70)

    firstnameentry = Entry(addroot, font=('arial', 15), textvariable= firstnameval)
    firstnameentry.place(x=250, y=130)

    birthdateentry = Entry(addroot, font=('arial', 15), textvariable=birthdateval)
    birthdateentry.place(x=250, y=190)

    sexentry = Entry(addroot, font=('arial', 15), textvariable=sexval)
    sexentry.place(x=250, y=250)

    ###submit button
    submitbtn = Button(addroot,text = 'Submit', font = ('arial', 15, 'bold'), width=20, command = submitadd)
    submitbtn.place(x = 110, y = 310)

    addroot.mainloop()
def searchstudent():
    def search():
        print('search submit')

    searchroot = Toplevel(master=DataEntryFrame)
    searchroot.grab_set()
    searchroot.geometry('480x380+100+100')
    searchroot.title('Student Manangement System')
    searchroot.config(bg='white')
    searchroot.iconbitmap()
    searchroot.resizable(False, False)
    ########_________________________________add student labels
    idlabel = Label(searchroot, text='Enter ID : ', bg='white', font=('arial', 18))
    idlabel.place(x=10, y=10)

    surnamelabel = Label(searchroot, text='Enter Surname : ', bg='white', font=('arial', 18))
    surnamelabel.place(x=10, y=70)

    firstnamelabel = Label(searchroot, text='Enter Firstname : ', bg='white', font=('arial', 18))
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = Label(searchroot, text='Enter Birthdate : ', bg='white', font=('arial', 18))
    birthdatelabel.place(x=10, y=190)

    sexlabel = Label(searchroot, text='Enter Sex : ', bg='white', font=('arial', 18))
    sexlabel.place(x=10, y=250)

    ######--------------------------------------------->Student Entry
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    identry = Entry(searchroot, font=('arial', 15), textvariable=idval)
    identry.place(x=250, y=10)

    surnameentry = Entry(searchroot, font=('arial', 15), textvariable=surnameval)
    surnameentry.place(x=250, y=70)

    firstnameentry = Entry(searchroot, font=('arial', 15), textvariable=firstnameval)
    firstnameentry.place(x=250, y=130)

    birthdateentry = Entry(searchroot, font=('arial', 15), textvariable=birthdateval)
    birthdateentry.place(x=250, y=190)

    sexentry = Entry(searchroot, font=('arial', 15), textvariable=sexval)
    sexentry.place(x=250, y=250)

    ###submit button
    submitbtn = Button(searchroot, text='Search', font=('arial', 15, 'bold'), width=20, command=search)
    submitbtn.place(x=110, y=310)

    searchroot.mainloop()
def deletestudent():
    print('Student delete')
def updatestudent():
    def update():
        print('search submit')

    updateroot = Toplevel(master=DataEntryFrame)
    updateroot.grab_set()
    updateroot.geometry('480x380+100+100')
    updateroot.title('Student Manangement System')
    updateroot.config(bg='white')
    updateroot.iconbitmap()
    updateroot.resizable(False, False)
    ########_________________________________add student labels
    idlabel = Label(updateroot, text='Enter ID : ', bg='white', font=('arial', 18))
    idlabel.place(x=10, y=10)

    surnamelabel = Label(updateroot, text='Enter Surname : ', bg='white', font=('arial', 18))
    surnamelabel.place(x=10, y=70)

    firstnamelabel = Label(updateroot, text='Enter Firstname : ', bg='white', font=('arial', 18))
    firstnamelabel.place(x=10, y=130)

    birthdatelabel = Label(updateroot, text='Enter Birthdate : ', bg='white', font=('arial', 18))
    birthdatelabel.place(x=10, y=190)

    sexlabel = Label(updateroot, text='Enter Sex : ', bg='white', font=('arial', 18))
    sexlabel.place(x=10, y=250)

    ######--------------------------------------------->Student Entry
    idval = StringVar()
    surnameval = StringVar()
    firstnameval = StringVar()
    birthdateval = StringVar()
    sexval = StringVar()

    identry = Entry(updateroot, font=('arial', 15), textvariable=idval)
    identry.place(x=250, y=10)

    surnameentry = Entry(updateroot, font=('arial', 15), textvariable=surnameval)
    surnameentry.place(x=250, y=70)

    firstnameentry = Entry(updateroot, font=('arial', 15), textvariable=firstnameval)
    firstnameentry.place(x=250, y=130)

    birthdateentry = Entry(updateroot, font=('arial', 15), textvariable=birthdateval)
    birthdateentry.place(x=250, y=190)

    sexentry = Entry(updateroot, font=('arial', 15), textvariable=sexval)
    sexentry.place(x=250, y=250)

    ###submit button
    submitbtn = Button(updateroot, text='Update', font=('arial', 15, 'bold'), width=20, command=update)
    submitbtn.place(x=110, y=310)

    updateroot.mainloop()
def showstudent():
    print('Student show')
def exportstudent():
    print('Student export')
def exitstudent():
    res = messagebox.askyesnocancel('Notification ', 'Do you want to exit?')
    if(res == True):
        root.destroy()

# Initialize Tkinter window
root = Tk()
root.title('Student Management System')
root.config(bg='white')
root.geometry('1175x1000+300+10')
root.iconbitmap()  # If you have an icon, provide the path like root.iconbitmap('path_to_icon.ico')
root.resizable(False, False)

# Variables for the slider
ss = 'Jaaseia Gian R Abenoja  '
count = 0  # Initial count for character position in slider text
text = ''  # Initial text for the slider display

# Function for the slider effect
def IntroLabelTick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''  # Reset text when the end of the string is reached
        SliderLabel.config(text = text);
    else:
        text += ss[count]
        SliderLabel.config(text=text)
        count += 1
    SliderLabel.after(200, IntroLabelTick)
######################################################################### Main frames

DataEntryFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=2)
DataEntryFrame.place(x=10, y=80, width=360, height=550)
frontlabel = Label(DataEntryFrame, text = 'Welcome', width= 25,font=('arial',20))
frontlabel.pack(side=TOP,expand = TRUE)

addbtn = Button(DataEntryFrame, text = '1. Add Student',width= 25,font=('arial',17), command= addstudent)
addbtn.pack(side=TOP,expand = TRUE)

searchbtn = Button(DataEntryFrame, text = '2. Search Student',width= 25,font=('arial',17), command= searchstudent)
searchbtn.pack(side=TOP,expand = TRUE)

deletebtn = Button(DataEntryFrame, text = '3. Delete Student',width= 25,font=('arial',17),command= deletestudent)
deletebtn.pack(side=TOP,expand = TRUE)

updatebtn = Button(DataEntryFrame, text = '4. Update Student',width= 25,font=('arial',17), command = updatestudent)
updatebtn.pack(side=TOP,expand = TRUE)

showallbtn = Button(DataEntryFrame, text = '5. Show All',width= 25,font=('arial',17),command= showstudent)
showallbtn.pack(side=TOP,expand = TRUE)

exportbtn = Button(DataEntryFrame, text = '6. Export Data',width= 25,font=('arial',17),command = exportstudent)
exportbtn.pack(side=TOP,expand = TRUE)

exitbtn = Button(DataEntryFrame, text = '7. Exit',width= 25,font=('arial',17), command= exitstudent)
exitbtn.pack(side=TOP,expand = TRUE)



#################Showing the main frames
ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=2)
ShowDataFrame.place(x=450, y=80, width=680, height=550)

####showing the main data
# Scrollbars
style = ttk.Style()
style.configure('Treeview.Heading', font=('arial', 11, 'bold'))

scroll_x = Scrollbar(ShowDataFrame, orient=HORIZONTAL)
scroll_y = Scrollbar(ShowDataFrame, orient=VERTICAL)
# Treeview widget with scrollbars
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
studenttable.heading('Sex', text = 'Sex')
studenttable.column('Student ID', width=100)
studenttable.column('Surname', width=100)
studenttable.column('First Name', width=100)
studenttable.column('Birthdate', width=100)
studenttable.column('Sex', width=100)
studenttable['show'] = 'headings'
studenttable.pack(fill=BOTH, expand=1)





########################################################################## Slider label
SliderLabel = Label(root, text=ss, font=('arial', 30, 'bold'), relief=RIDGE, borderwidth=5, bg='pink')
SliderLabel.place(x=260, y=0)

#######################################Start the slider animation
IntroLabelTick()
#######################################

########################################## Connect database
connectbutton = Button(root,text = 'Connect to Database', width= 20,font=('arial', 13, 'bold'), relief= RIDGE, borderwidth= 4, bd=6, bg= 'white',
                       activebackground='black', activeforeground= 'black', command=Connectdb)
connectbutton.place(x=900, y = 0)
# Run the Tkinter main loop
root.mainloop()
