from tkinter import *
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
from tkinter.ttk import Combobox
import os


# Import the other files
from users import *
from todolist import *
from notifications import *
from favorites import *
from profileSettings import *
from settings import *



def catalog():
    
    panelCatalog = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    panelCatalog.place(x=200,y=50)


    # Entry Label - To Do List
    cataloglbl = Label(panelCatalog, text="To Do List", font=("Sans Serif", 20, "bold"), fg="#000")
    cataloglbl.place(x=0, y=0)


    # List Box to visualize the current info
    todolistBox = Listbox(panelCatalog, width=50, height=15, selectmode= "single")
    todolistBox.place(x=250,y=120)
    

    # Number os Tasks Label
    numberTasks= Label(panelCatalog, text="Number of Tasks: ", font=("Sans Serif", 10, "bold"), fg="#000000")
    numberTasks.place(x=250,y=50)
    

    # Insert Task Entry
    insertTask = Entry(panelCatalog, width=30) # textvariable
    insertTask.place(x=250,y=90)
    
    
    # Button Add Task
    addTask = Button(panelCatalog, text="Add Task", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000") #command= lambda: add_task(insertTask.get())
    addTask.place(x=30,y=80)


    # Delete Task Button
    deleteTask = Button(panelCatalog, text="Delete Task", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    deleteTask.place(x=30,y=140)


    # Sort ASC Button
    sortAscTask = Button(panelCatalog, text="Sort ASC", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    sortAscTask.place(x=30,y=200)


    # Sort DESC Button
    sortDescTask = Button(panelCatalog, text="Sort DESC", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    sortDescTask.place(x=30,y=260)
    
    
    # Delete All Button
    deleteAllTask = Button(panelCatalog, text="Delete All", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    deleteAllTask.place(x=30,y=320)


    # Section To filter the state of the tasks
    values = ["To Do", "Doing", "Done"]
    selectState = Combobox(panelCatalog, values=values, width=20)
    selectState.place(x=250,y=10)
    
    


def notifications():
    pass



def favorites():
    pass



def profile_Menu():
    
    # Paned Window Profile
    profilePanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    profilePanel.place(x=200,y=50)
    
    
    # Username Info
    usernameInfo = Label(profilePanel, text="Username: ", font=("Sans Serif", 15, "bold"), fg="#000000")
    usernameInfo.place(x=50,y=0)
    

    # Age Info
    ageInfo = Label(profilePanel, text="Age: ", font=("Sans Serif", 15, "bold"), fg="#000000")
    ageInfo.place(x=50,y=50)
    
    
    # Email Info
    emailInfo = Label(profilePanel, text="Email: ", font=("Sans Serif", 15, "bold"), fg="#000000")
    emailInfo.place(x=50,y=100)
    
    
    # Password Info
    passwordInfo = Label(profilePanel, text="Password: ", font=("Sans Serif", 15, "bold"), fg="#000000")
    passwordInfo.place(x=50,y=150)
    
    
    # Display Password CheckButton
    pwdDisplay = Checkbutton(profilePanel, text="Display Password", font=("Sans Serif", 15, "bold"), fg="#000000")
    pwdDisplay.place(x=50,y=200)





def settings():
    
    # Paned Window Settings
    settingsPanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    settingsPanel.place(x=200,y=50)
    

    # Label add Notitications
    addNotificationLabel = Label(settingsPanel, text="Add Notifications", font=("Sans Serif", 15, "bold"), fg="#000000")
    addNotificationLabel.place(x=50,y=0)
    
    
    # Entry add Notifications
    addNotificationEntry = Entry(settingsPanel)
    addNotificationEntry.place(x=300,y=5)


    # Label Change Password
    pwdChangelbl = Label(settingsPanel, text="Change Password", font=("Sans Serif", 15, "bold"), fg="#000000")
    pwdChangelbl.place(x=50,y=50)


    # Entry Change Password
    pwdChangeEntry = Entry(settingsPanel)
    pwdChangeEntry.place(x=300,y=55)


    # Label Change Email
    emailChangelbl = Label(settingsPanel, text="Change Email", font=("Sans Serif", 15, "bold"), fg="#000000")
    emailChangelbl.place(x=50,y=100)
    
    
    # Entry Change Email
    emailChangeEntry = Entry(settingsPanel)
    emailChangeEntry.place(x=300,y=105)


    # Defining Buttons to apply changes
    applyChangesName = Button(settingsPanel, text="Apply Changes", width=12, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    applyChangesPwd = Button(settingsPanel, text="Apply Changes", width=12, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    applyChangesMail = Button(settingsPanel, text="Apply Changes", width=12, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    
    # Place buttons
    applyChangesName.place(x=500,y=0)
    applyChangesPwd.place(x=500,y=50)
    applyChangesMail.place(x=500,y=100)

    
    
    

# Register Window
# Function to allow user to register in the app
def register():
    
    panelRegister = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500) 
    panelRegister.place(x=200,y=50)
   
    # Temporary Variables - to retrieve them later - keyword to execute that task: .get()
    name_regist_temp = StringVar()
    age_regist_temp = StringVar()
    email_regist_temp = StringVar()
    password_regist_temp = StringVar()
    user_type = StringVar()
    password_confirmation = StringVar()
    # Set User by Default as Type of  
    user_type.set('user')
    
    


    # Register Components
    # Name Label
    name_registerlbl = Label(panelRegister, text="Name", font= ("Sans Serif", 18), fg="#000")
    name_registerlbl.place(x=350,y=80)
    
    
    # Name Entry
    name_register_entry = Entry(panelRegister, textvariable = name_regist_temp)
    name_register_entry.place(x=480,y=85)
    
    
    # Age Label
    age_registerlbl = Label(panelRegister, text="Age", font=("Sans Serif", 18), fg="#000")
    age_registerlbl.place(x=350, y=130)
    
    
    # Age Entry
    age_register_entry = Entry(panelRegister, textvariable = age_regist_temp)
    age_register_entry.place(x=480,y=135)
    
    
    # Email Label
    email_lbl = Label(panelRegister, text="Email", font= ("Sans Serif", 18), fg="#000")
    email_lbl.place(x=350,y=180)
    
    
    # Email Entry
    email_entry = Entry(panelRegister, textvariable= email_regist_temp)
    email_entry.place(x= 480,y= 185)
    
    
    # Password Label
    password_registerlbl = Label(panelRegister, text="Password", font= ("Sans Serif", 18), fg="#000")
    password_registerlbl.place(x=350,y=230)


    # Password Entry
    password_entry = Entry(panelRegister, show="*", textvariable = password_regist_temp)
    password_entry.place(x=480,y=235)

    # Password Confirmation Label
    password_confirmationlbl = Label(panelRegister, text="Confirm", font= ("Sans Serif", 18), fg="#000")
    password_confirmationlbl.place(x=350,y=280)
    
    # Password Confirmation Entry
    password_confirmation_entry = Entry(panelRegister, show="*", textvariable = password_confirmation)
    password_confirmation_entry.place(x=480,y=285)

    # LabelFrame for CheckButtons
    lblFrame_user = LabelFrame(panelRegister, text="Type of User:",  width=120, height=70, relief="sunken", bd="3", fg="black")
    lblFrame_user.place(x= 350,y=350)
    

    # Type of User Confirmation
    # User
    cb1 = Radiobutton(lblFrame_user, text="User", variable= user_type, value= "user")
    cb1.place(x=0,y=0) 
    
    
    # Admin
    cb2 = Radiobutton(lblFrame_user, text="Admin", variable= user_type, value= "admin")
    cb2.place(x=0,y=20)


    submit_register_btn = Button(panelRegister, text="Submit", state="active", width=7, height=3, font=("Sans Serif", 12, "bold"), fg="#000000", command= lambda: verification(name_regist_temp.get(), age_regist_temp.get(), email_regist_temp.get(), password_regist_temp.get(), password_confirmation.get(), user_type.get())) # lambda function to call the function verification
    submit_register_btn.place(x=550,y=350)



# Login Window
# Function to allow user to sign up and access the app
def login():
    
    
    loginPaned = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    loginPaned.place(x=200,y=50)
    
    
    # Temporary Values
    login_name_temp = StringVar()
    login_password_temp = StringVar()
    

    
    #login_window.focus_force() # Forces the focus to the current window
    #login_window.grab_set() # Directs all events to the active window


    # Login Components
    # Name Label 
    name_loginlbl = Label(loginPaned, text="Name", font=("Sans Serif", 20), fg="#000")
    name_loginlbl.place(x=80,y=50)

    # Name Entry
    name_login_entry = Entry(loginPaned, textvariable = login_name_temp)
    name_login_entry.place(x=250,y=60)

    # Password Label
    password_loginlbl = Label(loginPaned, text="Password", font=("Sans Serif", 20), fg="#000")
    password_loginlbl.place(x=80,y=100)    
    
    # Password Entry
    password_login_entry = Entry(loginPaned, show="*", textvariable = login_password_temp)
    password_login_entry.place(x=250,y=110)


    # Login Button
    login_button = Button(loginPaned, text="Login", font=('Sans Serif', 12, "bold"),width=4, command= lambda: login_session(login_name_temp.get(), login_password_temp.get()))
    login_button.place(x=350,y=150)



# Login Session
# Function that is going to be executed after the login is successfully done
# To decide if the menu is going to be created within this function
def login_session():
    pass    
    
    
    
    
    
    
def home_menu():
    # Main Window Components
    
    homePanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    homePanel.place(x=200,y=50)
    
    # Name Label
    namelbl = Label(homePanel, text="Name", font= ("Sans Serif", 20), fg="#000")
    namelbl.place(x=150,y=100)


    # Name Entry
    name_Entry = Entry(homePanel) # variable =
    name_Entry.place(x=350,y=110)


    # Password Label
    passwordlbl = Label(homePanel, text="Password", font= ("Sans Serif", 20), fg="#000")
    passwordlbl.place(x=150,y=150)


    # Password Entry
    password_Entry = Entry(homePanel) # variable =
    password_Entry.place(x=350,y=150)


    # Login Button
    login_btn = Button(homePanel, text = 'Login', font=('Sans Serif', 16, "bold"),width=6, command = login)
    login_btn.place(x=350,y=250)


    # Register Button
    register_btn = Button(homePanel, text = 'Register', font = ('Sans Serif', 16, "bold"),width = 6, command = register)
    register_btn.place(x=200,y=250)
        
    
    


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
main.resizable(0,0) # Disable resizing of the app
main.configure() # Background Configurations - COLOR TO BE DECIDE LATER ################


# Side Bar Settings
# For minimum and maximum size of the side bar
side_min = 100
side_max = 200

expansion = side_min # To expand the side bar

expanded = False # To check if the side bar is expanded or not


# Function to grow the side bar to the maximum size
def grow_sidebar():
    global expansion, expanded
    
    expansion += 10 # To increase the width of the side bar
    repeat = main.after(5, grow_sidebar) # To repeat the function every 5 miliseconds
    frame.config(width=expansion) # To change the width of the side bar to the new width
    
    if expansion >= side_max:
        expanded = True
        main.after_cancel(repeat) # after_cancel() is used to cancel the function after it has been called
        colorize()

# Function to shrink the side bar to the minimum size
def shrink_sidebar():
    global expansion, expanded
    
    expansion -= 10 # To decrease the width of the side bar
    repeat = main.after(5, shrink_sidebar) # To repeat the function every 5 miliseconds
    frame.config(width=expansion) # To change the width of the side bar to the new width
    
    if expansion <= side_min:
        expanded = False
        main.after_cancel(repeat) # after_cancel() is used to cancel the function after it has been called
        colorize()

# Function to change the color of the text and images of the side bar buttons
def colorize(): 
    if expanded == True:
        home_button_icon.config(text="Home", image="", font=(10), bg="red")
        catalog_button_icon.config(text="To Do List", image="", font=(10), bg="red")
        notifications_button_icon.config(text="Notifications", image="", font=(10), bg="red")
        favorites_button_icon.config(text="Favorites", image="", font=(10), bg="red")
        profile_button_icon.config(text="Profile", image="", font=(10), bg="red")
        settings_button_icon.config(text="Settings", image="", font=(10), bg="red")
        
    # If the side bar is not expanded then the images are going to be displayed
    else:
        home_button_icon.config(text="Home", image= homeImg, font=(10), bg="red")
        catalog_button_icon.config(text="To Do List", image= catalogImg, font=(10), bg="red")
        notifications_button_icon.config(text="Notifications", image= notificationsImg, font=(10), bg="red")
        favorites_button_icon.config(text="Favorites", image= favoritesImg, font=(10), bg="red")
        profile_button_icon.config(text="Profile", image= profileImg, font=(10), bg="red")
        settings_button_icon.config(text="Settings", image= settingsImg, font=(10), bg="red")



main.update()
# Frame of the window without action
frame = Frame(main, bg='red', width=100, height=main.winfo_height())
frame.place(x=0,y=0)


# Left Frame of the main Window
# Images
homeImg = PhotoImage(file = "Images/home.png")
catalogImg = PhotoImage(file = "Images/catalog.png")
notificationsImg = PhotoImage(file = "Images/notification.png")
favoritesImg = PhotoImage(file="Images/favorites.png")
profileImg = PhotoImage(file="Images/profile.png")
settingsImg = PhotoImage(file = "Images/settings.png")


# Side Bar Buttons
home_button_icon = Button(frame, image = homeImg, bg="red", relief="flat", command = home_menu)
catalog_button_icon = Button(frame, image=catalogImg, bg="red", relief="flat", command = catalog)
notifications_button_icon = Button(frame, image = notificationsImg, bg="red", relief="flat", command = notifications)
favorites_button_icon = Button(frame, image=favoritesImg, bg="red", relief="flat", command = favorites)
profile_button_icon = Button(frame, image=profileImg, bg="red", relief="flat", command = profile_Menu)
settings_button_icon = Button(frame, image=settingsImg, bg="red", relief="flat", command = settings)

# Placing the buttons of the side bar
home_button_icon.place(x=20, y=20)
catalog_button_icon.place(x=20, y=90)
notifications_button_icon.place(x=20, y=160)
favorites_button_icon.place(x=20, y=230)
profile_button_icon.place(x=20, y=300)
settings_button_icon.place(x=20, y=370)



# Binding the mouse to the side bar to expand and shrink it when the mouse is over it
# The binding function is used to deal with events, we use it with the frame component
frame.bind("<Enter>", lambda event: grow_sidebar())
frame.bind("<Leave>", lambda event: shrink_sidebar())


# Image - To Be Decided



home_menu()

# Main Window Loop
main.mainloop()