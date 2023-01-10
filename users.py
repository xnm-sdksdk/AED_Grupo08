# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

# path to users.txt file
users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
"""
def verification(name_regist_temp,password_regist_temp):
     
    
    # To check all files inside the directory
    all_profiles = os.listdir()
    # print(all_profiles) Verify if is all good

    
    usersFilePath = open(users_file, "r", encoding="utf-8") # open in read mode
    listUsers = usersFilePath.readlines() # read file to a list
    usersFilePath.close() # close file
    
    for line in listUsers:
        if name_regist_temp == line.split(";")[0]:
            messagebox.showerror("Register", "Account already exists!")
            return
    
    # verification for the password confirmation
    if password_regist_temp != password_confirmation:
        messagebox.showerror("Regist", "Password does not match!")
        return 

        
    for profile_check in all_profiles:
        
        if name_regist_temp == profile_check:
            messagebox.showerror("Register", "Account already exists!")
            return 
            
    
    line = name_regist_temp + "," + age_regist_temp + "," + email_regist_temp + "," + password_regist_temp + "," + user_type + "\n"
    messagebox.showinfo("Register", "Account has been created!")
"""
    
    
    
    

# Function to verify if the user is registered in the app
def authentication(name_regist_temp, age_regist_temp, email_regist_temp, password_regist_temp, password_confirmation, user_type, panelRegister):
    
    
    all_profiles = os.listdir()
    print(all_profiles) # For back-end verifications
    
    
    # verification for empty fields
    if name_regist_temp == "" or age_regist_temp == "" or email_regist_temp == "" or password_regist_temp == "" or password_confirmation == "" or user_type == "":        
        messagebox.showerror("Register", "All fields are required!")
        return
    
    for name_check in all_profiles:
        if name_regist_temp == name_check:
            messagebox.showerror("Register", "An account with that name already exists!")
            return
        else:
            fUsers = open(users_file, "a", encoding="utf-8")
            fields = name_regist_temp + ";" + age_regist_temp + ";" + email_regist_temp + ";" + password_regist_temp + ";" + user_type + "\n"
            fUsers.write(fields)
            fUsers.close()
            messagebox.showinfo("Register", "Account has been created successfully!")
            panelRegister.place_forget()
            return
            
            