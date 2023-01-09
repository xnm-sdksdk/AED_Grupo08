# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

# path to users.txt file
users_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(name_regist_temp, age_regist_temp, email_regist_temp, password_regist_temp, password_confirmation, user_type):
     
    
    # To check all files inside the directory
    all_profiles = os.listdir()
    # print(all_profiles) Verify if is all good

    
    # verification for empty fields
    if name_regist_temp == "" or age_regist_temp == "" or email_regist_temp == "" or password_regist_temp == "" or password_confirmation == "" or user_type == "":        
        messagebox.showerror("Error!", "All fields are required!")
        return
    
    
    usersFilePath = open(users_file, "r", encoding="utf-8") # open in read mode
    listUsers = usersFilePath.readlines() # read file to a list
    usersFilePath.close() # close file
    
    for line in listUsers:
        if name_regist_temp == line.split(";")[0]:
            messagebox.showerror("Register", "Account already exists!")
            return
    
    """
    # verification for the password confirmation
    if password_regist_temp != password_confirmation:
        messagebox.showerror("Regist", "Password does not match!")
        return 
    """
        
    for profile_check in all_profiles:
        
        if name_regist_temp == profile_check:
            messagebox.showerror("Register", "Account already exists!")
            return 
            
    
    line = name_regist_temp + "," + age_regist_temp + "," + email_regist_temp + "," + password_regist_temp + "," + user_type + "\n"
    messagebox.showinfo("Register", "Account has been created!")
    
    
    
    

# Function to verify if the user is registered in the app
def authentication(name_regist_temp, password_regist_temp):
    fileAuth = open(users_file, "r", encoding="utf-8") # Open the file to read using the utf-8 encoding
    listUsers = fileAuth.readlines() # read all lines and save in a list
    fileAuth.close() # Close the file
    
    
    
    for line in listUsers:  # For each line in the list
        if name_regist_temp == "" or password_regist_temp == "":
            messagebox.showerror("Login", "All fields are required!")
            return
        # If the name and password are the same as the ones in the file
        if line.split(";")[0] == name_regist_temp and line.split(";")[0] == password_regist_temp: 
            # If the user is logged in, show a success message
            entry_msg = "Welcome " + name_regist_temp
            messagebox.showinfo("Login", entry_msg)
            return entry_msg
    # Otherwise show an error message
    messagebox.showerror("Login", "The user or password are incorrect!")
    return ""
