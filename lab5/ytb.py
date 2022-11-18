import pyautogui
import keyboard
import time


def scrollpage():
    pyautogui.moveTo(540, 877)
    time.sleep(2)
    pyautogui.scroll(-335)


def refreshTime():
    time.sleep(2)
    pyautogui.click(106, 61)
    time.sleep(2)


def bot_watcher():
    steps = 0
    while (steps < 3):
        for i in range(steps):
            refreshTime()
        for i in range(steps):
            scrollpage()
        pyautogui.click(540, 877)
        time.sleep(4)
        pyautogui.click(26, 61)  # back button
        time.sleep(3)
        for i in range(steps):
            refreshTime()
        for i in range(steps):
            scrollpage()
        pyautogui.click(910, 877)
        time.sleep(4)
        pyautogui.click(26, 61)  # back button
        time.sleep(3)
        for i in range(steps):
            refreshTime()
        for i in range(steps):
            scrollpage()
        pyautogui.click(1296, 877)
        time.sleep(4)
        pyautogui.click(26, 61)  # back buttons
        time.sleep(3)
        for i in range(steps):
            refreshTime()
        for i in range(steps):
            scrollpage()
        pyautogui.click(1648, 877)
        time.sleep(4)
        pyautogui.click(26, 61)  # back button
        steps = steps + 1


def press_channel_subscribe():
    time.sleep(2)
    dan = pyautogui.locateOnScreen(
        r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\danZona.png', confidence=0.7)
    pyautogui.click(dan)
    time.sleep(4)
    # subscribe = pyautogui.locateOnScreen(
    # r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\subscribe.png', confidence = 0.7)
    # time.sleep(1)
    # pyautogui.click(subscribe)
    videos = pyautogui.locateOnScreen(
        r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\videos.png', confidence=0.7)
    time.sleep(2)
    pyautogui.click(videos)
    time.sleep(3)
    bot_watcher()


def search_zona():
    if pyautogui.locateOnScreen(r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\ytbSearch.png', confidence=0.9) != None:
        youtubeBar = pyautogui.locateOnScreen(
            r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\ytbSearch.png', confidence=0.9)
        pyautogui.click(youtubeBar)
        pyautogui.write("Zona")
        pyautogui.press('enter')
        time.sleep(4)
        press_channel_subscribe()
    else:
        print("nu gaseste bara search youtube")


def cautare_google():
    if pyautogui.locateOnScreen(r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\searchbar.png', confidence=0.7) != None:
        camp_google = pyautogui.locateOnScreen(
            r'C:\Users\Sebi\Desktop\UB\Inteligenta-Artificiala\lab5\searchbar.png', confidence=0.7)
        pyautogui.click(camp_google)
        pyautogui.write("https://youtube.com")
        pyautogui.press('enter')
        time.sleep(5)
        print("Imaginea se afla pe ecran")
        search_zona()
    else:
        print("Imaginea nu se afla pe ecran")


def coordonate():
    print(pyautogui.position())


time.sleep(2)
cautare_google()
