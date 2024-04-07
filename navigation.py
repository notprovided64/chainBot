from myio import click, moveClick, moveTo, hold_keys
import time
import pyautogui as auto

def goToLake():
    hold_keys(["shift", "d"], 2.1)
    hold_keys(["shift", "d", "s"], 1)
    hold_keys(["shift", "d"], 1)
    
    moveClick([1452, 298])

    for _ in range(10):
        auto.scroll(-10)

    moveTo([1452, 488])

def goToCenter():
    hold_keys(["shift", "a"], 1)
    hold_keys(["shift", "a", "w"], 1)
    hold_keys(["shift", "a"], 2.1)
    hold_keys(["shift", "s"], 1)
    
def navigatePokecenter(coords):
    moveClick(coords["healing"])
    time.sleep(0.5)

    #walking forward to the attendant
    hold_keys(["w"], 1.33)
    
    click() # start conversation
    time.sleep(1)

    click() # hello and welcome to doodleco
    time.sleep(1)

    click() # i can heal
    time.sleep(0.5)

    moveClick(coords["yes_button"]) 
    time.sleep(1)
    
    click() # okay i'll take your
    time.sleep(5)

    click() # now i have to
    time.sleep(3)

    click() # time to turn
    time.sleep(3.5)

    click() # all done
    time.sleep(2)

    click() # hope to see
    time.sleep(0.5)

    hold_key("s", 1.5)
