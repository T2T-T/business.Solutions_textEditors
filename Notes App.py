from tkinter import *
from tkinter import filedialog
from tkmacosx import Button

# Keep track of the currently opened file
current_file = None

def open_file():
    global current_file
    current_file = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    if current_file:
        with open(current_file, "r") as f:
            content = f.read()
            T.delete("1.0", END)
            T.insert("1.0", content)

def save_file():
    global current_file
    if current_file is None:
        current_file = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

    if current_file:
        text_content = T.get("1.0", END)
        with open(current_file, "w") as f:
            f.write(text_content)
        print("Content saved.")

# Create the main window
root = Tk()
root.title("Notes")

# Text widget
T = Text(root, width=50, height=20)
T.pack(pady=10)

# Buttons
open_button = Button(root, text="Open", background="blue", command=open_file)
save_button = Button(root, text="Save", background="red", command=save_file)

open_button.pack(side=LEFT, padx=10)
save_button.pack(side=LEFT, padx=10)

# Start the GUI event loop
root.mainloop()