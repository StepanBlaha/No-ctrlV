import pyperclip
import time
import os
# pip install pyperclip
last_text = ""
is_stopped = False
while True:
    # Get file user wants to write into
    print("Instructions:")
    print(f'To exit write mode:\n copy stop write\n close the file')
    print(f'To resume:\n If file is closed run the file\n If still running copy start write')
    print("Now enter the file for writting")
    userInp = input("Path to file you want to write into: ")
    # File validity check
    if os.path.isfile(userInp):
        if userInp.endswith('.txt'):
            print("Write file successfully set up")
            # Initialy clean the clipboard
            pyperclip.copy("")
            break
        else:
            print("Must be a .txt file")
    else:
        print("Enter calid absolute path to the file you want to write into")

while True:

    copied_text = pyperclip.paste().strip()
    # Make sure the clipboard isnt empty
    if not copied_text:
        time.sleep(1)
        continue
    # Make sure the clipboard content isnt the same
    if copied_text == last_text:
        time.sleep(1)
        continue

    last_text = copied_text

    # Handle stop and restart of the write mode
    if copied_text.lower() == "stop write":
        is_stopped = True
        continue
    elif copied_text.lower() == "start write":
        is_stopped = False
        continue
    # Skip iteration if write is stopped
    if is_stopped:
        continue

    # Write into file
    with open(userInp, "a") as f:
        f.write(copied_text + '\n')


    # Timeout
    time.sleep(1)