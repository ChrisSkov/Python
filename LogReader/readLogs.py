import pathlib
import tkinter as tk
from tkinter import filedialog, Text
import os


root = tk.Tk()

no_of_errors = 0
with open("D:/Python/LogsToRead/.logs/combined-log-24-08-2020.log", "r") as a_file:
    for line in a_file:
        stripped_line = line.strip()
        if stripped_line.startswith("{\"error\""):
            no_of_errors += 1
        print(stripped_line)

print(no_of_errors)
# Open directory with logs files
# log_file_path = {path to dir}
# create regex for various scenarios e.g error, context etc
# create list of matches
# match_list = []
# search files for lines matching regex
# with open (file) as file
# for line in file
# for match in re.finditer(regex, line, re.S):
# match_text = match.group()
# math_list.append(match_text)
# print match_text


def selectLogDir():
    directory_name = filename = filedialog.askdirectory()
    for path in pathlib.Path(directory_name).iterdir():
        if path.is_file():
            current_file = open(path, "r")
            print(current_file.read())
            current_file.close()


canvas = tk.Canvas(root, height=700, width=700, bg="teal")
canvas.pack()
frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

openFile = tk.Button(root, text="Open File", padx=10, pady=5, fg="white", bg="teal", command=selectLogDir)
openFile.pack()

root.mainloop()