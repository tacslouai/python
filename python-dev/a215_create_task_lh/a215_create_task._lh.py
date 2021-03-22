#Background Source: https://www.flickr.com/photos/129875605@N07/34919107730
#Icon Sources:
#   Chrome: https://en.m.wikipedia.org/wiki/File:Google_Chrome_icon_(September_2014).svg
#   Windows Explorer: https://commons.wikimedia.org/wiki/File:Windows_Explorer_Icon.svg
#   Webull: https://win10storeapp.com/wp-content/uploads/2019/05/Webull-Invest-Smart-Trade-Free-Stocks-ETFs.-App-for-Windows-10-8-7-Latest-Version.png
#   Github Desktop: https://static.macupdate.com/products/39062/m/github-desktop-logo.webp

import turtle as trtl
import os

wn = trtl.Screen()
wn.setup(600, 600)
wn.bgpic('background2.gif')
icons = ['chrome.gif','explorer.gif', 'webull.gif','github.gif']
paths = ['C:\\Users\\lhammad\\AppData\\Local\\Google\\Chrome\\Application\\chrome.exe', 'C:\\Windows\\explorer.exe', 'C:\\Users\\lhammad\\AppData\\Local\\Programs\\Webull\\Webull.exe', 'C:\\Users\\lhammad\\AppData\\Local\\GitHubDesktop\\GitHubDesktop.exe']
icon_turts = []

def open_file(x, y):
    global icon_turts
    global paths

    for i in icon_turts:
        if(i.distance(x, y)<50):
            p = icon_turts.index(i)
            os.startfile(paths[p])

for icon in icons:
    temp_turt = trtl.Turtle()
    wn.register_shape(icon)
    temp_turt.shape(icon)
    temp_turt.penup()
    temp_turt.pensize(50)
    temp_turt.speed(0)
    temp_turt.goto(-250, 250-len(icon_turts)*75)
    icon_turts.append(temp_turt)

for turt in icon_turts:
    turt.onclick(open_file)


wn.mainloop()