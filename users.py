# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox


# path to users.txt file
users_file = "files/users.txt"

# Function to verify all inputs inserted by the user in the register function 
def verification(name_regist_temp, age_regist_temp, email_regist_temp, password_regist_temp, password_confirmation, user_type):
    # Retrieve the values from the items with the specified key     
    name = name_regist_temp.get()
    age = age_regist_temp.get()
    email = email_regist_temp.get()
    password = password_regist_temp.get()
    confirmation = password_confirmation.get()
    user = user_type.get()
    
    
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

    
    if name == "" or age == "" or email == "" or password == "" or user == "":
        messagebox.showerror("Error!", "All fields are required!")
        
        
    for profile_check in all_profiles:
        if name == profile_check:
            messagebox.showerror("Error!", "Account already exists!")
            return 
            
            
        # else for placement of the treeview



