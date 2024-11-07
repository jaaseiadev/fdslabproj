from tkinter import *
import time

# Initialize Tkinter window
root = Tk()
root.title('Student Management System')
root.config(bg='white')
root.geometry('1174x700+200+50')
root.iconbitmap()  # If you have an icon, provide the path like root.iconbitmap('path_to_icon.ico')
root.resizable(False, False)

# Variables for the slider
ss = 'Jaaseia Gian R Abenoja'
count = 0  # Initial count for character position in slider text
text = ''  # Initial text for the slider display

# Function for the slider effect
def IntroLabelTick():
    global count, text
    if count >= len(ss):
        count = 0
        text = ''  # Reset text when the end of the string is reached
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
clock = Label(root, font=('times', 14, 'bold'), relief=RIDGE, borderwidth=4, bg='lawn green')
clock.place(x=0, y=0)

############################################################################## Start the slider animation
IntroLabelTick()

# Run the Tkinter main loop
root.mainloop()
