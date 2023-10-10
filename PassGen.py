import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(event=None):
    password_length = int(password_length_entry.get())

    if password_length <= 0:
        messagebox.showerror("Error", "Password length must be a positive integer")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.choice(characters) for i in range(password_length))
    
    password_label.config(text="Generated Password:")
    generated_password_label.config(text=generated_password, font=("Arial", 16, "bold"))

# Create the main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")  

# Create a label and entry for password length input
password_length_label = tk.Label(root, text="Enter password length:")
password_length_label.pack(pady=10)
password_length_entry = tk.Entry(root)
password_length_entry.pack(pady=10)

password_length_entry.bind('<Return>', generate_password)

# Create a button to generate the password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display "Generated Password:"
password_label = tk.Label(root, text="Generated Password:")
password_label.pack(pady=10)

generated_password_label = tk.Label(root, text="", font=("Arial", 16, "bold"))
generated_password_label.pack()

# Run the main event loop
root.mainloop()
