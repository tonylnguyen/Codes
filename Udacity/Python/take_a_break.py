import webbrowser
import time

take_break = 0

while take_break != 3:
    time.sleep(2)
    webbrowser.open('https://www.youtube.com/watch?v=37Z_bIqIWpg')
    take_break = take_break + 1
