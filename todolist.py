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
    
def filterTasks(userName, selectCategoria, treeTodo, treeDoing, treeDone):
    
    treeTodo.delete(*treeTodo.get_children())
    treeDoing.delete(*treeDoing.get_children())
    treeDone.delete(*treeDone.get_children())
    
    # Add to the treeview 
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[1] == selectCategoria and campos[2] == "todo":
            treeTodo.insert("", "end", values = (campos[0]))   
        if campos[1] == selectCategoria and campos[2] == "doing": 
            treeDoing.insert("", "end", values = (campos[0]))
        if campos[1] == selectCategoria and campos[2] == "done": 
            treeDone.insert("", "end", values = (campos[0]))
    
def deleteSelectedTask(userName, treeTodo, treeDoing, treeDone):
    
    row_idTodo = treeTodo.focus()
    linhaTodo = treeTodo.item(row_idTodo)
    linhaSelecionadaTodo = linhaTodo["values"]
    
    row_idDoing = treeDoing.focus()
    linhaDoing = treeDoing.item(row_idDoing)
    linhaSelecionadaDoing = linhaDoing["values"]
    
    row_idDone = treeDone.focus()
    linhaDone = treeDone.item(row_idDone)
    linhaSelecionadaDone = linhaDone["values"]
   
    listaA = []
    if linhaSelecionadaTodo != "":
       listaA.append(linhaSelecionadaTodo)
    if linhaSelecionadaDoing != "":
        listaA.append(linhaSelecionadaDoing)
    if linhaSelecionadaDone != "":   
        listaA.append(linhaSelecionadaDone)
    taskRemove = str(listaA[0])
    taskRemoveA = taskRemove.replace("[", "").replace("]", "").replace("'", "")
    
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[0] == taskRemoveA:
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line)

def sort(userName):
    
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    f = open(listaTarefas, 'r', encoding='utf-8')
    lines = f.readlines()

    sorted_lines = sorted(lines)

    with open(listaTarefas, 'w') as f:
        f.writelines(sorted_lines)
        
def sortReverse(userName):
    
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    f = open(listaTarefas, 'r', encoding='utf-8')
    lines = f.readlines()

    sorted_lines = sorted(lines, key=lambda x: x.split()[-1], reverse=True)

    with open(listaTarefas, 'w') as f:
        f.writelines(sorted_lines)  

def deleteAll(userName, selectCategoria, treeTodo, treeDoing, treeDone):
    
    treeTodo.delete(*treeTodo.get_children())
    treeDoing.delete(*treeDoing.get_children())
    treeDone.delete(*treeDone.get_children())
    
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[1] == selectCategoria:
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != "":
                            fListaDoing.write(line)

# Function to add to the favorites list
def addFavorites(userName, selectCategoria, treeTodo, treeDoing, treeDone):
            
    row_idTodo = treeTodo.focus()
    linhaTodo = treeTodo.item(row_idTodo)
    linhaSelecionadaTodo = linhaTodo["values"]
    
    row_idDoing = treeDoing.focus()
    linhaDoing = treeDoing.item(row_idDoing)
    linhaSelecionadaDoing = linhaDoing["values"]
    
    row_idDone = treeDone.focus()
    linhaDone = treeDone.item(row_idDone)
    linhaSelecionadaDone = linhaDone["values"]
   
    listaA = []
    if linhaSelecionadaTodo != "":
       listaA.append(linhaSelecionadaTodo)
    if linhaSelecionadaDoing != "":
        listaA.append(linhaSelecionadaDoing)
    if linhaSelecionadaDone != "":   
        listaA.append(linhaSelecionadaDone)
    taskSelected = str(listaA[0])
    taskSelectedA = taskSelected.replace("[", "").replace("]", "").replace("'", "")
    
    favoritosFile = ".\\users\\" + userName + "\\favorites.txt"
    fListFavoritos = open(favoritosFile, "r", encoding="utf-8")
    listaFavoritos = fListFavoritos.readlines()
    fListFavoritos.close()
   
    if len(listaFavoritos) == 0:
        fList = open(favoritosFile, 'a', encoding='utf-8')     
        fList.write(taskSelectedA + ";" + selectCategoria + ";")
    else:
        fList = open(favoritosFile, 'a', encoding='utf-8') 
        fList.write("\n" + taskSelectedA + ";" + selectCategoria + ";")
    fList.close()
    with open(favoritosFile, "r") as fListaDoing:
            lines = fListaDoing.readlines()
            with open(favoritosFile, "w") as fListaDoing:
                for line in lines:
                    if line.strip("\n") != "":
                        fListaDoing.write(line)

def estadoDoingDone(userName, selectCategoria, treeTodo, treeDoing, treeDone):
    
    row_idTodo = treeTodo.focus()
    linhaTodo = treeTodo.item(row_idTodo)
    linhaSelecionadaTodo = linhaTodo["values"]
    
    row_idDoing = treeDoing.focus()
    linhaDoing = treeDoing.item(row_idDoing)
    linhaSelecionadaDoing = linhaDoing["values"]
    
    row_idDone = treeDone.focus()
    linhaDone = treeDone.item(row_idDone)
    linhaSelecionadaDone = linhaDone["values"]
   
    listaA = []
    if linhaSelecionadaTodo != "":
       listaA.append(linhaSelecionadaTodo)
    if linhaSelecionadaDoing != "":
        listaA.append(linhaSelecionadaDoing)
    if linhaSelecionadaDone != "":   
        listaA.append(linhaSelecionadaDone)
    taskSelected = str(listaA[0])
    taskSelectedA = taskSelected.replace("[", "").replace("]", "").replace("'", "")
    
    listaTarefas = ".\\users\\" + userName + "\\list.txt"
    fListTasks = open(listaTarefas, "r", encoding="utf-8")
    listaTasks = fListTasks.readlines()
    fListTasks.close()
    for linha in listaTasks:
        campos = linha.split(";")
        if campos[0] == taskSelectedA and campos[2] == "todo":
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open (listaTarefas, "a") as fListaDoing:
                linhaAlteradaDone = ("\n" + taskSelectedA + ";" + selectCategoria + ";" + "doing" + ";")
                fListaDoing.write(linhaAlteradaDone)
                fListaDoing.close()
                with open(listaTarefas, "r") as fListaDoing:
                    lines = fListaDoing.readlines()
                    with open(listaTarefas, "w") as fListaDoing:
                        for line in lines:
                            if line.strip("\n") != "":
                                fListaDoing.write(line)
        elif campos[0] == taskSelectedA and campos[2] == "doing":
            with open(listaTarefas, "r") as fListaDoing:
                lines = fListaDoing.readlines()
                with open(listaTarefas, "w") as fListaDoing:
                    for line in lines:
                        if line.strip("\n") != linha.strip("\n"):
                            fListaDoing.write(line)
            with open (listaTarefas, "a") as fListaDoing:
                linhaAlteradaDone = ("\n" + taskSelectedA + ";" + selectCategoria + ";" + "done" + ";")
                fListaDoing.write(linhaAlteradaDone)
                fListaDoing.close()
                with open(listaTarefas, "r") as fListaDoing:
                    lines = fListaDoing.readlines()
                    with open(listaTarefas, "w") as fListaDoing:
                        for line in lines:
                            if line.strip("\n") != "":
                                fListaDoing.write(line)
      

