import pyautogui
import time


def gift():
    time.sleep(2)
    pyautogui.click(x=981, y=616)
    time.sleep(0.3)
    pyautogui.click(x=966, y=903)
    time.sleep(0.3)
    pyautogui.click(x=985, y=939)
    time.sleep(0.3)
    pyautogui.click(x=998, y=644)
    pyautogui.click()
    gift()


pyautogui.failSafeCheck()
gift()