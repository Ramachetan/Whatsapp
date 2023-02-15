## USER
import pyautogui
import time

# Set the phone number and message to send
phone_number = "+91 93815 72034"
message = "Hello, World!"

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

I have this code how to make a windows application out of it

## ASSISTANT


To create a Windows application out of this code, you can use a framework like PyInstaller, which can package Python scripts as standalone executable files for Windows, Linux, or macOS.

Here are the steps to create a Windows application using PyInstaller:

1. Install PyInstaller:
   Open a command prompt and type the following command:
   
   ```
   pip install pyinstaller
   ```

2. Create a folder and copy your Python script (`whatsapp.py`) into it.

3. Open a command prompt and navigate to the folder where your script is located.

4. Type the following command to create an executable file:
   ```
   pyinstaller --onefile whatsapp.py
   ```

   This will create a folder named `dist` containing the executable file `whatsapp.exe`.

5. Double-click the `whatsapp.exe` file to run the application.

Note: The above steps assume that you have a working version of Python and pip installed on your system. If not, you will need to install them before proceeding with the above steps.

## USER
write a github read me file based on that

## ASSISTANT
Sure, here's an example README file for your GitHub project:

# WhatsApp Message Scheduler

This is a Python script that uses the PyAutoGUI library to automate sending WhatsApp messages at a scheduled time. 

## Installation

To use this script, you will need to have Python 3.x and the PyAutoGUI library installed on your system. You can install PyAutoGUI using pip:

```
pip install pyautogui
```

You can then download or clone the `whatsapp_scheduler.py` file from this repository.

## Usage

1. Set the phone number and message to send by editing the `phone_number` and `message` variables in the script.

2. Set the time to send the message (in 24-hour format) by editing the `send_time` variable in the script.

3. Run the script using the following command:

   ```
   python whatsapp_scheduler.py
   ```

   The script will wait until the scheduled time to send the message, then open the WhatsApp app and send the message to the specified phone number.

## Creating a Windows Application

If you want to create a standalone Windows application from this script, you can use the PyInstaller library. 

1. Install PyInstaller using the following command:

   ```
   pip install pyinstaller
   ```

2. Run the following command to create a standalone executable file:

   ```
   pyinstaller --onefile whatsapp_scheduler.py
   ```

   This will create a `dist` folder containing the executable file. Double-click the `whatsapp_scheduler.exe` file to run the application.

## Limitations

This script currently only works with the Windows version of WhatsApp. It may not work with future versions of the app, as the user interface may change. Use this script at your own risk, as it may violate WhatsApp's terms of service.

## Credits

This script was created by [Your Name Here]. The PyAutoGUI library is maintained by Al Sweigart.

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use and modify the code as you see fit.