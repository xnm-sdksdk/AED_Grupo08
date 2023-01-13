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
    else:
        # Convert the time inserted by the user to seconds
        timer = int(float(timerNotification))
        min_sec_timer = timer * 60
        messagebox.showinfo("Notifications", "Send Notification?")
        
        time.sleep(min_sec_timer)
        
        # Send the notification to the user
        notification.notify(title= titleNotification, message= messageNotification, app_icon="Images/icon.png",app_name="Notifications", timeout= 10)