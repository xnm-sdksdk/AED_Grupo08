# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

# path to users.txt file
users_file = "files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(name_regist_temp, age_regist_temp, email_regist_temp, password_regist_temp, password_confirmation, user_type):
    
    
    name_regist_temp = StringVar()
    age_regist_temp = StringVar()
    email_regist_temp = StringVar()
    password_regist_temp = StringVar()
    user_type = StringVar()
    password_confirmation = StringVar()
    # Set User by Default as Type of  
    user_type.set('user')
    
    
    # To check all files inside the directory
    all_profiles = os.listdir()
    # print(all_profiles) Verify if is all good

    
    # verification for empty fields
    if name_regist_temp == "" or age_regist_temp == "" or email_regist_temp == "" or password_regist_temp == "" or password_confirmation == "" or user_type == "":        
        messagebox.showerror("Error!", "All fields are required!")
        return
    
    
    # verification for the password confirmation
    if password_regist_temp != password_confirmation:
        messagebox.showerror("Regist", "Password does not match!")
        return 
        
    for profile_check in all_profiles:
        if name == profile_check:
            messagebox.showerror("Regist", "Account already exists!")
            return 
            
    
    usersf = open(users_file, "a")
    line = name_regist_temp + "," + age_regist_temp + "," + email_regist_temp + "," + password_regist_temp + "," + user_type + "\n"
    usersf.write(line)
    usersf.close()
    messagebox.showinfo("Regist", "Account has been created!")
    



