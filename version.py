import pyautogui
import time
import schedule
import subprocess

# Function to handle UAC prompt and click "Yes"
def handle_uac():
    subprocess.Popen(["powershell.exe", "Start-Process 'MontavueGo.exe' -Verb runAs"])
    time.sleep(2)
    pyautogui.click(960, 540)  # Adjust the coordinates to click "Yes" button

# Function to perform search and open MontavueGo app
def open_montavuego():
    pyautogui.hotkey('win', 's')  # Open Windows search
    time.sleep(1)
    pyautogui.write('MontavueGo')
    time.sleep(1)
    pyautogui.press('enter')  # Press enter to open the app

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

# Main function
def main():
    handle_uac()
    time.sleep(2)  # Wait for the UAC prompt to appear
    open_montavuego()
    time.sleep(5)  # Wait for the app to open
    perform_actions()

# Schedule the main function to run at 6 AM on weekdays
schedule.every().monday.at("06:00").do(main)
schedule.every().tuesday.at("06:00").do(main)
schedule.every().wednesday.at("06:00").do(main)
schedule.every().thursday.at("06:00").do(main)
schedule.every().friday.at("06:00").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)
