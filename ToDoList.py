import tkinter as G
from tkinter import messagebox

# Function to add a task
def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(G.END, task)
        entry.delete(0, G.END)

# Function to handle pressing the "Enter" key
def on_enter(event):
    add_task()

# Function to delete a task
def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)

# Function to update a task
def update_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        updated_task = entry.get()
        if updated_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, updated_task)
            entry.delete(0, G.END)

# Create the main window
root = G.Tk()
root.title("To-Do List App")

# Create and place GUI components
entry = G.Entry(root, width=60)  
entry.pack(pady=10)

# Bind Enter key to add_task
entry.bind("<Return>", on_enter)

label = G.Label(root, text="Tasks:")
label.pack()

task_listbox = G.Listbox(root, width=60, height=15)
task_listbox.pack(side=G.LEFT, padx=10, pady=5)

scrollbar = G.Scrollbar(root, orient=G.VERTICAL, command=task_listbox.yview, width=20)
scrollbar.pack(side=G.RIGHT, fill=G.Y)
task_listbox.config(yscrollcommand=scrollbar.set)

add_button = G.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = G.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

update_button = G.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

# Run the application
root.mainloop()
