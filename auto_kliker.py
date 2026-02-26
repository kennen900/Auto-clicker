import pyautogui
import time
import keyboard
import threading

kliker = float(input("Podaj z jaką prędkością ma klikać: "))

running = False
paused = False
key = False
wybur = ''

def auto_click():
    global running, paused
    while True:
        if key:
            pyautogui.press(wybur)
            time.sleep(kliker)
        if running and not paused:
            pyautogui.click()
            time.sleep(kliker)
        else:
            time.sleep(0.01)



thread = threading.Thread(target=auto_click)
thread.daemon = True
thread.start()

print("[ - start | ] - stop | ; - pauza | 1 - kontynuuj | . - dowolny wybrany klawisz")

while True:
    if keyboard.is_pressed('['):
        running = True
        print("Start")
        time.sleep(0.2)

    elif keyboard.is_pressed(']'):
        running = False
        print("Stop")
        break

    elif keyboard.is_pressed(';'):
        paused = True
        print("Pauza")
        time.sleep(0.2)

    elif keyboard.is_pressed('1'):
        paused = False
        print("Kontynuacja")
        time.sleep(0.2)

    elif keyboard.is_pressed('.'):
        key = True
        wybur = input("Podaj klawisz: ")