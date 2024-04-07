from myio import *
import time

def fish(coords):
    log("fishing", "started fishing")
    time.sleep(0.5)
  
    while True:
        moveTo(coords["center"])
        click()
        time.sleep(0.5)

        while True:
            screen = screenshot(coords)
            if on_screen(screen, 'images/catch2.png'):
                if handle_catch(coords):
                    time.sleep(4.5)
                    return
                else:
                    break
                
            if on_screen(screen, 'images/nothing2.png'):
                log("fishing", "nothing biting")
                dismiss_message(coords)

            time.sleep(0.1)

def handle_catch(coords):
    log("fishing", "got a bite")
    time.sleep(0.8)
    click()

    log("fishing", "starting fishing minigame")
    fishing_minigame(coords)

    time.sleep(0.5)
    screen = screenshot(coords)
    if not on_screen(screen, "images/fishing_success.png"):
        log("fishing", "failed minigame")
        return False
        
    log("fishing", "caught fish")
    dismiss_message(coords)
    return True  
  
def fishing_minigame(coords):
    time.sleep(2.45)
    moveClick(coords["reel_button"])
  
def dismiss_message(coords):
    time.sleep(0.75)
    click()
  
def check_for_battle(coords):
    for i in range(3):
        time.sleep(5.5)
        screen = screenshot(coords)
        if not on_screen(screen, "images/battle_settings.png"):
            log("fishing", "didn't")
            continue
  
        log("fishing", "caught fish")
        return