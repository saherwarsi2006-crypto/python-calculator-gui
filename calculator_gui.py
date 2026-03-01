import tkinter as tk

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 16))
entry.pack(fill=tk.BOTH)

# buttons
buttons = [
    '7','8','9','/',
    '4','5','6','*',
    '1','2','3','-',
    '0','.','=','+'
]

frame = tk.Frame(root)
frame.pack()

for b in buttons:
    if b == "=":
        btn = tk.Button(frame, text=b, command=calculate)
    else:
        btn = tk.Button(frame, text=b, command=lambda x=b: click(x))
    btn.pack(side=tk.LEFT)

tk.Button(root, text="Clear", command=clear).pack()

root.mainloop()