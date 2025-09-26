import tkinter as tk
from tkinter import filedialog

# Create a root window (it won't be shown)
root = tk.Tk()
root.withdraw()  # Hide the root window

# Open a file selection dialog
file_path = filedialog.askopenfilename(
    title="Select a File",
    filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]  # Filter file types
)

# Print the selected file path
if file_path:
    print(f"Selected file: {file_path}")
else:
    print("No file selected.")
