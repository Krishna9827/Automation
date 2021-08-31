from tkinter import Scrollbar
import pyautogui
import time

time.sleep(3)

#Mouse Functions
print(pyautogui.size()) #prints the screen resolution. # Size(width=1366, height=768)
print(pyautogui.position()) #Point(x=-122, y=6) Currents mouse coordinates.

pyautogui.FAILSAFE = True

#(x-coordinate, y-coordinate, time taken to move.)
#pyautogui.moveTo(670,375,3) #ye 3 time hai ya animation you can say

# Move the mouse relative to its current postition
#pyautogui.moveRel(100,100, 3)

#Click  ((no. of clicks , 1st 3, 2nd 3 is duration))
#pyautogui.tripleClick()
#pyautogui.click(670,375, 3, 3, button="left") 
#pyautogui.doubleClick()
#pyautogui.leftClick()
#pyautogui.rightClick()

#Scrolls up 500
#pyautogui.scroll(500)     # scroll up 500 "clicks"
#Scrolls down -500
#pyautogui.scroll(-500)     # scroll down -500 "clicks"
#pyautogui.hscroll(10)   # scroll right 10 "clicks"
#pyautogui.hscroll(-10)   # scroll left 10 "clicks"
#pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

#mouse drag up down
#pyautogui.mouseUp(120, 120, button="left")
#pyautogui.mouseDown(120, 120, button="left")

#example of mouse up and down
#pyautogui.mouseDown(300, 400, button="left")
#pyautogui.moveTo(800,400, 3)
#time.sleep(1) #for the delay after draging
#pyautogui.mouseUp()
#pyautogui.moveTo(1000, 400, 3)

#Spiral drawing using pyautogui
#distance = 300
#while distance > 0:
#time.sleep(1)
#    pyautogui.dragRel(distance, 0 , 1, button="left")
#    distance = distance - 20
#    pyautogui.dragRel( 0  ,distance, 1, button="left")
#    pyautogui.dragRel(-distance, 0 , 1, button="left")
#    distance = distance - 20 
#    pyautogui.dragRel( 0  ,-distance, 1, button="left")
#    time.sleep(1)

#To abort the code in between we have to move our mouse to any 1 corner of the screen





#Project 1 (liker)
#time.sleep(2)
#range will be the number of things you want to like
#for i in range(5):
#    pyautogui.moveTo(x=-1187, y=306)
#    time.sleep(1)
#    pyautogui.doubleClick()
#    time.sleep(1)
#    pyautogui.scroll(-800)
#    time.sleep(1)
#    pyautogui.leftClick()
#    time.sleep(1)







#Keyboard Functions
#pyautogui.write("Hello")
#pyautogui.press("enter")
#pyautogui.press("space")


#Dino Game - Chrome
#time.sleep(1)
#for i in range (100):
#    pyautogui.press("space")                                                                                                    




# Screenshot in pyatogui
#pyautogui.screenshot("ss.png")

