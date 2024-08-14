import os
import shutil as sh
import tkinter as tk
from tkinter import messagebox


def submit():
    source_directory = entry.get()
    try:
        # get a list of all files in the source directory
        file_list = os.listdir(source_directory)

        # create a directory for each file extension
        for file_name in file_list:
            file_extension = os.path.splitext(file_name)[1][1:]
            destination_directory = os.path.join(source_directory, file_extension)
            if os.path.exists(destination_directory) == False:
                os.makedirs(destination_directory)
            # move the file to the appropriate directory
            source_path = os.path.join(source_directory, file_name)
            destination_path = os.path.join(destination_directory, file_name)
            sh.move(source_path, destination_path)

        messagebox.showinfo(title = "Successful", message = "The files have been moved successfully")
        window.destroy()
    except Exception as e:
        messagebox.showinfo(title = "Error", message = f"An error occurred while sorting the files: {e}")
        window.destroy()

# Tkinter graphical interface
window = tk.Tk()
window.geometry("500x300")
label = tk.Label(window, text = "Input the directory you want to sort", font = ("Arial", 20))
label.pack(pady=50)

entry = tk.Entry(window, font = ("Arial", 10), width = 50)
entry.pack(pady=10)
submit_button = tk.Button(window, text="Submit", command=submit)
submit_button.pack()
window.mainloop()