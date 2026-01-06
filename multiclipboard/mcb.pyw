#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
import shelve
import pyperclip
import sys

mcb_shelf = shelve.open("mcb")

# Save clipboard content.
if len(sys.argv) == 3:
    command = sys.argv[1].lower()
    keyword = sys.argv[2]

    if command == "save":
        mcb_shelf[keyword] = pyperclip.paste()
    elif command == "delete":
        if keyword in mcb_shelf:
            del mcb_shelf[keyword]

elif len(sys.argv) == 2:
    command = sys.argv[1].lower()

    # List keywords
    if command == "list":
        pyperclip.copy(str(list(mcb_shelf.keys())))
    # Delete all keywords
    elif command == "delete_all":
        mcb_shelf.clear()
    # Load content
    elif command in mcb_shelf:
        pyperclip.copy(mcb_shelf[command])

mcb_shelf.close()
