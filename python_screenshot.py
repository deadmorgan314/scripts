import pyautogui
import time

def screen():
    filename = str(time.time()).split(".")[0] + ".png"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)

screen()