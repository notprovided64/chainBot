from myio import moveClick, drag, hotkey
import time

def resetDoodleOrder(coords):
    enterPartyMenu(coords)
    for i in range(5):
        moveDoodle(coords, i, i+1)
        # time.sleep(0.2)
        
    exitPartyMenu(coords)

def swapToDoodle(coords, index):
    enterPartyMenu(coords)

    moveDoodle(coords, index, 0)
    time.sleep(0.5)

    exitPartyMenu(coords)

def moveDoodle(coords, index1, index2):
    drag(getDoodlePartyPosition(coords, index1), getDoodlePartyPosition(coords, index2))

def enterPartyMenu(coords):
    hotkey("tab")
    time.sleep(1)

    moveClick(coords["menu_party"])
    time.sleep(1)

def exitPartyMenu(coords):
    moveClick(coords["party_exit"])
    time.sleep(0.8)

    hotkey("tab")
    time.sleep(1)
    
def getDoodlePartyPosition(coords, index):
    position = coords["party_lead"].copy()
    
    h_index = index % 2
    v_index = int(index/2)

    position[0] += h_index * coords["party_h_offset"]
    position[1] += v_index * coords["party_v_offset"]
    
    return position
 
