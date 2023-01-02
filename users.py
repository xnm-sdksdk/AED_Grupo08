# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox



# Function to verify all inputs inserted by the user in the register function 
def verification():
    # Retrieve the values from the items with the specified key     
    name = name_regist_temp.get()
    age = age_regist_temp.get()
    email = email_regist_temp.get()
    password = password_regist_temp.get()
    user = user_type.get()
    
    
    
    # To check all files inside the directory
    all_profiles = os.listdir()
    # print(all_profiles) Verify if is all good

    
    if name == "" or age == "" or email == "" or password == "" or user == "":
        messagebox.showerror("Error!", "All fields are required!")
        
        
    for profile_check in all_profiles:
        if name == profile_check:
            messagebox.showerror("Error!", "Account already exists!")
            return 
            
            
        # else for placement of the treeview



