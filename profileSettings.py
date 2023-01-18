# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

usersFile = ".\\Files\\users.txt"



def personal_details():
    
    file = open(usersFile, "r")
    file_data = file.read()
    details = file_data.split()
    name = details[0]
    age = details[1]
    mail = details[2]
    pwd = details[3]
    pwdCheck = details[4]
    user = details[5]
    
    
    
    