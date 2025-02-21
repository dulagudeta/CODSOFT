from tkinter import *
from tkinter import messagebox

def add_task():
    t = task_entry.get().strip()
    if t == "":
        messagebox.showwarning("Warning", "Please enter a task.")
    else:
        task_list.insert(END, t)
        task_entry.delete(0, END)
        update_status()
        save_tasks()

def delete_task():
    try:
        index = task_list.curselection()[0]
        task_list.delete(index)
        update_status()
        save_tasks()
    except:
        messagebox.showwarning("Warning", "Select a task to delete.")

def save_tasks():
    f = open("tasks.txt", "w")
    tasks = task_list.get(0, END)
    for task in tasks:
        f.write(task + "\n")
    f.close()

def load_tasks():
    try:
        f = open("tasks.txt", "r")
        for line in f:
            task_list.insert(END, line.strip())
        f.close()
        update_status()
    except:
        pass

def update_status():
    status_label.config(text="Total tasks: " + str(task_list.size()))

root = Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg="#D3E0EA")
root.resizable(False,False)

Label(root, text="My To-Do List", font=("Arial", 16, "bold"), bg="Azure", fg="navy").pack(pady=10)

task_entry = Entry(root, font=("Arial", 12), width=30)
task_entry.pack(pady=5)

Button(root, text="Add Task", command=add_task, bg="blue", font=("Arial", 12)).pack(pady=5)

task_list = Listbox(root, font=("Arial", 12), width=35, height=10, bg="white", fg="black")
task_list.pack(pady=5)

Button(root, text="Delete Task", command=delete_task, bg="red", font=("Arial", 12)).pack(pady=5)
Button(root, text="Save Tasks", command=save_tasks, bg="Green", font=("Arial", 12)).pack(pady=5)

status_label = Label(root, text="Total tasks: 0", font=("Arial", 10), bg="white", fg="Navy")
status_label.pack(pady=5)

load_tasks()
root.mainloop()
