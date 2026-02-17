import pyautogui
import time
import keyboard

kliker = float(input("Podaj z jak predkoscia ma klikac "))
wlacznik = input("[ - by odpalic, ] - by wylaczyc, ; - przerwa, 1 - kontynuluj, lub inny przycisk zostaw puste ")

while wlacznik == '[':
    if keyboard.is_pressed(']'):
        print("koniec")
        break
    elif keyboard.is_pressed(";"):
        while True:
            if keyboard.is_pressed('1'):
                break
            if keyboard.is_pressed(']'):
                print("koniec")
                break
        
    pyautogui.click()
    pyautogui.PAUSE = kliker

if wlacznik == '':
    przycisk = input("Podaj przycisk ")
    while True:
        if keyboard.is_pressed(']'):
            print("koniec")
            wlacznik == ']'
            break
        pyautogui.press(przycisk)
        pyautogui.PAUSE = kliker


    

    
