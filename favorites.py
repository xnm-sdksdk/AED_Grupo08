# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
from time import strftime
import datetime
import os

favorites_file = ".\\Files\\favorites.txt"

comments_file = ".\\Files\\comments.txt"

activity_file = ".\\Files\\activity.txt"


def insertComment(userName, content, activity, commentlbox):
    
    if content == "":
        messagebox.showerror("Error", "The comment field is empty!")
        return
    else:
        # Register the comment by time and date
        time = datetime.datetime.now()
        date = time.strftime("%d/%m/%Y %H:%M:%S")
        
        # open the file and write the comment
        fcomments = open(comments_file, "a", encoding="utf-8")
        fields = userName + ";" + content + ";" + date + "\n"
        fcomments.write(fields)
        fcomments.close()
        
        # Name of the user, activity selected,  the content  of the comment and date of the comment.
        commentlbox.insert("end", userName + " said in:  " + activity +  "   Comment: " + content + ".    " + date)