# ScreenshotApp

ScreenshotApp is a simple Python application that allows users to capture a portion of their screen and copy it to the clipboard. The application is triggered by a hotkey (Ctrl+Shift+S) and uses the `pyautogui` for capturing the screen.

## Features

- Fullscreen capture area with adjustable rectangle selection.
- Captured screenshot is automatically copied to the clipboard.
- Hotkey activation for easy access.

## How the App works:

1. Start the app, or the python script
2. Press `Ctrl+Shift+S` to activate the screen capture tool.
3. Click and drag to select the area you want to capture. The screenshot will be automatically copied to the clipboard.

## Prerequisites

- Python 3.x
- `tkinter` 
- `pyautogui` 
- `keyboard`
- `pywin32`

## Installation

You can clone the repostitory or download the source code.

Source code download:
![image](https://github.com/Dzynekz/ScreenshotApp/assets/128654056/72f149d3-2f0e-40c0-a7b5-26fd3354f358)




## Using Executable Version

An executable (.exe) version of this application is also available for Windows users. This allows you to run the application without installing Python or any dependencies.

## Using Python Script

1. In the folder with python script run:
   ```sh
   pip install -r requirements.txt
   ```
2. Run the script:
    ```sh
    python screenshot_app.py
    ```
