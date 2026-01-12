from tkinter import *

from tkmacosx import Button






def change_label_text():
  label.config(text="Updated")

def change_label1_text():
  label1.config(text="Updated")

def change_label2_text():
  label2.config(text="Updated")

# Create the main window
root = Tk()
root.title("Enter Title Here")

#Set size of window
root.geometry("300x150")

# Create buttons
red_button = Button(root, text="button 1", background= 'white', command=change_label_text)
yellow_button = Button(root, text="button 2", background= "white",command=change_label1_text)
green_button = Button(root, text="button 3",background= "white",command=change_label2_text)
white_button = Button(root, text="random", background= "white")
#Add a label
label = Label(root, text="lable 1")
label1 = Label(root,text="label 2")
label2 = Label(root, text="lable 3")
# Place widgets in window (with pack function!)
label.grid(row=0,column=2)
label1.grid(row=1,column=2)
label2.grid(row=2,column=2)
red_button.grid(row=0,column=0)
yellow_button.grid(row=1,column=0)
green_button.grid(row=2,column=0)
white_button.grid(row=3,column=1)
# Start the GUI event loopte
#now we show it working
root.mainloop()