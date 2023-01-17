from tkinter import *
from tkinter import ttk
from datetime import datetime 
from tkinter import messagebox
from tkinter.ttk import Combobox
from time import strftime
import os


# Import the other files
from users import *
from todolist import *
from notifications import *
from favorites import *
from profileSettings import *
from settings import *



def catalog():
    
    # Global Vars
    global values
    
    
    # Temporary Vars
    insertTask = StringVar()
    
    
    panelCatalog = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    panelCatalog.place(x=200,y=50)


    # Entry Label - To Do List
    cataloglbl = Label(panelCatalog, text="To Do List", font=("Sans Serif", 20, "bold"), fg="#000")
    cataloglbl.place(x=0, y=0)


    # List Box to visualize the current info
    todolistBox = Listbox(panelCatalog, width=50, height=15, selectmode= "single", selectbackground="green")
    todolistBox.place(x=250,y=120)
    

    # Number os Tasks Label
    numberTasks= Label(panelCatalog, text="Number of Tasks: ", font=("Sans Serif", 10, "bold"), fg="#000000")
    numberTasks.place(x=250,y=50)
    

    # Insert Task Entry
    addTask = Entry(panelCatalog, width=30, textvariable= insertTask)
    addTask.place(x=250,y=90)
    
    
    # Button Add Task
    addTask = Button(panelCatalog, text="Add Task", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: addTaskBox(insertTask.get(), todolistBox))
    addTask.place(x=30,y=80)


    # Delete Task Button
    deleteTask = Button(panelCatalog, text="Delete Task", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: deleteSelectedTask(todolistBox))
    deleteTask.place(x=30,y=140)


    # Sort ASC Button
    sortAscTask = Button(panelCatalog, text="Sort ASC", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: sortAsc(todolistBox))
    sortAscTask.place(x=30,y=200)


    # Sort DESC Button
    sortDescTask = Button(panelCatalog, text="Sort DESC", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: sortDesc(todolistBox))
    sortDescTask.place(x=30,y=260)
    
    
    # Delete All Button
    deleteAllTask = Button(panelCatalog, text="Delete All", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command=lambda: cleanBox(todolistBox))
    deleteAllTask.place(x=30,y=320)


    # Add to favorites Button
    addfavoritesButton = Button(panelCatalog, text="Add to\n Favorites", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    addfavoritesButton.place(x=30,y=380)
    

    # Filter Button
    filterTask = Button(panelCatalog, text="Filter", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
    filterTask.place(x=500,y=5)
    
    

    # Section To filter the state of the tasks
    values = ["To Do", "Doing", "Done"]
    selectState = Combobox(panelCatalog, values=values, width=20)
    selectState.place(x=250,y=10)
    
    

# FUNCTION NOTIFICATIONS MENU
def notifications():
    
    # Paned Window Notifications
    notificationsPanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    notificationsPanel.place(x=200,y=50)
    
    
    seeNotifications = Label(notificationsPanel, text="See Notifications", font=("Sans Serif", 20, "bold"), fg="#000000")
    seeNotifications.place(x=50,y=50)


    # Button to open notifications
    openNotifications = Button(notificationsPanel, text="Open", width=8, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command=lambda: send_Info())    
    openNotifications.place(x=350,y=40)
    
    
    # Label to keep track of notifications
    notificationslbl = Label(notificationsPanel, text="You've got    Notifications", font=("Sans Serif", 20, "bold"), fg="#000000")
    notificationslbl.place(x=50,y=150)


    # TO delete
    notificationsNumber = Label(notificationsPanel, text="3", font=("Sans Serif", 20, "bold"), fg="red")
    notificationsNumber.place(x=220,y=150)




# FUNCTION FAVORITES MENU
def favorites():
    
    # String Var
    content = StringVar() # For the comments data
    
    
    # Paned Window Favorites
    favoritesPanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    favoritesPanel.place(x=200,y=50)
    
    
    # Label to select the favorite category
    seeFavorites = Label(favoritesPanel, text="See Favorites", font=("Sans Serif", 20, "bold"), fg="#000000")
    seeFavorites.place(x=0,y=0)
    
    # ComboBox to select the favorite category
    favoritesCombo = Combobox(favoritesPanel, values=["To Do", "Doing", "Done"], width=20)
    favoritesCombo.place(x=250,y=5)


    # Select Activity Label
    activitylbl = Label(favoritesPanel, text="Select a Activity", font=("Sans Serif", 20, "bold"), fg="#000000")
    activitylbl.place(x=0,y=70) 


    # Activity Listbox
    activitylbox = Combobox(favoritesPanel, values=["To Do", "Doing", "Done"], width=20)
    activitylbox.place(x=300,y=75)



    # Comment on a favorite
    commentlbl = Label(favoritesPanel, text="Leave a Comment...", font=("Sans Serif", 15, "bold"), fg="#000000")
    commentlbl.place(x=0,y=150)
    
    
    # Comment Listbox
    commentlbox = Listbox(favoritesPanel, width=50, height=10, selectmode= "single")
    commentlbox.place(x=100,y=200)
    
    
    
    # Add a comment Entry
    commentEntry = Entry(favoritesPanel, width=30, textvariable = content)
    commentEntry.place(x=300,y=150)


    # Add a comment Button
    commentBtn = Button(favoritesPanel, text="Comment", width=6, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: insertComment(userName.get(), content.get()))
    commentBtn.place(x=600, y=140)





# FUNCTION PROFILE MENU 
def profile_Menu():
    
    global users_file
    users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

    file = open(users_file, 'r', encoding='utf-8')
    line = file.readlines()
    users_file = line[0].split(";")
    file.close()
    
    """
    [0] - Name
    [1] - Age
    [2] - Email
    [3] - Password
    [4] - Password Confirmation
    [5] - Type of User
    """
    
    # Paned Window Profile
    profilePanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    profilePanel.place(x=200,y=50)
    
    
    # Username Info
    usernameInfo = Label(profilePanel, text="Username: {0}".format(users_file[0]), font=("Sans Serif", 15, "bold"), fg="#000000")
    usernameInfo.place(x=50,y=0)
    
    # Email Info
    emailInfo = Label(profilePanel, text="Email: {0}".format(users_file[2]), font=("Sans Serif", 15, "bold"), fg="#000000")
    emailInfo.place(x=50,y=50)
    
    
    # Password Info
    passwordInfo = Label(profilePanel, text="Password: {0}".format(users_file[3]), font=("Sans Serif", 15, "bold"), fg="#000000")
    passwordInfo.place(x=50,y=100)
    
    check = Checkbutton(profilePanel, text="Show Password", font=("Sans Serif", 15, "bold"), fg="#000000")
    check.place(x=50,y=150)
    
    
    
    # Section to Change the user info
    # Label to change name
    nameChangeLabel = Label(profilePanel, text="Change Name", font=("Sans Serif", 15, "bold"), fg="#000000")
    nameChangeLabel.place(x=50,y=250)
    
    
    # Entry to change name
    nameChangeEntry = Entry(profilePanel)
    nameChangeEntry.place(x=300,y=255)


    # Label Change Password
    pwdChangelbl = Label(profilePanel, text="Change Password", font=("Sans Serif", 15, "bold"), fg="#000000")
    pwdChangelbl.place(x=50,y=350)


    # Entry Change Password
    pwdChangeEntry = Entry(profilePanel)
    pwdChangeEntry.place(x=300,y=355)


    # Label Change Email
    emailChangelbl = Label(profilePanel, text="Change Email", font=("Sans Serif", 15, "bold"), fg="#000000")
    emailChangelbl.place(x=50,y=300)
    
    
    # Entry Change Email
    emailChangeEntry = Entry(profilePanel)
    emailChangeEntry.place(x=300,y=305)


    # Defining Buttons to apply changes
    applyChanges = Button(profilePanel, text="Apply", width=12, height=2, font=("Sans Serif", 10, "bold"), fg="#000000")
 
 
    # Place buttons
    applyChanges.place(x=550,y=330)





def settings():
    
    # String Var
    # Notifications
    titleNotification = StringVar()
    messageNotification = StringVar()
    timerNotification = StringVar()
    
    # Categories
    categories = StringVar()
    
    
    # Paned Window Settings
    settingsPanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    settingsPanel.place(x=200,y=50)
    
    
    # Changes Section
    # Label to add categories
    addCategorieslbl = Label(settingsPanel, text="Add Categories: ", font=("Sans Serif", 15, "bold"), fg="#000000")
    addCategorieslbl.place(x=50,y=0)
    
    
    # ComboBox to add categories
    addCategoriesCombo = Entry(settingsPanel, textvariable = categories)
    # VERY IMPORTANT - NEED TO ADD THE VALUES
    addCategoriesCombo.place(x=300,y=5)
    
    
    # Button to add categories
    addCategoriesButton = Button(settingsPanel, text="Add", width=5, height=1, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: settingsCategories(categories.get())) 
    addCategoriesButton.place(x=500,y=0)
    
    
    # Button
    removeCategoriesButton = Button(settingsPanel, text="Remove", width=5, height=1, font=("Sans Serif", 10, "bold"), fg="#000000")
    removeCategoriesButton.place(x=600,y=0)
    
    
    # Label add notifications
    addNotifications = Label(settingsPanel, text="Notifications Title", font=("Sans Serif", 15, "bold"), fg="#000")
    addNotifications.place(x=50, y=70)
    
    
    # Entry to notification For the Title
    addNotificationsEntry = Entry(settingsPanel, textvariable= titleNotification)
    addNotificationsEntry.place(x=300,y=75)
    
    
    # Label for notifications label
    addMessageNotification = Label(settingsPanel, text="Message", font=("Sans Serif", 15, "bold"), fg="#000")
    addMessageNotification.place(x=50, y=120)
    
    addMessageEntry = Entry(settingsPanel, textvariable= messageNotification)
    addMessageEntry.place(x=300,y=125)
    
    # Set timer for notifications Label
    timerlbl = Label(settingsPanel, text="Set Timer (min)", font=("Sans Serif", 15, "bold"), fg="#000")
    timerlbl.place(x=50, y=170)
    
    
    # Set timer for notifications Entry
    timerEntry = Entry(settingsPanel, textvariable= timerNotification)
    timerEntry.place(x=300,y=175)


    # Button to add notifications
    addNotificationsButton = Button(settingsPanel, text="Add", width="5", height="1", font=("Sans Serif", 10, "bold"), fg="#000", command= lambda: send_Info(titleNotification.get(), messageNotification.get(), timerNotification.get()))
    addNotificationsButton.place(x=500,y=170)
    


    # Statistics Part
    # Label to show the number os tasks
    numberTasks = Label(settingsPanel, text="Number of Tasks: ", font=("Sans Serif", 12, "bold"), fg="#000000")
    numberTasks.place(x=50,y=240)
    
    # Label to show the number of categories
    numberCategory = Label(settingsPanel, text="Number of Task By Categories: ", font=("Sans Serif", 12, "bold"), fg="#000000")
    numberCategory.place(x=50,y=290)
    
    
    # Label to show the time spent on the app
    timeSpaceWeek = Label(settingsPanel, text="Activity Last week: ", font=("Sans Serif", 12, "bold"), fg="#000000")
    timeSpaceWeek.place(x=50,y=340)
    
    timeSpaceMonth = Label(settingsPanel, text="Activity Last Month: ", font=("Sans Serif", 12, "bold"), fg="#000000")
    timeSpaceMonth.place(x=50,y=390)
    
    
    
    
    

# Register Window
# Function to allow user to register in the app
def register():
    
    panelRegister = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500) 
    panelRegister.place(x=200,y=50)
   
    # Temporary Variables - to retrieve them later - keyword to execute that task: .get()
    userName = StringVar()
    userAge = StringVar()
    userMail = StringVar()
    userPwd = StringVar()
    userPwdCheck = StringVar()
    userType = StringVar()
    # Set User by Default as Type of  
    userType.set('user')
    
    


    # Register Components
    # Name Label
    name_registerlbl = Label(panelRegister, text="Name", font= ("Sans Serif", 18), fg="#000")
    name_registerlbl.place(x=150,y=50)
    
    
    # Name Entry
    name_register_entry = Entry(panelRegister, textvariable = userName)
    name_register_entry.place(x=300,y=55)
    
    
    # Age Label
    age_registerlbl = Label(panelRegister, text="Age", font=("Sans Serif", 18), fg="#000")
    age_registerlbl.place(x=150, y=90)
    
    
    # Age Entry
    age_register_entry = Entry(panelRegister, textvariable = userAge)
    age_register_entry.place(x=300,y=95)
    
    
    # Email Label
    email_lbl = Label(panelRegister, text="Email", font= ("Sans Serif", 18), fg="#000")
    email_lbl.place(x=150,y=130)
    
    
    # Email Entry
    email_entry = Entry(panelRegister, textvariable= userMail)
    email_entry.place(x= 300,y= 135)
    
    
    # Password Label
    password_registerlbl = Label(panelRegister, text="Password", font= ("Sans Serif", 18), fg="#000")
    password_registerlbl.place(x=150,y=170)


    # Password Entry
    password_entry = Entry(panelRegister, show="*", textvariable = userPwd)
    password_entry.place(x=300,y=175)

    # Password Confirmation Label
    password_confirmationlbl = Label(panelRegister, text="Confirm", font= ("Sans Serif", 18), fg="#000")
    password_confirmationlbl.place(x=150,y=210)
    
    # Password Confirmation Entry
    password_confirmation_entry = Entry(panelRegister, show="*", textvariable = userPwdCheck)
    password_confirmation_entry.place(x=300,y=215)

    # LabelFrame for CheckButtons
    lblFrame_user = LabelFrame(panelRegister, text="Type of User:",  width=120, height=70, relief="sunken", bd="3", fg="black")
    lblFrame_user.place(x= 150,y=270)
    

    # Type of User Confirmation
    # User
    cb1 = Radiobutton(lblFrame_user, text="User", variable= userType, value= "user")
    cb1.place(x=0,y=0) 
    
    
    # Admin
    cb2 = Radiobutton(lblFrame_user, text="Admin", variable= userType, value= "admin")
    cb2.place(x=0,y=20)


    # lambda function to call the function verification
    submit_register_btn = Button(panelRegister, text="Submit", state="active", width=5, height=3, font=("Sans Serif", 12, "bold"), fg="#000000", command= lambda: authentication(userName.get(), userAge.get(), userMail.get(), userPwd.get(), userPwdCheck.get(), userType.get(), panelRegister))
    submit_register_btn.place(x=380,y=270)



        
    
def home_menu():
    
    global userName
    global userPwd
    
    # StringVars
    userName = StringVar()
    userPwd = StringVar()
    
    
    # Main Window Components
    homePanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    homePanel.place(x=200,y=50)
    
    # Name Label
    namelbl = Label(homePanel, text="Name", font= ("Sans Serif", 20), fg="#000")
    namelbl.place(x=150,y=100)


    # Name Entry
    name_Entry = Entry(homePanel, textvariable= userName)
    name_Entry.place(x=350,y=110)


    # Password Label
    passwordlbl = Label(homePanel, text="Password", font= ("Sans Serif", 20), fg="#000")
    passwordlbl.place(x=150,y=150)


    # Password Entry
    password_Entry = Entry(homePanel, show="*", textvariable= userPwd)
    password_Entry.place(x=350,y=150)


    # Login Button
    login_btn = Button(homePanel, text = 'Login', font=('Sans Serif', 16, "bold"),width=6, command= lambda: verification(userName.get(), userPwd.get(), homePanel, logged_Menu))
    login_btn.place(x=350,y=250)


    # Register Button
    register_btn = Button(homePanel, text = 'Register', font = ('Sans Serif', 16, "bold"),width = 6, command = register)
    register_btn.place(x=200,y=250)
        




# Function to load a UI after the users is successfully logged in
def logged_Menu():
    
    # Read the File
    users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

    file = open(users_file, 'r', encoding='utf-8')
    line = file.readlines()
    users_file = line[0].split(";")
    file.close()
    
    
    loggedPanel = PanedWindow(main, orient=HORIZONTAL, width= 800, height=500)
    loggedPanel.place(x=200,y=50)
    
    
    # Canvas for the image
    homeCanvas = Canvas(loggedPanel, width= 600, height=300)
    homeCanvas.place(x=100,y=100)
    
    
    # Place for Image to be displayed
    calendar = PhotoImage("Images/calendar.png")
    homeCanvas.create_image(0,0, image=calendar)
    
    # Label for the welcome message on the top 
    welcomelbl = Label(loggedPanel ,text="Welcome to your To Do List App {0}".format(users_file[0]), font=("Sans Serif", 20), fg="#000")
    welcomelbl.place(x=80,y=0)
    
    # Button to Log Out of the APP
    logout = Button(loggedPanel, text="Log Out", font=("Sans Serif", 12, "bold"), width=6, command= lambda: logOut(userName.get(), userPwd.get(), logged_Menu, home_menu))
    logout.place(x=650,y=350)
     
    
    
    
    
    
    
    
    
# Function to display the current time
def clock():
    
    # Label for the clock
    clocklbl = Label(main, font=("Sans Serif", 15), fg="#000")
    clocklbl.place(x=850,y=5)
    
    
    # Getting the current time
    time = strftime("%H:%M:%S")
    
    # Configure the clock label
    clocklbl.config(text=time)
    
    # After 500 miliseconds the clock function is going to be called again
    clocklbl.after(500, clock)
    


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
        home_button_icon.config(text="Home", bg="red" , image="", font=(10))
        catalog_button_icon.config(text="To Do List", bg="red" , image="", font=(10))
        notifications_button_icon.config(text="Notifications", bg="red" , image="", font=(10))
        favorites_button_icon.config(text="Favorites", bg="red" , image="", font=(10))
        profile_button_icon.config(text="Profile", bg="red" , image="", font=(10))
        settings_button_icon.config(text="Settings", bg="red" , image="", font=(10))
        
    # If the side bar is not expanded then the images are going to be displayed
    else:
        home_button_icon.config(text="Home", image= homeImg, font=(10))
        catalog_button_icon.config(text="To Do List", image= catalogImg, font=(10))
        notifications_button_icon.config(text="Notifications", image= notificationsImg, font=(10))
        favorites_button_icon.config(text="Favorites", image= favoritesImg, font=(10))
        profile_button_icon.config(text="Profile", image= profileImg, font=(10))
        settings_button_icon.config(text="Settings", image= settingsImg, font=(10))



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
home_button_icon = Button(frame, image = homeImg, bg="red", relief="flat",command = lambda: refresh(home_menu, logged_Menu))
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


# Function to display the home menu
home_menu()
# Function to display the current time
clock()

# Main Window Loop
main.mainloop()