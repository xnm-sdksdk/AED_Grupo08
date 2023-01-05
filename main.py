from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import os


# Import the other files
from users import *






def menu():
    
    
    main.withdraw()
    
    menu_window = Toplevel(main)
    menu_window.focus_force()
    menu_window.grab_set()
    
    
    menu_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    menu_window.title("Menu")
    # register_window.resizable(0,0)






# Register Window
# Function to allow user to register in the app
def register():
    
    main.withdraw() # Function to close the main window
    
    # Create a new window in Top Level Mode
    register_window = Toplevel(main)
    register_window.focus_force() # Forces the focus to the current window
    register_window.grab_set() # Directs all events to the active window
    
    
    
    # Global Variables to use the, outside of the defined function
    """
    global name_regist_temp
    global age_regist_temp
    global email_regist_temp
    global password_regist_temp
    global password_confirmation
    global user_type
    """
    
    
    # Temporary Variables - to retrieve them later - keyword to execute that task: .get()
    name_regist_temp = StringVar()
    age_regist_temp = StringVar()
    email_regist_temp = StringVar()
    password_regist_temp = StringVar()
    user_type = StringVar()
    password_confirmation = StringVar()
    # Set User by Default as Type of  
    user_type.set('user')
    
    
    
    register_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(main_width, main_height, int(x), int(y)))
    register_window.title("Register")
    # register_window.resizable(0,0)
    #register_window.focus_force() # Forces the focus to the current window
    #register_window.grab_set() # Directs all events to the active window


    # Register Components
    # Name Label
    name_registerlbl = Label(register_window, text="Register", font= ("Sans Serif", 18), fg="#000")
    name_registerlbl.place(x=350,y=80)
    
    
    # Name Entry
    name_register_entry = Entry(register_window, textvariable = name_regist_temp)
    name_register_entry.place(x=480,y=85)
    
    
    # Age Label
    age_registerlbl = Label(register_window, text="Age", font=("Sans Serif", 18), fg="#000")
    age_registerlbl.place(x=350, y=130)
    
    
    # Age Entry
    age_register_entry = Entry(register_window, textvariable = age_regist_temp)
    age_register_entry.place(x=480,y=135)
    
    
    # Email Label
    email_lbl = Label(register_window, text="Email", font= ("Sans Serif", 18), fg="#000")
    email_lbl.place(x=350,y=180)
    
    
    # Email Entry
    email_entry = Entry(register_window, textvariable= email_regist_temp)
    email_entry.place(x= 480,y= 185)
    
    
    # Password Label
    password_registerlbl = Label(register_window, text="Password", font= ("Sans Serif", 18), fg="#000")
    password_registerlbl.place(x=350,y=230)


    # Password Entry
    password_entry = Entry(register_window, show="*", textvariable = password_regist_temp)
    password_entry.place(x=480,y=235)

    # Password Confirmation Label
    password_confirmationlbl = Label(register_window, text="Confirm", font= ("Sans Serif", 18), fg="#000")
    password_confirmationlbl.place(x=350,y=280)
    
    # Password Confirmation Entry
    password_confirmation_entry = Entry(register_window, show="*", textvariable = password_confirmation)
    password_confirmation_entry.place(x=480,y=285)

    # LabelFrame for CheckButtons
    lblFrame_user = LabelFrame(register_window, text="Type of User:",  width=120, height=70, relief="sunken", bd="3", fg="black")
    lblFrame_user.place(x= 350,y=350)
    

    # Type of User Confirmation
    # User
    cb1 = Radiobutton(lblFrame_user, text="User", variable= user_type, value= "user")
    cb1.place(x=0,y=0) 
    
    
    # Admin
    cb2 = Radiobutton(lblFrame_user, text="Admin", variable= user_type, value= "admin")
    cb2.place(x=0,y=20)


    submit_register_btn = Button(register_window, text="Submit", state="active", width=7, height=3, font=("Sans Serif", 12, "bold"), fg="#000000", command= lambda: verification(name_regist_temp.get(), age_regist_temp.get(), email_regist_temp.get(), password_regist_temp.get(), password_confirmation.get(), user_type.get())) # lambda function to call the function verification
    submit_register_btn.place(x=550,y=350)



# Login Window
# Function to allow user to sign up and access the app
def login():
    
    main.withdraw()
    
    login_window = Toplevel(main)
    login_window.focus_force()
    login_window.grab_set()
    
    # Global variables
    
    
    # Temporary Values
    login_name_temp = StringVar()
    login_password_temp = StringVar()
    
    
    
    # Different dimensions for the login window
    login_width = 500
    login_height = 250
    login_window.geometry("{:.0f}x{:.0f}+{:.0f}+{:.0f}".format(login_width, login_height, int(x), int(y)))
    login_window.title("Login")
    # register_window.resizable(0,0)
    
    #login_window.focus_force() # Forces the focus to the current window
    #login_window.grab_set() # Directs all events to the active window


    # Login Components
    # Name Label 
    name_loginlbl = Label(login_window, text="Name", font=("Sans Serif", 20), fg="#000")
    name_loginlbl.place(x=80,y=50)

    # Name Entry
    name_login_entry = Entry(login_window, textvariable = login_name_temp)
    name_login_entry.place(x=250,y=60)

    # Password Label
    password_loginlbl = Label(login_window, text="Password", font=("Sans Serif", 20), fg="#000")
    password_loginlbl.place(x=80,y=100)    
    
    # Password Entry
    password_login_entry = Entry(login_window, show="*", textvariable = login_password_temp)
    password_login_entry.place(x=250,y=110)


    # Login Button
    login_button = Button(login_window, text="Login", font=('Sans Serif', 12, "bold"),width=4, command= lambda: login_session(login_name_temp.get(), login_password_temp.get()))
    login_button.place(x=350,y=150)



# Login Session
# Function that is going to be executed after the login is successfully done
# To decide if the menu is going to be created within this function
def login_session():
    pass    
    


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


# Side Bar Settings

# For minimum and maximum size of the side bar
side_min = 50
side_max = 200

expansion = side_min # To expand the side bar

expanded = False # To check if the side bar is expanded or not

def grow_sidebar():
    global expansion, expanded
    
    expansion += 10 # To increase the width of the side bar
    repeat = main.after(5, grow_sidebar) # To repeat the function every 5 miliseconds
    frame.config(width=expansion) # To change the width of the side bar to the new width
    
    if expansion >= side_max:
        expanded = True
        main.after_cancel(repeat) # after_cancel() is used to cancel the function after it has been called
        colorize()

def shrink_sidebar():
    global expansion, expanded
    
    expansion -= 10 # To decrease the width of the side bar
    repeat = main.after(5, shrink_sidebar) # To repeat the function every 5 miliseconds
    frame.config(width=expansion) # To change the width of the side bar to the new width
    
    if expansion <= side_min:
        expanded = False
        main.after_cancel(repeat) # after_cancel() is used to cancel the function after it has been called
        colorize()

def colorize():
    if expanded == True:
        home_button_icon.config(text="Home", image="", font=(10))
        settings__button_icon.config(text="Settings", image="", font=(10))
        about__button_icon.config(text="About", image="", font=(10))

    else:
        home_button_icon.config(text="Home", image= home, font=(10))
        settings__button_icon.config(text="Settings", image= settings, font=(10))
        about__button_icon.config(text="About", image=about, font=(10))




main.update()
frame = Frame(main, bg='red', width=50, height=main.winfo_height())
frame.place(x=0,y=0)


# Left Frame of the main Window
# Images
home = PhotoImage(file = "Images/home.png")
settings = PhotoImage(file = "Images/settings.png")
about = PhotoImage(file = "Images/about.png")


# Side Bar Buttons
home_button_icon = Button(frame, image=home, bg="red", relief="flat")
settings__button_icon = Button(frame, image=settings, bg="red", relief="flat")
about__button_icon = Button(frame, image=about, bg="red", relief="flat")

home_button_icon.place(x=10, y=50)
settings__button_icon.place(x=10, y=150)
about__button_icon.place(x=10, y=250)


frame.bind("<Enter>", lambda event: grow_sidebar())
frame.bind("<Leave>", lambda event: shrink_sidebar())


# Text Label - To
to_txt = Label(main, text="To", font=("Sans Serif", 30, "bold"), fg="green")
to_txt.place(x=100,y=100)


# Text Label - Do
do_txt = Label(main, text="Do", font=("Sans Serif", 30, "bold"), fg="yellow")
do_txt.place(x=170,y=100)


# Text Label - List
list_txt = Label(main, text="List", font=("Sans Serif", 30, "bold"), fg="red")
list_txt.place(x=240,y=100)



# Image - To Be Decided



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