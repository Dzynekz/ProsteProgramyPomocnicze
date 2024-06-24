import tkinter as tk
import pyautogui
import keyboard
import io
import win32clipboard
import time
import threading




class ScreenCaptureApp:
    def __init__(self, root):
        self.root = root
        self.root.withdraw()  # Hide main window
        self.capture_area = None
        self.rect = None
        self.start_x = self.start_y = 0

    def capture_screen(self):
        self.capture_area = tk.Toplevel(self.root)
        self.capture_area.attributes('-fullscreen', True)
        self.capture_area.attributes('-alpha', 0.3)

        # Using Canvas to draw the rectangle
        self.canvas = tk.Canvas(self.capture_area, cursor="cross")
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind('<Button-1>', self.on_button_press)
        self.canvas.bind('<B1-Motion>', self.on_move_press)
        self.canvas.bind('<ButtonRelease-1>', self.on_button_release)

    def on_button_press(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline='red', width=2)

    def on_move_press(self, event):
        cur_x, cur_y = (event.x, event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, cur_x, cur_y)

    def on_button_release(self, event):
        end_x, end_y = (event.x, event.y)
        self.capture_area.destroy()  # Destroy the window

        x1 = min(self.start_x, end_x)
        y1 = min(self.start_y, end_y)
        x2 = max(self.start_x, end_x)
        y2 = max(self.start_y, end_y)

        # Interception of the screenshot of the area
        screenshot = pyautogui.screenshot(region=(x1, y1, x2-x1, y2-y1))

        # Conversion of the picture to the format compatible with clipboard
        output = io.BytesIO()
        screenshot.save(output, format='BMP')
        data = output.getvalue()[14:]
        output.close()

        # Copying an image to the clipboard
        win32clipboard.OpenClipboard()
        win32clipboard.EmptyClipboard()
        win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
        win32clipboard.CloseClipboard()

        print("Screenshot saved to clipboard.")
        self.root.withdraw()  # Hide main window

        
def on_hotkey():
    print("hotkey activated")
    root.after(0, app.capture_screen)

root = tk.Tk()
app = ScreenCaptureApp(root) 

def main():
    keyboard.add_hotkey('ctrl+shift+s', on_hotkey, suppress=True, trigger_on_release=True)
    while True:
        time.sleep(1)  # Prevents 100% CPU usage

# Run the main loop in a separate thread
threading.Thread(target=main, daemon=True).start()
root.mainloop()