# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
from time import strftime
import datetime
import os

favorites_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/favorites.txt"

comments_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/comments.txt"



def insertComment(userName, content):
    
    # Register the comment by time and date
    time = datetime.datetime.now()
    date = time.strftime("%d/%m/%Y %H:%M:%S")
    
    # open the file and write the comment
    fcomments = open(comments_file, "a", encoding="utf-8")
    fields = userName + ";" + content + ";" + date + "\n"
    fcomments.write(fields)
    fcomments.close()