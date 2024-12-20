import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        task_listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "No task selected!")

root = tk.Tk()
root.title("To-Do List")

input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_entry = tk.Entry(input_frame, width=40)
task_entry.pack(side=tk.LEFT, padx=5)

add_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_button.pack(side=tk.LEFT, padx=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
