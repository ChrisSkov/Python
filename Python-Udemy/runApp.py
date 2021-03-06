import tkinter as tk
from tkinter import filedialog, Text
import os

root = tk.Tk()
apps = []


def addApp():
    
    for widget in frame.winfo_reqwidth():
        widget.destroy()
    
    filename= filedialog.askopenfilename(initialdir="/", title="Select File", filetypes=(("executables", "*.exe"),("all files", "*,*")))
    apps.append(filename)
    for app in apps:
        label = tk.Label(frame, text=app, bg="gray")
        label.pack()
        
def runAoo(): apps:list

canvas = tk.Canvas(root, height=700, width=700, bg="white")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5,fg="white", bg="teal", command=addApp)

openFile.pack()

runApps = tk.Button(root, text="Run Apps", padx=10, pady=5,fg="white", bg="teal", command=addApp)

runApps.pack()

root.mainloop()