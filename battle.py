import asyncio
from myio import *
import sys
import time
from misc import first_nonzero_index

async def handleBattle(coords, move_count, bot_function):
    log("battle", "checking to see if ready to fight")
    for _ in range(100):
        screen = screenshot(coords)
        if on_screen(screen, "images/ready.png"):
            log("battle", "ready to handle battle")
            time.sleep(0.3)
            break
        time.sleep(0.2)
    else:
        hotkey("shift", "ctrl", "2")
        _ = input("press enter to resume")
        moveClick(coords["menu_party"])
        return
    
    screen = screenshot(coords, True)

    caught_icon = on_screen(screen, 'images/caught.png')
    uncaught_icon = on_screen(screen, 'images/uncaught.png')

    is_target = match_in_folder(screen, "images/target")
    ignore = match_in_folder(screen, "images/ignore") or caught_icon or uncaught_icon

    log("battle", f"{caught_icon=} {uncaught_icon=} {is_target=} {ignore=}")

    if is_target:
        log("battle", "killing")
        kill(coords, move_count)
    elif ignore:
        log("battle", "running")
        run(coords)
    else:
        log("battle", "should get ping")
        await handlePotentialTint(coords, move_count, bot_function)

    log("battle", f"finished battle {move_count=}")
    waitForEnd(coords)

async def handlePotentialTint(coords, move_count, bot_function):
    record_gif(coords["gif_top_left"], coords["gif_width"], coords["gif_height"], "test.gif")

    while(True):
        response = await bot_function()

        match response:
            case 1:
                while(True):
                    await asyncio.sleep(10)
                    moveClick(coords["menu_party"])
            case 2:
                run(coords)
                break
            case 3:
                kill(coords, move_count)
                break
            case 4:
                #take screenshot of doodle and add it to the target list
                addToTargetList(coords)
                await asyncio.sleep(2)
                kill(coords, move_count)
                break
            case None:
                moveClick(coords["menu_party"])
                continue
                
def waitForEnd(coords):
    while(True):
        screen = screenshot(coords)
        if on_screen(screen, "images/menu.png"):
            log("battle", "menu spotted")
            break
        time.sleep(0.2) 
    time.sleep(0.5)      
    
def run(coords):
    time.sleep(0.3)
    while(True): # TODO irl lookup insert mode shortcuts for helix
        moveClick(coords["run_button"])
        time.sleep(2)

        screen = screenshot(coords)
        if not on_screen(screen, "images/battle_settings.png"):
            break
            

# something is fucked here, two moves in one turn + 1 remaining doesnt work for some reason
def kill(coords, move_count):
    while(True):
        moveIndex = first_nonzero_index(move_count)
    
        time.sleep(0.5)

        attackAtIndex(coords, move_count, moveIndex)
    
        time.sleep(8)

        screen = screenshot(coords)
        if not on_screen(screen, "images/battle_settings.png"):
            break
        elif on_screen(screen, "images/replace_move.png"):
            time.sleep(1)
            moveClick(coords["cancel_replace_move"])
            time.sleep(1)
            click() 
            break       

def attackAtIndex(coords, move_count, index):
    moveClick(coords["fight_button"])

    moveLocation = coords["attack"].copy()

    for _ in range(index):
        moveLocation[0] += coords["attack_offset"]

    time.sleep(0.5)

    moveClick(moveLocation)
    move_count[index] -= 1
    
