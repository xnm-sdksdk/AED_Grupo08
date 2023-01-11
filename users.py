# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

# path to users.txt file
users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(name_regist_temp, password_regist_temp):
    
    all_profiles = os.listdir("Files/users.txt")
    
    fUsers = open(users_file, "r", encoding="utf-8")
    usersList = fUsers.readlines()
    fUsers.close()
    
    for name in all_profiles:
        if name_regist_temp != usersList[0]: 
            messagebox.showerror("Login", "Invalid Username!")
            return

# Function to verify if the user is registered in the app
def authentication(userName, userAge, userMail, userPwd, userPwdCheck, userType, panelRegister):
    
    
    # Variables to check values
    
    
    
    
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
        elif userAge != int:
            messagebox.showerror("Register", "Age must be a number!")
            return
        
        # Password verification
        elif userPwd != userPwdCheck:
            messagebox.showerror("Register", "Passwords don't match!")
            return
            
        # Verification to check if email has "@" and "." and if the "@" is before the "."
        elif userMail.find("@") == -1 or userMail.find(".") == -1:
            messagebox.showerror("Register", "Email does not contain @ or .")
            return
        elif userMail.find(".") < userMail.find("@"):
            messagebox.showerror("Register", "Email is not written correctly.")
            return
        
        # Everything is correct append to the files
        else:
            emailVerification = True
            fUsers = open(users_file, "a", encoding="utf-8")
            fields = userName + ";" + userAge + ";" + userMail + ";" + userPwd + ";" + userPwdCheck + ";" + userType + "\n"
            fUsers.write(fields)
            fUsers.close()
            messagebox.showinfo("Register", "Account has been created successfully!")
            panelRegister.place_forget()
            return
            
            