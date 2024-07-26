import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_number = len(tasks) + 1
        var = tk.BooleanVar()
        chk = tk.Checkbutton(frame, text=f"{task_number}. {task}", variable=var, bg='white', anchor='w')
        chk.pack(fill='x', padx=5, pady=2)
        tasks.append((chk, var))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    for chk, var in tasks:
        if var.get():
            chk.destroy()
    update_numbering()

def clear_tasks():
    for chk, var in tasks:
        chk.destroy()
    tasks.clear()

def update_numbering():
    for i, (chk, var) in enumerate(tasks):
        chk.config(text=f"{i + 1}. {chk.cget('text').split('. ', 1)[1]}")

root = tk.Tk()
root.title("To-Do List")
root.configure(bg='lightblue')

frame = tk.Frame(root, bg='white')
frame.pack(pady=10, padx=10, fill='both', expand=True)

tasks = []

entry = tk.Entry(root, width=50, font=('Helvetica', 12))
entry.pack(pady=10)

button_frame = tk.Frame(root, bg='lightblue')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, bg='green', fg='white', font=('Helvetica', 12, 'bold'))
add_button.grid(row=0, column=0, padx=10)

delete_button = tk.Button(button_frame, text="Delete Task", command=delete_task, bg='red', fg='white', font=('Helvetica', 12, 'bold'))
delete_button.grid(row=0, column=1, padx=10)

clear_button = tk.Button(button_frame, text="Clear Tasks", command=clear_tasks, bg='blue', fg='white', font=('Helvetica', 12, 'bold'))
clear_button.grid(row=0, column=2, padx=10)

root.mainloop()