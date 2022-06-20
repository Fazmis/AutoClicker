import keyboard
import pyautogui
import threading
pyautogui.FAILSAFE = False


def auto_click():
    while pause.wait():
        pyautogui.click()


def main():
    while True:
        keyboard.wait('Ctrl + Q')
        pause.set()
        keyboard.wait('Ctrl + Q')
        pause.clear()


pause = threading.Event()

thread1 = threading.Thread(target=auto_click)
thread2 = threading.Thread(target=auto_click)
thread3 = threading.Thread(target=auto_click)
thread4 = threading.Thread(target=main)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
