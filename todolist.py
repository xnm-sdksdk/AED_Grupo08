from tkinter import *
from tkinter import messagebox
import os

# Function to add tasks to the list
def addTaskBox(userName, insertTask, selectCategoria):
    tasks_file = ".\\users\\" + userName + "\\list.txt"
    
    # Check if the task field is empty if is error message is going to be displayed
    if insertTask == "":
        messagebox.showerror("Error", "The category field is empty!")
        return
    # If not insert the task in the ListBox
    else: 
        fListTasks = open(tasks_file, "r", encoding="utf-8")
        listaTasks = fListTasks.readlines()
        fListTasks.close()  
        if len(listaTasks) == 0:
            fList = open(tasks_file, 'a', encoding='utf-8')     
            fList.write(insertTask + ";" + selectCategoria + ";" + "todo" + ";")
        else:
            fList = open(tasks_file, 'a', encoding='utf-8') 
            fList.write("\n" + insertTask + ";" + selectCategoria + ";" + "todo" + ";")
        fList.close()
        with open(tasks_file, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(tasks_file, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line) 
        return

    

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
def sortDesc(todolistBox):
    # Sort the tasks in descending order
    count = todolistBox.size()
    list = []
    for i in range(count):
        # append the content from the listbox
        list.append(todolistBox.get(i))
    list.sort(reverse=True) # sort alphabetically in reverse order
    # delete the content of the lbox
    todolistBox.delete(0, "end")
    for i in list:
        todolistBox.insert("end", i)



# Function to add to the favorites list
def addFavorites():
    pass

# Function to filter the tasks
def filter():
    pass
