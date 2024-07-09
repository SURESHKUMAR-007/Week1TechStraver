import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length, min_lowercase, min_uppercase, min_digits, min_symbols):
    if length < min_lowercase + min_uppercase + min_digits + min_symbols:
        raise ValueError("Password length is too short for the specified minimum counts of character types.")
    
    password_chars = (
        random.choices(string.ascii_lowercase, k=min_lowercase) +
        random.choices(string.ascii_uppercase, k=min_uppercase) +
        random.choices(string.digits, k=min_digits) +
        random.choices(string.punctuation, k=min_symbols)
    )
    
    remaining_length = length - len(password_chars)
    if remaining_length > 0:
        password_chars += random.choices(string.ascii_letters + string.digits + string.punctuation, k=remaining_length)
    
    random.shuffle(password_chars)
    return ''.join(password_chars)

def on_generate_password():
    try:
        length = int(length_entry.get())
        min_lowercase = int(lowercase_entry.get())
        min_uppercase = int(uppercase_entry.get())
        min_digits = int(digits_entry.get())
        min_symbols = int(symbols_entry.get())
        
        password = generate_password(length, min_lowercase, min_uppercase, min_digits, min_symbols)
        messagebox.showinfo("Generated Password", password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")

# Create the GUI application
root = tk.Tk()
root.title("Password Generator")

# Length input
tk.Label(root, text="Password Length:").grid(row=0, column=0)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1)

# Minimum lowercase characters input
tk.Label(root, text="Minimum Lowercase Characters:").grid(row=1, column=0)
lowercase_entry = tk.Entry(root)
lowercase_entry.grid(row=1, column=1)

# Minimum uppercase characters input
tk.Label(root, text="Minimum Uppercase Characters:").grid(row=2, column=0)
uppercase_entry = tk.Entry(root)
uppercase_entry.grid(row=2, column=1)

# Minimum digits input
tk.Label(root, text="Minimum Digits:").grid(row=3, column=0)
digits_entry = tk.Entry(root)
digits_entry.grid(row=3, column=1)

# Minimum symbols input
tk.Label(root, text="Minimum Symbols:").grid(row=4, column=0)
symbols_entry = tk.Entry(root)
symbols_entry.grid(row=4, column=1)

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=on_generate_password)
generate_button.grid(row=5, column=0, columnspan=2)

# Run the application
root.mainloop()
