import tkinter as tk
import subprocess
import pyautogui
import time
import schedule

# Function to perform search and open MontavueGo app
def open_montavuego():
    pyautogui.hotkey('command', 'space')  # Open Spotlight search
    time.sleep(1)
    pyautogui.write('MontavueGo')
    time.sleep(1)
    pyautogui.press('return')  # Press enter to open the app

# Function to perform actions within the MontavueGo app
def perform_actions():
    # Double click on Live View
    pyautogui.doubleClick(500, 500)  # Adjust the coordinates as per your screen resolution

    # Click on + sign to create another Live View tab
    pyautogui.click(100, 100)  # Adjust the coordinates as per your screen resolution

    # Drag the newly created tab to the second monitor
    pyautogui.mouseDown(100, 100)  # Adjust the coordinates as per your screen resolution
    pyautogui.moveTo(1200, 100)  # Adjust the coordinates as per your second monitor position
    pyautogui.mouseUp()

    # Display cameras in the live view
    pyautogui.click(200, 900)  # Adjust the coordinates as per your screen resolution
    time.sleep(1)
    pyautogui.click(300, 900)  # Adjust the coordinates as per your second monitor resolution

# Function to handle UAC prompt and click "Yes" (not needed for macOS)
def handle_uac():
    pass

# Function to launch the automation process
def launch():
    open_montavuego()
    time.sleep(5)  # Wait for the app to open
    perform_actions()

# Create a GUI window
root = tk.Tk()
root.title("MontavueGo Automation")

# Function to launch the automation code when the button is clicked
def launch_clicked():
    launch()

# Create a button to launch the automation code
launch_button = tk.Button(root, text="Launch", command=launch_clicked)
launch_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
