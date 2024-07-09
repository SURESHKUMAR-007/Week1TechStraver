import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pyqrcode
import png

def generate_qr():
    # Get the input data from the entry widget
    data = entry.get()
    
    # Check if the data is not empty
    if not data:
        messagebox.showwarning("Input Error", "Please enter a URL or string.")
        return

    # Generate the QR code
    qr_code = pyqrcode.create(data)
    
    # Ask the user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG files", "*.png")])
    
    if file_path:
        # Save the QR code as a PNG file
        qr_code.png(file_path, scale=6)
        messagebox.showinfo("Success", f"QR Code saved to {file_path}")

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Create a label
label = tk.Label(root, text="Enter URL or String:")
label.pack(pady=10)

# Create an entry widget
entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create a button to generate the QR code
generate_button = tk.Button(root, text="Generate QR Code", command=generate_qr)
generate_button.pack(pady=20)

# Run the main loop
root.mainloop()
