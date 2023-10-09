import tkinter as tk

expression = ""

def append_number(num):
    global expression
    expression += str(num)
    eq.set(expression)
    exp_f.icursor(len(expression)) 

def clear():
    global expression
    expression = ""
    eq.set("")
    exp_f.icursor(0)  

def calculate():
    global expression
    try:
        result = str(eval(expression))
        eq.set(result)
        expression = ""
        exp_f.icursor(0) 
    except:
        eq.set("Invalid input")
        expression = ""
        exp_f.icursor(0) 

def modify_expression(event=None):
    global expression
    cursor_position = exp_f.index(tk.INSERT)
    expression = exp_f.get()
    eq.set(expression)
    exp_f.icursor(cursor_position) 

def delete_last_character():
    global expression
    if expression:
        expression = expression[:-1]
        eq.set(expression)
        exp_f.icursor(len(expression))

def create_button(gui, text, row, column, command=None, height=2, width=5, bg="white"):
    button = tk.Button(gui, text=text, fg="black", bg=bg, font=("Arial", 14),
                       command=command or (lambda: append_number(text)), height=height, width=width)
    button.grid(row=row, column=column, padx=5, pady=5)

if __name__ == "__main__":
    gui = tk.Tk()
    gui.title("Simple Calculator")
    gui.geometry("300x385")

    eq = tk.StringVar()
    exp_f = tk.Entry(gui, textvariable=eq, font=("Arial", 18))
    exp_f.grid(row=0, column=0, columnspan=4, ipadx=10, ipady=10)

    buttons_data = [
        ("1", 1, 0), ("2", 1, 1), ("3", 1, 2), ("+", 1, 3),
        ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
        ("7", 3, 0), ("8", 3, 1), ("9", 3, 2), ("*", 3, 3),
        (".", 4, 0), ("0", 4, 1), ("=", 4, 2,calculate,2,5,"orange"),
        ("/", 4, 3),
        ("Del", 5, 1, delete_last_character, 1, 5, "red"),
        ("Clear", 5, 0, clear, 1, 5, "red")
    ]

    for button_data in buttons_data:
        create_button(gui, *button_data)

    exp_f.bind("<KeyRelease>", modify_expression)  

    gui.mainloop()
