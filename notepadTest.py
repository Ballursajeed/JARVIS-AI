import subprocess
import pyautogui
import time

def write_to_notepad(content):
    try:
        # Open Notepad
        notepad_process = subprocess.Popen(['notepad.exe'])

        # Wait for Notepad to open
        time.sleep(1)

        # Type the content into Notepad
        pyautogui.typewrite(content)

        print("Content written to Notepad successfully.")
    except FileNotFoundError:
        print("Notepad is not installed or not found in the system PATH.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    user_content = input("Enter the content you want to write in Notepad: ")
    write_to_notepad(user_content)
