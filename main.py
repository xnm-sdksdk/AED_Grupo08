import os
from tkinter import *
from tkinter import ttk
import datetime
from tkinter import messagebox










def menu():
    menu_window = Toplevel(main)
    menu_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    menu_window.title("Register")
    # register_window.resizable(0,0)
    menu_window.focus_force() # Forces the focus to the current window
    menu_window.grab_set() # Directs all events to the active window






# Register Window
def register():
    register_window = Toplevel(main)
    register_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    register_window.title("Register")
    # register_window.resizable(0,0)
    register_window.focus_force() # Forces the focus to the current window
    register_window.grab_set() # Directs all events to the active window


    # Register Components
    # Name Label
    name_registerlbl = Label(register_window, text="Register", font= ("Sans Serif", 20), fg="#000")
    name_registerlbl.place(x=500,y=100)
    
    
    # Name Entry
    name_register_entry = Entry(register_window) # variable =
    name_register_entry.place(x=650,y=110)
    
    
    # Email Label
    email_lbl = Label(register_window, text="Email", font= ("Sans Serif", 20), fg="#000")
    email_lbl.place(x=500,y=150)
    
    
    # Email Entry
    email_entry = Entry(register_window) # variable =
    email_entry.place(x=650,y=160)
    
    
    # Password Label
    password_registerlbl = Label(register_window, text="Password", font= ("Sans Serif", 20), fg="#000")
    password_registerlbl.place(x=500,y=200)


    # Password Entry
    password_entry = Entry(register_window) # variable =
    password_entry.place(x=650,y=210)


    # Type of User Confirmation
    # User
    cb1 = Checkbutton(register_window, text="User")
    cb1.place(x=500,y=250) 
    
    
    # Admin
    cb2 = Checkbutton(register_window, text="Admin")
    cb2.place(x=600,y=250)




# Login Window
def login():
    login_window = Toplevel(main)
    
    # Different dimensions for the login window
    login_width = 500
    login_height = 250
    login_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(login_width, login_height, int(x), int(y)))
    login_window.title("Login")
    # register_window.resizable(0,0)
    login_window.focus_force() # Forces the focus to the current window
    login_window.grab_set() # Directs all events to the active window


    # Login Components
    # Name Label 
    name_loginlbl = Label(login_window, text="Name", font=("Sans Serif", 20), fg="#000")
    name_loginlbl.place(x=80,y=50)

    # Name Entry
    name_login_entry = Entry(login_window) # variable =
    name_login_entry.place(x=250,y=60)

    # Password Label
    password_loginlbl = Label(login_window, text="Password", font=("Sans Serif", 20), fg="#000")
    password_loginlbl.place(x=80,y=100)    
    
    # Password Entry
    password_login_entry = Entry(login_window) # variable =
    password_login_entry.place(x=250,y=110)







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
password_Entry = Entry(main) # variable =
password_Entry.place(x=650,y=200)


# Login Button
login_btn = Button(main, text = 'Login', font=('Sans Serif', 16, "bold"),width=6, command = login)
login_btn.place(x=700,y=250)


# Register Button
register_btn = Button(main, text = 'Register', font = ('Sans Serif', 16, "bold"),width = 6, command = register)
register_btn.place(x=500,y=250)

# Main Window Loop
main.mainloop()