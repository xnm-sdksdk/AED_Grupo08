# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
from time import strftime
from datetime import datetime
import os

favorites_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/favorites.txt"

comments_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/comments.txt"



def insertComment(userName):
    
    # Register the comment by time and date
    time = datetime.datetime.now()
    date = time.strftime("%d/%m/%Y %H:%M:%S")