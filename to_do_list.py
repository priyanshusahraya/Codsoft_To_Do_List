import tkinter as tk
from tkinter import simpledialog, messagebox
import os

# File to store the to-do list
TODO_FILE = "todo_list.txt"

def read_todo_list():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def write_todo_list(tasks):
    with open(TODO_FILE, "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def add_task():
    task = simpledialog.askstring("Add Task", "Enter the task:")
    if task:
        tasks = read_todo_list()
        tasks.append(task)
        write_todo_list(tasks)
        update_task_list()
        messagebox.showinfo("Task Added", f"Task '{task}' added.")

def update_task_list():
    tasks = read_todo_list()
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

def update_task():
    task_number = listbox.curselection()
    if task_number:
        new_task = simpledialog.askstring("Update Task", "Enter the new task:")
        if new_task:
            tasks = read_todo_list()
            tasks[task_number[0]] = new_task
            write_todo_list(tasks)
            update_task_list()
            messagebox.showinfo("Task Updated", f"Task updated to '{new_task}'.")
    else:
        messagebox.showwarning("No Selection", "Please select a task to update.")

def delete_task():
    task_number = listbox.curselection()
    if task_number:
        tasks = read_todo_list()
        removed_task = tasks.pop(task_number[0])
        write_todo_list(tasks)
        update_task_list()
        messagebox.showinfo("Task Deleted", f"Task '{removed_task}' deleted.")
    else:
        messagebox.showwarning("No Selection", "Please select a task to delete.")

# Setting up the Tkinter window
root = tk.Tk()
root.title("To-Do List Application")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(button_frame, text="Update Task", command=update_task)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT, padx=5)

# Initialize the task list
update_task_list()

# Start the Tkinter event loop
root.mainloop()
