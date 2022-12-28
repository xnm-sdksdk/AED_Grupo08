import os
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox







# Register Window
def register():
    register_window = Toplevel(main)
    register_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    register_window.title("Register")
    # register_window.resizable(0,0)
    register_window.focus_force() # Forces the focus to the current window
    register_window.grab_set() # Directs all events to the active window







# Login Window
def login():
    login_window = Toplevel(main)
    login_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    login_window.title("Register")
    # register_window.resizable(0,0)
    login_window.focus_force() # Forces the focus to the current window
    login_window.grab_set() # Directs all events to the active window




# Main Window Initialization 
main = Tk()

# Defining the app with and height - DIMENSIONS OF THE APP TO BE DECIDE LATER #########################
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
main.configure() # Background Configurations - COLOR TO BE DECIDE LATER ################
# main.resizable(0,0) disable resizing of the app


# Main Window Components

# Name Label
namelbl = Label(main, text="Name", font= ("Sans Serif", 20), fg="#000")
namelbl.place(x=500,y=150)


# Name Entry
name_Entry = Entry(main) # variable =
name_Entry.place(x=650,y=160)


# Password Label
passwordlbl = Label(main, text="Password", font= ("Sans Serif", 20), fg="#000")
passwordlbl.place(x=500,y=200)


# Password Entry
password_Entry = Entry(main)
password_Entry.place(x=650,y=200)


# Login Button
login_btn = Button(main, text = 'Login', font=('Sans Serif', 16, "bold"),width=6, command = login)
login_btn.place(x=700,y=250)


# Register Button
register_btn = Button(main, text = 'Register', font = ('Sans Serif', 16, "bold"),width = 6, command = register) # command =
register_btn.place(x=500,y=250)

# Main Window Loop
main.mainloop()