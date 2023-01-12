from tkinter import *
from tkinter import messagebox
import os

tasks_file = "/home/xnm/Documents/Algoritmia_Estrutura_de_Dados/Projeto_2022_2023/AED_Project_22_23/Files/list.txt"


# Function to add tasks to the list
def addTaskBox(insertTask, todolistBox):
    # Check if the task field is empty if is error message is going to be displayed
    if insertTask == "":
        messagebox.showerror("Error", "The task field is empty!")
        return
    # If not insert the task in the ListBox
    else:
        todolistBox.insert("end", insertTask)
        insertTask.set("")
        countTasks()


# Function to remove the selected task
def deleteSelectedTask(todolistBox):
    position = todolistBox.curselection()
    
    # Check if there is a task selected
    if len(position) > 0:
        todolistBox.delete(todolistBox.curselection())
        countTasks()
    else:
        messagebox.showerror("Error", "The ListBox has no data selected!")
        return


# Function to clean the whole ListBox
def cleanBox(todoListBox):
    todoListBox.delete(0, "end")
    countTasks()


# Function to increment the number of tasks
def countTasks():
    pass


# Function to sort the tasks in ascending order
def sortAsc(todolistBox):
    # Get the number of tasks
    count = todolistBox.size()
    list = []
    for i in range(count):
        list.append(todolistBox.get(i)) # append the content from the listbox
    list.sort() # sort alphabetically
    todolistBox.delete(0, "end") # delete the content of the lbox
    for i in list: # places the list ordered in the lbox
        todolistBox.insert("end", i)
        


# Function to sort the tasks in descending order
def sortDesc():
    pass


# Function to add to the favorites list
def addFavorites():
    pass


# Function to filter the tasks
def filter():
    pass
