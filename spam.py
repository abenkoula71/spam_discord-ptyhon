import pyautogui as auto
import time
time.sleep(2)
while True:
    auto.write('Hello word')
    auto.press('enter')
    time.sleep(1)
