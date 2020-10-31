'''
import pyautogui
print(pyautogui.size())
import pyautogui 
pyautogui.moveTo(100, 500)
pyautogui.click(clicks = 2)
'''

from pynput.mouse import Listener


xPos = []
yPos = []


def on_click(x, y, button, pressed):
    #print(x, y, button, pressed)
    if(pressed):
        xPos.insert(0, x)
        yPos.insert(0, y)
        print(xPos, yPos)
        if(len(xPos) > 5):
            xPos.pop(4)
            yPos.pop(4)




with Listener(on_click=on_click) as listener:
    listener.join()
