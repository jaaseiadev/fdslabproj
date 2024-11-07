from tkinter import *
from tkinter import Toplevel
import time
from tokenize import String


####################Connection to database
def Connectdb():
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
    submitbutton = Button(dbroot,text = 'Submit', font = ('arial', 15, 'bold'), width=20)
    submitbutton.place(x = 110, y = 190)
    dbroot.mainloop()
#####################################

# Initialize Tkinter window
root = Tk()
root.title('Student Management System')
root.config(bg='white')
root.geometry('1174x700+200+50')
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
DataEntryFrame.place(x=10, y=80, width=400, height=600)

ShowDataFrame = Frame(root, bg='white', relief=GROOVE, borderwidth=2)
ShowDataFrame.place(x=550, y=80, width=620, height=600)
########################################################################## Slider label
SliderLabel = Label(root, text=ss, font=('arial', 30, 'bold'), relief=RIDGE, borderwidth=5, bg='pink')
SliderLabel.place(x=260, y=0)

######################################################################## Clock label with corrected syntax and placement
############################################################################## Start the slider animation
IntroLabelTick()
########################################## Connect database
connectbutton = Button(root,text = 'Connect to Database', width= 20,font=('arial', 13, 'bold'), relief= RIDGE, borderwidth= 4, bd=6, bg= 'white',
                       activebackground='black', activeforeground= 'black', command=Connectdb)
connectbutton.place(x=900, y = 0)
# Run the Tkinter main loop
root.mainloop()
