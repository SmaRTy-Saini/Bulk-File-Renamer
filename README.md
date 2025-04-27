# Bulk File Renamer Tool

A simple, flexible tool for bulk renaming files based on customizable patterns. Ideal for photographers, content managers, developers, and anyone handling large batches of files needing consistent naming conventions.

---

## ✨ Features

* **Custom Prefix:** Easily add personalized prefixes to your filenames.
* **Date Formatting:** Automatically insert dates into filenames using your preferred format (e.g., `YYYY-MM-DD` like `2025-04-26`).
* **Sequential Numbering:** Add incremental numbers to files to maintain order and uniqueness.
* **Dual Interfaces:** Choose between:
    * A user-friendly graphical interface (GUI) built with Python and Tkinter.
    * A scriptable command-line interface (CLI) using PowerShell for automation.
* **Lightweight and Fast:** Designed with minimal dependencies for quick and efficient operation.

---

## 🚀 Installation

Choose the version that best suits your workflow:

### Python Version (GUI)

1.  **Install Python:** Ensure you have Python 3.x installed. Download it from [python.org](https://www.python.org/).
2.  **Check Tkinter:** Tkinter is usually included with standard Python installations on Windows and macOS. On some Linux distributions, you might need to install it separately (e.g., `sudo apt-get update && sudo apt-get install python3-tk` on Debian/Ubuntu).
3.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SmaRTy-Saini/Bulk-File-Renamer.git](https://github.com/SmaRTy-Saini/Bulk-File-Renamer.git)
    cd Bulk-File-Renamer
    ```
    Alternatively, download the repository files as a ZIP and extract them.
4.  **Run the script:**
    ```bash
    python bulk-file-renamer.py
    ```

### PowerShell Version (CLI)

1.  **Open PowerShell:** Launch PowerShell on your Windows machine.
2.  **Get the Script:** Clone the repository (as shown above) or download `bulk_rename.ps1`.
3.  **Navigate to the script's directory:**
    ```powershell
    # Example: Replace 'path\to\Bulk-File-Renamer' with the actual path
    cd C:\path\to\Bulk-File-Renamer
    ```
4.  **Run the script:**
    ```powershell
    ./bulk_rename.ps1
    ```
    *Note: If you encounter an error about script execution being disabled, you may need to adjust your PowerShell execution policy. You can allow scripts for the current user by running:*
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
    ```
    *Run PowerShell as Administrator if needed for this command.*

---

## 🛠 Usage

### Python GUI

1.  Launch the application (`python bulk-file-renamer.py`).
2.  Click **"Select Folder"** to choose the directory containing the files you want to rename.
3.  Configure the renaming options:
    * Enter a **Prefix** (optional).
    * Enable and configure **Date Formatting** (optional).
    * Enable and configure **Sequential Numbering** (optional).
4.  *(Recommended)* Review the proposed new filenames in the **Preview** section.
5.  Click **"Bulk Rename"** to apply the changes to the files in the selected folder.

### PowerShell CLI

1.  Open the `bulk_rename.ps1` script in a text editor (like VS Code, Notepad++, or Notepad).
2.  Modify the script parameters near the top (e.g., `$targetFolder`, `$prefix`, date/numbering settings) according to your requirements.
3.  *(Advanced)* For more complex automation, you can modify the script to accept command-line arguments instead of editing the file directly.
4.  Save the changes and run the script from PowerShell as described in the Installation section.

---

## 📦 Project Structure
