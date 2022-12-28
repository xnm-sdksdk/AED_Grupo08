import os
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox






















# Main Window Initialization 
main = Tk()

# Defining the app with and height
main_width = 1000
main_height = 500

# Getting the user screen width and height to center the app
screen_width = main.winfo_screenwidth()
screen_height = main.winfo_screenheight()

# x and y  used to calculate the coordinates for the Tk app main window
x = (screen_width/2) - (main_width/2) 
y = (screen_height/2) - (main_height/2)

# 
main.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y))) # 
main.title("To Do List") # Title of the app
main.configure() # Background Configurations
# main.resizable(0,0) disable resizing of the app


# Main Window Components




main.mainloop()