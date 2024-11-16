import os
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import time

def rename_files():
    folder_path = filedialog.askdirectory(title="Select Folder")
    if not folder_path:
        return
    
    prefix = entry_prefix.get()
    date_format = entry_date.get()
    try:
        files = os.listdir(folder_path)
        files = [file for file in files if os.path.isfile(os.path.join(folder_path, file))]
        
        if not files:
            messagebox.showerror("Error", "No files found in the selected folder.")
            return

        for i, filename in enumerate(files):
            old_file_path = os.path.join(folder_path, filename)
            file_extension = os.path.splitext(filename)[1]
            
            # Apply date format if needed
            if date_format:
                current_time = time.strftime(date_format)
                new_filename = f"{prefix}_{current_time}_{i+1}{file_extension}"
            else:
                new_filename = f"{prefix}_{i+1}{file_extension}"
            
            new_file_path = os.path.join(folder_path, new_filename)
            os.rename(old_file_path, new_file_path)
        
        messagebox.showinfo("Success", f"Renamed {len(files)} files successfully.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Setting up the Tkinter window
window = tk.Tk()
window.title("Bulk File Renamer")
window.geometry("400x300")

# Prefix field
label_prefix = tk.Label(window, text="Enter Prefix:")
label_prefix.pack(pady=5)
entry_prefix = tk.Entry(window, width=30)
entry_prefix.pack(pady=5)

# Date format field
label_date = tk.Label(window, text="Enter Date Format (Optional, e.g., %Y-%m-%d):")
label_date.pack(pady=5)
entry_date = tk.Entry(window, width=30)
entry_date.pack(pady=5)

# Rename button
rename_button = tk.Button(window, text="Rename Files", command=rename_files)
rename_button.pack(pady=20)

# Run the app
window.mainloop()
