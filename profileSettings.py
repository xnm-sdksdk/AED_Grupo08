# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
import os

users = ".\\Files\\users.txt"

def personal_details(userName, nameChanged, passwordChanged, emailChanged):
    os.rename(".\\users\\" + userName,".\\users\\" + nameChanged)
    
    fUsers = open(users, "r", encoding="utf-8")
    for linha in fUsers:
        campos = linha.split(";")
        if campos[0] == userName:   
            with open(users, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(users, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
           
    linhaAlteradaDone = ("\n" + nameChanged + ";" + campos[3] + ";" + emailChanged + ";" + passwordChanged + ";" + campos[4] + ";" + campos[5] + ";" + campos[6] + ";" + campos[7] + ";")
    fListaDoing = open (users, "a", encoding="utf-8")
    fListaDoing.write(linhaAlteradaDone)
    fListaDoing.close()
    
    
    with open(users, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(users, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line)
       
    
    


    
    
    
    