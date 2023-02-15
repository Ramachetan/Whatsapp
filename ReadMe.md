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
