import pyautogui
import keyboard
from time import sleep

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1291,722,(12,152,33)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1380,722,(254,15,23)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1466,722,(244,244,64)):
        pyautogui.press('j')
        sleep(0.05)