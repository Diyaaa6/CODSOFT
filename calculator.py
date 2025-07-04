import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.resizable(False, False)

def on_click(value):
    if value == "C":
        entry.delete(0, tk.END)
    elif value == "=":
        try:
            result = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, value)

entry = tk.Entry(root, font=("Arial", 20))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=5, ipady=5)

buttons = ['7', '8', '9', '/','4', '5', '6', '*','1', '2', '3', '-','C', '0', '=', '+']

for index, text in enumerate(buttons):
    row = (index // 4) + 1
    col = index % 4
    button = tk.Button(root, text=text, width=5, height=2, font=("Arial", 16),
                       command=lambda val=text: on_click(val))
    button.grid(row=row, column=col, padx=5, pady=5)

root.mainloop()
