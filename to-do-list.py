import tkinter as tk

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)

def update_task():
    selected = listbox.curselection()
    new_task = entry.get()
    if selected and new_task != "":
        listbox.delete(selected)
        listbox.insert(selected[0], new_task)
        entry.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do")

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

add_btn = tk.Button(root, text="Add", command=add_task)
add_btn.pack()

update_btn = tk.Button(root, text="Update", command=update_task)
update_btn.pack()

delete_btn = tk.Button(root, text="Delete", command=delete_task)
delete_btn.pack()

listbox = tk.Listbox(root, width=35)
listbox.pack(pady=10)

root.mainloop()
