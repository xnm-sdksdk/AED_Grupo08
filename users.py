from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
from time import strftime
import os

pastaUsers = "users"
usersGlobal = ".\\Files\\users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(userName, userPwd, homePanel, catalog):
    global logged
    
    logged = False
    
    usersGlobalFile = open(usersGlobal, "r", encoding="utf-8")
    for line in usersGlobalFile:
        campos = line.split(";")
        if userName == campos[0] and userPwd == campos[3]:
            logged = True
            success = "Welcome " + userName + "!"
            messagebox.showinfo("Login", success)
            homePanel.place_forget()
            catalog()

    if logged == False:
        messagebox.showerror("Login", "Username or password is incorrect!")
        return
        
# Function to verify if the user is registered in the app
def authentication(userNameR, userAge, userMail, userPwdR, userPwdCheck, userType, panelRegister):
    
    # verification for empty fields
    if userNameR == "" or userAge == "" or userMail == "" or userPwdR == "" or userPwdCheck == "" or userType == "":        
        messagebox.showerror("Register", "All fields are required!")
        return
    # Password verification
    if userPwdR != userPwdCheck:
        messagebox.showerror("Register", "Passwords don't match!")
        return  
    # Verification to check if email has "@" and "." and if the "@" is before the "."
    if userMail.find("@") == -1 or userMail.find(".") == -1:
        messagebox.showerror("Register", "Email does not contain '@' or '.'")
        return
    if userMail.find(".") < userMail.find("@"):
        messagebox.showerror("Register", "Email is not written correctly.")
        return
    
    
    # Verification to check if the username already exists
    usersGlobalFile = open(usersGlobal, "r", encoding="utf-8")
    for line in usersGlobalFile:
        campos = line.split(";")
        if userNameR == campos[0]:
            messagebox.showerror("Register", "Username already exists!")
            return  
        # Everything is correct append to the files
        else:
            if os.path.exists(pastaUsers):
                
                addUsersFile = os.path.join(pastaUsers, userNameR)
                os.makedirs(addUsersFile)
                
                listTodo = ".\\users\\" + userNameR + "\\list.txt"
                listTodoFile = open(listTodo, "x", encoding="utf-8") 
                listFav = ".\\users\\" + userNameR + "\\favorites.txt"
                listFavFile = open(listFav, "x", encoding="utf-8") 
                
                emailVerification = True
                time = datetime.datetime.now()
                date = time.strftime("%d/%m/%Y;%H:%M:%S")
                
                usersFile = open(usersGlobal, "a", encoding="utf-8")
                usersFileFields = "\n" + userNameR + ";" + userAge + ";" + userMail + ";" + userPwdR + ";" + userPwdCheck + ";" + userType + ";" + date + ";" + "\n"
                usersFile.write(usersFileFields)
                usersFile.close()
                messagebox.showinfo("Register", "Account has been created successfully!")
                panelRegister.place_forget()
                with open(usersGlobal, "r") as fListaDoing:
                    lines = fListaDoing.readlines()
                    with open(usersGlobal, "w") as fListaDoing:
                        for line in lines:
                            if line.strip("\n") != "":
                                fListaDoing.write(line)
                return




