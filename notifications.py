# Library's: Tkinter UI and messagebox
from tkinter import *
from tkinter import messagebox
from plyer import notification # Library to send notifications
import time 
import os




def send_Info(titleNotification, messageNotification, timerNotification):
    
    if titleNotification == "" or messageNotification == "" or timerNotification == "":
        messagebox.showerror("Alert", "All fields are required!")
        return