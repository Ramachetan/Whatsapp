import pyautogui
import time

# Set the phone number and message to send
phone_number = "Your_Number"
message = "Your_Message"

# Set the time to send the message (in 24-hour format)
send_time = "12:36:00"

# Wait until the send time is reached
while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == send_time:
        break
    time.sleep(1)

# Open the WhatsApp app and click on the new message button
pyautogui.hotkey('win', 's')
pyautogui.write('WhatsApp')
pyautogui.press('enter')
time.sleep(5)  # wait for WhatsApp to open
pyautogui.click(200, 200)  # click on the new message button

# Type the phone number and message, and send the message
pyautogui.write(phone_number)
pyautogui.press('enter')
time.sleep(2)  # wait for the chat to open
pyautogui.write(message)
pyautogui.press('enter')
