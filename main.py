from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from datetime import datetime as dt
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
        
    panelCatalog = PanedWindow(main, relief="sunken", borderwidth=2 , width= 600, height=450)
    panelCatalog.place(x=220,y=20)

    # Entry Label - To Do List
    cataloglbl = Label(panelCatalog, text="To Do List", font=("Sans Serif", 20, "bold"), fg="#000")
    cataloglbl.place(x=30, y=25)
    
    # Categoria
    categoria = Label(panelCatalog, text="Category", font=("Sans Serif", 14), fg="#000000")
    categoria.place(x=300, y=80)
    # Select Categoria
    categorias = ".\\Files\\categorias.txt"
    categoriasList = []
    f = open(categorias, 'r', encoding='utf-8')
    for line in f:
        categoriasList.append(line.strip())
    f.close()
    global selectCategoria
    selectCategoria = Combobox(panelCatalog, values=categoriasList, width=20)
    selectCategoria.place(x=280, y=115)
    
    # Filter Button
    filterTask = Button(panelCatalog, text="Ver", width=7, height=3, font=("Sans Serif", 10, "bold"), fg="#000000", command=filterTasks)
    filterTask.place(x=450, y=80)
    
    # Entry Label - To Do List
    addTasksLbl = Label(panelCatalog, text="Add some tasks here", font=("Sans Serif", 14), fg="#000")
    addTasksLbl.place(x=30, y=80)
    # Insert Task Entry
    global insertTask
    insertTask = StringVar()
    addTask = Entry(panelCatalog, width=20, textvariable=insertTask)
    addTask.place(x=30, y=115)
    # Button Add Task
    addTask = Button(panelCatalog, text="Add", width=4, font=("Sans Serif", 10, "bold"), fg="#000000", command=lambda: addTaskBox(userName.get(), insertTask.get(), selectCategoria.get()))
    addTask.place(x=168, y=110)

    # Delete Task Button
    deleteTask = Button(panelCatalog, text="Delete Task", width=16, font=("Sans Serif", 10, "bold"), fg="#000000", command = deleteSelectedTask)
    deleteTask.place(x=45,y=190)

    # Sort ASC Button
    sortAscTask = Button(panelCatalog, text="Sort ASC", width=16, height=1, font=("Sans Serif", 10, "bold"), fg="#000000", command=sort)
    sortAscTask.place(x=45,y=235)

    # Sort DESC Button
    sortDescTask = Button(panelCatalog, text="Sort DESC", width=16, height=1, font=("Sans Serif", 10, "bold"), fg="#000000")
    sortDescTask.place(x=45,y=280)
    
    # Delete All Button
    deleteAllTask = Button(panelCatalog, text="Delete All", width=16, height=1, font=("Sans Serif", 10, "bold"), fg="#000000", command=deleteAll)
    deleteAllTask.place(x=45,y=325)

    # Add to favorites Button
    addfavoritesButton = Button(panelCatalog, text="Add to Favorites", width=16, font=("Sans Serif", 10, "bold"), fg="#000000")
    addfavoritesButton.place(x=45,y=370)
    
    # TVTodo
    global treeTodo
    treeTodo = ttk.Treeview(panelCatalog, height = 10, selectmode = "browse", columns = ("ToDo"), show = "headings")
    treeTodo.column("ToDo", width = 120, anchor = "w")
    treeTodo.heading("ToDo", text = "To Do")
    treeTodo.place(x=210, y=170)
    treeTodo.delete(*treeTodo.get_children())
        
    # TVDoing
    global treeDoing
    treeDoing = ttk.Treeview(panelCatalog, height = 10, selectmode = "browse", columns = ("Doing"), show = "headings")
    treeDoing.column("Doing", width = 120, anchor = "w")
    treeDoing.heading("Doing", text = "Doing")
    treeDoing.place(x=330, y=170)
    treeDoing.delete(*treeDoing.get_children())
    
    # TVDone
    global treeDone
    treeDone = ttk.Treeview(panelCatalog, height = 10, selectmode = "browse", columns = ("Done"), show = "headings")
    treeDone.column("Done", width = 120, anchor = "w")
    treeDone.heading("Done", text = "Done")
    treeDone.place(x=450, y=170)
    treeDone.delete(*treeDone.get_children())
    
    btnDoing = Button(panelCatalog, text="Doing", command=estadoDoing)
    btnDoing.place(x=350, y=410)
    btnDone = Button(panelCatalog, text="Done", command=estadoDone)
    btnDone.place(x=410, y=410)    
    filterTasks()
    
    
def sort():
    
    treeDone.heading("Done", command=lambda: treeview_sort_column(treeDone, 0, False))

    
def filterTasks():
    
    treeTodo.delete(*treeTodo.get_children())
    treeDoing.delete(*treeDoing.get_children())
    treeDone.delete(*treeDone.get_children())
    
    # Add to the treeview 
    listaTarefas = ".\\users\\" + userName.get() + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[1] == selectCategoria.get() and campos[2] == "todo":
            treeTodo.insert("", "end", values = (campos[0]))   
        if campos[1] == selectCategoria.get() and campos[2] == "doing": 
            treeDoing.insert("", "end", values = (campos[0]))
        if campos[1] == selectCategoria.get() and campos[2] == "done": 
            treeDone.insert("", "end", values = (campos[0]))
            
    
def estadoDoing():
    
    row_idDoing = treeTodo.focus()
    linhaDoing = treeTodo.item(row_idDoing)
    nameTaskDoing = linhaDoing["values"][0]
    
    listaTarefas = ".\\users\\" + userName.get() + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[0] == nameTaskDoing and campos[2] == "todo":
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open (listaTarefas, "a") as fListaDoing:
                linhaAlteradaDoing= ("\n" + nameTaskDoing + ";" + selectCategoria.get() + ";" + "doing" + ";")
                fListaDoing.write(linhaAlteradaDoing)
                fListaDoing.close()
                with open(listaTarefas, "r") as fListaDoing:
                    lines = fListaDoing.readlines()
                    with open(listaTarefas, "w") as fListaDoing:
                        for line in lines:
                            if line.strip("\n") != "":
                                fListaDoing.write(line)
      
def estadoDone():
    
    row_idDone = treeDoing.focus()
    linhaDone = treeDoing.item(row_idDone)
    global nameTaskDone
    nameTaskDone = linhaDone["values"][0]
    
    listaTarefas = ".\\users\\" + userName.get() + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[0] == nameTaskDone and campos[2] == "doing":
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open (listaTarefas, "a") as fListaDoing:
                linhaAlteradaDone = ("\n" + nameTaskDone + ";" + selectCategoria.get() + ";" + "done" + ";")
                fListaDoing.write(linhaAlteradaDone)
                fListaDoing.close()
                with open(listaTarefas, "r") as fListaDoing:
                    lines = fListaDoing.readlines()
                    with open(listaTarefas, "w") as fListaDoing:
                        for line in lines:
                            if line.strip("\n") != "":
                                fListaDoing.write(line)
    
    
def deleteSelectedTask():
    
    row_idTodo = treeTodo.focus()
    linhaTodo = treeTodo.item(row_idTodo)
    linhaSelecionadaTodo = linhaTodo["values"]
    
    row_idDoing = treeDoing.focus()
    linhaDoing = treeDoing.item(row_idDoing)
    linhaSelecionadaDoing = linhaDoing["values"]
    
    row_idDone = treeDone.focus()
    linhaDone = treeDone.item(row_idDone)
    linhaSelecionadaDone = linhaDone["values"]
   
    listaA = []
    if linhaSelecionadaTodo != "":
       listaA.append(linhaSelecionadaTodo)
    if linhaSelecionadaDoing != "":
        listaA.append(linhaSelecionadaDoing)
    if linhaSelecionadaDone != "":   
        listaA.append(linhaSelecionadaDone)
    taskRemove = str(listaA[0])
    taskRemoveA = taskRemove.replace("[", "").replace("]", "").replace("'", "")
    
    listaTarefas = ".\\users\\" + userName.get() + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[0] == taskRemoveA:
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line)
                            


    
    
def deleteAll():
    
    treeTodo.delete(*treeTodo.get_children())
    treeDoing.delete(*treeDoing.get_children())
    treeDone.delete(*treeDone.get_children())
    
    listaTarefas = ".\\users\\" + userName.get() + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[1] == selectCategoria.get():
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line)
    
    
    

   

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


    

    
    

   
    
    

    
    
    

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
    activity = StringVar() # For the activity data
    
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
    activitylbox = Combobox(favoritesPanel, valuess=["To Do", "Doing", "Done"], width=20, textvariable= activity)
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
    commentBtn = Button(favoritesPanel, text="Comment", width=6, height=2, font=("Sans Serif", 10, "bold"), fg="#000000", command= lambda: insertComment(userName.get(), content.get(), activity.get(), commentlbox))
    commentBtn.place(x=600, y=140)

# FUNCTION PROFILE MENU 
def profile_Menu():
    
    global users_file
    users_file = ".\\Files\\users.txt"
    # users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

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
    
    panelRegister = PanedWindow(main, relief="raised", width=500, height=300) 
    panelRegister.place(x=300,y=100)
   
    # Temporary Variables - to retrieve them later - keyword to execute that task: .get()
    global UserNameR
    userNameR = StringVar()
    global userAge 
    userAge = StringVar()
    global userMail
    userMail = StringVar()
    global userPwdR
    userPwdR = StringVar()
    global userPwdCheck
    userPwdCheck = StringVar()
    global userType
    userType = StringVar()
    # Set User by Default as Type of  
    userType.set('user')
    
    # Register Components
    # Name Label
    name_registerlbl = Label(panelRegister, text="Name", font= ("Sans Serif", 14), fg="#000")
    name_registerlbl.place(x=80,y=20)
    # Name Entry
    name_register_entry = Entry(panelRegister, textvariable=userNameR)
    name_register_entry.place(x=80,y=50)
    
    # Age Label
    age_registerlbl = Label(panelRegister, text="Birth date", font=("Sans Serif", 14), fg="#000")
    age_registerlbl.place(x=280, y=20)
    # Age Entry
    age_register_entry = Entry(panelRegister, textvariable=userAge)
    age_register_entry.place(x=280, y=50)
    
    # Email Label
    email_lbl = Label(panelRegister, text="Email", font= ("Sans Serif", 14), fg="#000")
    email_lbl.place(x=80, y=85)
    # Email Entry
    email_entry = Entry(panelRegister, textvariable= userMail, width=54)
    email_entry.place(x=80, y=115)
    
    # Password Label
    password_registerlbl = Label(panelRegister, text="Password", font= ("Sans Serif", 14), fg="#000")
    password_registerlbl.place(x=80,y=150)
    # Password Entry
    password_entry = Entry(panelRegister, show="*", textvariable=userPwdR)
    password_entry.place(x=80,y=180)

    # Password Confirmation Label
    password_confirmationlbl = Label(panelRegister, text="Confirm", font= ("Sans Serif", 14), fg="#000")
    password_confirmationlbl.place(x=280,y=150)
    # Password Confirmation Entry
    password_confirmation_entry = Entry(panelRegister, show="*", textvariable = userPwdCheck)
    password_confirmation_entry.place(x=280,y=180)

    # LabelFrame for CheckButtons
    lblFrame_user = LabelFrame(panelRegister, text="Type of User",  width=160, height=50, relief="sunken", bd="3", fg="black")
    lblFrame_user.place(x=80, y=220)
    
    # Type of User Confirmation
    # User
    cb1 = Radiobutton(lblFrame_user, text="User", variable= userType, value= "user")
    cb1.place(x=15, y=3) 
    # Admin
    cb2 = Radiobutton(lblFrame_user, text="Admin", variable= userType, value= "admin")
    cb2.place(x=80,y=3)

    # lambda function to call the function verification
    submit_register_btn = Button(panelRegister, text="Register", state="active", width=10, font=("Sans Serif", 16, "bold"), fg="#000000", command= lambda: authentication(userNameR.get(), userAge.get(), userMail.get(), userPwdR.get(), userPwdCheck.get(), userType.get(), panelRegister))
    submit_register_btn.place(x=270,y=225)

def login():
    
    global userName
    global userPwd
    
    # StringVars
    userName = StringVar()
    userPwd = StringVar()
    
    homePanelBG = PanedWindow(main, width=1000, height=500)
    homePanelBG.place(x=200,y=0)
    
    # Main Window Components
    homePanel = PanedWindow(main, relief="raised", width=500, height=300)
    homePanel.place(x=300,y=100)
    
    # Name Label
    namelbl = Label(homePanel, text="Name", font= ("Sans Serif", 16), fg="#000")
    namelbl.place(x=140,y=50)
    # Name Entry
    name_Entry = Entry(homePanel, textvariable=userName)
    name_Entry.place(x=260,y=55)

    # Password Label
    passwordlbl = Label(homePanel, text="Password", font= ("Sans Serif", 16), fg="#000")
    passwordlbl.place(x=140,y=100)
    # Password Entry
    password_Entry = Entry(homePanel, show="*", textvariable=userPwd)
    password_Entry.place(x=260,y=105)

    # Login Button
    login_btn = Button(homePanel, text = 'Login', font=('Sans Serif', 16, "bold"), width=10, command= lambda: verification(userName.get(), userPwd.get(), homePanel, catalog))
    login_btn.place(x=200,y=170)

    # Register Button
    register_btn = Button(homePanel, text = 'Register', font = ('Sans Serif', 12),width=8, command=register)
    register_btn.place(x=220,y=240)
   
# Function to display the current time
def clock():
    # Label for the clock
    clocklbl = Label(main, font=("Sans Serif", 15), fg="#000")
    clocklbl.place(x=880,y=20)
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

# To expand the side bar
expansion = side_min 

# To check if the side bar is expanded or not
expanded = False 

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
        catalog_button_icon.config(text="To Do List", bg="red" , image="", font=(10))
        notifications_button_icon.config(text="Notifications", bg="red" , image="", font=(10))
        favorites_button_icon.config(text="Favorites", bg="red" , image="", font=(10))
        profile_button_icon.config(text="Profile", bg="red" , image="", font=(10))
        settings_button_icon.config(text="Settings", bg="red" , image="", font=(10))
        home_button_icon.config(text="Sair", bg="red" , image="", font=(10))
        
    # If the side bar is not expanded then the images are going to be displayed
    else:
        catalog_button_icon.config(text="To Do List", image= catalogImg, font=(10))
        notifications_button_icon.config(text="Notifications", image= notificationsImg, font=(10))
        favorites_button_icon.config(text="Favorites", image= favoritesImg, font=(10))
        profile_button_icon.config(text="Profile", image= profileImg, font=(10))
        settings_button_icon.config(text="Settings", image= settingsImg, font=(10))
        home_button_icon.config(text="Sair", image= homeImg, font=(10))

main.update()

# Frame of the window without action
frame = Frame(main, bg='red', width=100, height=main.winfo_height())
frame.place(x=0,y=0)

# Left Frame of the main Window
# Images
catalogImg = PhotoImage(file = "Images/catalog.png")
notificationsImg = PhotoImage(file = "Images/notification.png")
favoritesImg = PhotoImage(file="Images/favorites.png")
profileImg = PhotoImage(file="Images/profile.png")
settingsImg = PhotoImage(file = "Images/settings.png")
homeImg = PhotoImage(file = "Images/home.png")

# Side Bar Buttons
catalog_button_icon = Button(frame, image=catalogImg, bg="red", relief="flat", command = catalog)
catalog_button_icon.place(x=20, y=20)
notifications_button_icon = Button(frame, image = notificationsImg, bg="red", relief="flat", command = notifications)
notifications_button_icon.place(x=20, y=90)
favorites_button_icon = Button(frame, image=favoritesImg, bg="red", relief="flat", command = favorites)
favorites_button_icon.place(x=20, y=160)
profile_button_icon = Button(frame, image=profileImg, bg="red", relief="flat", command = profile_Menu)
profile_button_icon.place(x=20, y=230)
settings_button_icon = Button(frame, image=settingsImg, bg="red", relief="flat", command = settings)
settings_button_icon.place(x=20, y=300)
home_button_icon = Button(frame, image = homeImg, bg="red", relief="flat", command=login)
home_button_icon.place(x=20, y=370)

# Binding the mouse to the side bar to expand and shrink it when the mouse is over it
# The binding function is used to deal with events, we use it with the frame component
frame.bind("<Enter>", lambda event: grow_sidebar())
frame.bind("<Leave>", lambda event: shrink_sidebar())

# Function to display the home menu
login()

# Function to display the current time
clock()

# Main Window Loop
main.mainloop()