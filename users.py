# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import datetime
from time import strftime
import os

# path to users.txt file
users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(userName, userPwd, homePanel, logged_Menu):
    global logged
    
    logged = False
    
    with open("/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt", "r", encoding="utf-8") as file:
        for line in file:
            params = line.split(";")
            if userName == params[0] and userPwd == params[3]:
                logged = True
                success = "Welcome " + userName + "!"
                messagebox.showinfo("Login", success)
                homePanel.place_forget()
                logged_Menu()
                return

            
                


        if logged == False:
            messagebox.showerror("Login", "Username or password is incorrect!")
            return
        
        
        
        

# Function to verify if the user is registered in the app
def authentication(userName, userAge, userMail, userPwd, userPwdCheck, userType, panelRegister):
    
    all_profiles = os.listdir()
    print(all_profiles) # For back-end verifications
    
    
    # verification for empty fields
    if userName == "" or userAge == "" or userMail == "" or userPwd == "" or userPwdCheck == "" or userType == "":        
        messagebox.showerror("Register", "All fields are required!")
        return
    
    
    for name_check in all_profiles:
        # Name verification
        if userName == name_check:
            messagebox.showerror("Register", "An account with that name already exists!")
            return
        
        # Age verification
        #elif userAge != int():
        #    messagebox.showerror("Register", "Age must be a number!")
        #    return
        
        
        # Size of password verification
        #elif len(userPwd) <= 5:
         #   messagebox.showerror("Register", "Password must be at least 6 characters long!")
          #  return
        
        
        # Password verification
        elif userPwd != userPwdCheck:
            messagebox.showerror("Register", "Passwords don't match!")
            return
            
        # Verification to check if email has "@" and "." and if the "@" is before the "."
        elif userMail.find("@") == -1 or userMail.find(".") == -1:
            messagebox.showerror("Register", "Email does not contain '@' or '.'")
            return
        elif userMail.find(".") < userMail.find("@"):
            messagebox.showerror("Register", "Email is not written correctly.")
            return
        
        # Everything is correct append to the files
        else:
            emailVerification = True
            time = datetime.datetime.now()
            date = time.strftime("%d/%m/%Y %H:%M:%S")
            fUsers = open(users_file, "a", encoding="utf-8")
            fields = userName + ";" + userAge + ";" + userMail + ";" + userPwd + ";" + userPwdCheck + ";" + userType + ";" + date + "\n"
            fUsers.write(fields)
            fUsers.close()
            messagebox.showinfo("Register", "Account has been created successfully!")
            panelRegister.place_forget()
            return
            

def logOut(userName, userPass, logged_Menu, home_menu):
    # function to log out the user and return to the home menu
    global logged
    logged = False
    logged_Menu.place_forget()
    refresh(home_menu, logged_Menu)
    return

def refresh(home_menu, logged_Menu):
    
    # if the users is logged show the logged menu otherwise show the home menu
    if logged == True:
        home_menu.place_forget()
        logged_Menu()
        return
    else:
        logged_Menu.place_forget()
        home_menu()
        return
        
        
