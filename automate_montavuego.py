import time
import pyautogui

# Login to the computer containing the MontavueGo app
pyautogui.press('win')
pyautogui.typewrite('MontavueGo')
pyautogui.press('enter')

# Handle User Account Control (UAC) prompt
uac_prompt = pyautogui.locateOnScreen('uac_prompt.png', confidence=0.9)
if uac_prompt is not None:
    # If the UAC prompt is found, click the "Yes" button
    uac_center = pyautogui.center(uac_prompt)
    pyautogui.click(uac_center)

# Wait for the MontavueGo app to load
time.sleep(10)

# Click on the MontavueGo icon on the desktop
pyautogui.click(x=100, y=100)

# Double-click on Live View
pyautogui.doubleClick(x=200, y=200)

# Click on the + sign to create another Live View tab
pyautogui.click(x=300, y=300)

# Drag the newly created tab to the second monitor
pyautogui.moveTo(x=400, y=400)
pyautogui.dragTo(x=800, y=400, duration=1)

# Display cameras in the live view by selecting preconfigured Tours
pyautogui.click(x=500, y=500)
pyautogui.typewrite('1')
pyautogui.press('enter')

# Display cameras in the live view on the second monitor by selecting preconfigured Tours
pyautogui.click(x=600, y=600)
pyautogui.typewrite('2')
pyautogui.press('enter')

# Start the automation at 6:00 AM on Monday and end it at 7 PM on Friday
while True:
    now = datetime.datetime.now()
    if now.weekday() >= 0 and now.weekday() <= 4 and now.hour >= 6 and now.hour <= 19:
        # Run the automation script
        pass
    else:
        # Wait for the next day at 6:00 AM
        time.sleep(60*60*24)
