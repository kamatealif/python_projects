

# 📋 MultiClipboard (mcb.pyw)

A "productivity hack" that turns your clipboard into a searchable database. Instead of copying and pasting one item at a time, this script allows you to save dozens of text snippets under keywords and retrieve them instantly via the command line.

---

## 🧠 How It Works

The program acts as a persistent middleman between your **System Clipboard** and a **Shelf File** (a permanent database on your disk).



### Core Components
* **`sys.argv`**: Reads the commands you type in the terminal.
* **`shelve`**: A Python module that saves dictionary-like data to your hard drive.
* **`pyperclip`**: Handles the actual "Copy" and "Paste" actions with your OS.

---

## 💻 Implementation

Save the following code as `mcb.pyw`. The `.pyw` extension ensures that no terminal window pops up when the script executes.

## 🚀 Command References 
| Command | Usage | Description |
| --- | --- | --- |
| Save | `py mcb.pyw save <key>` | Maps your current clipboard text to <key>. |
| Load | `py mcb.pyw <key>` | Copies the text stored under <key> to your clipboard. |
| List | `py mcb.pyw list` | Copies a list of all your saved keys to the clipboard. |
| Delete | `py mcb.pyw delete <key>` | Removes the specific <key> from storage. |
| Clear | `py mcb.pyw delete_all` | Wipes the entire database clean. |

## 🛠 Setup Guid 

1. Install Dependencies
You'll need the pyperclip module, as it is not part of the Python Standard Library:

    ```bash 
    pip instll pyperclip
    ```

2. option create a batch shortcut
To run the tool by simply typing mcb instead of py mcb.pyw, create a file named mcb.bat in your Windows folder:

    ```bash 
    @py.exe C:\Users\YourName\Documents\mcb.pyw %*
    ```