from time import sleep
import pyautogui


ACCEPT = 'accept.png'


def search(image):
    try:
        acceptButton = pyautogui.locateOnScreen(image)
        clickButton = pyautogui.center(acceptButton)
    except:
        return pyautogui.Point(x=0, y=0)
    return clickButton


def click(image):
    clickButton = wait_for_appearance(image)
    pyautogui.click(clickButton)


def wait_for_appearance(image):
    while (clickButton:=search(image)) == pyautogui.Point(x=0, y=0):
        sleep(1)
    return clickButton


def queue():
    print('Waiting for Queue pop...')
    click(ACCEPT)


def main():
    queue()

    
if __name__ == '__main__':
    main()
