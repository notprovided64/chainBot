import asyncio
from enum import Enum
import random
import sys
import time

from config import Config
from myio import *
from fishing import fish
from battle import handleBattle
from menu import swapToDoodle, resetDoodleOrder
from navigation import *
from discordBot import bot, getResponse, TOKEN

class GameState(Enum):
    FISHING = 1
    BATTLING = 2
    DONE = 3

async def bot_func():
    log("main", "doing bot stuff beeb ebpopwifwijwioagj")

async def main():
    config = Config("desktopConfig.toml")
    coords = config.coordinates
    party_moves = config.doodle_info["party_moves"]

    bot_task = asyncio.create_task(bot.start(TOKEN))

    await asyncio.sleep(5)
            
    _ = input("press enter to start")

    # focus the window
    moveClick(coords["tab"])

    await asyncio.sleep(0.2)

    # while(True):
    #     screen = screenshot(coords, top_half_only=True)
    #     if on_screen(screen, "images/target/moss.png"):
    #         print("yippee")

    #     _ = input("dawg")
            

    # while(False):
    while(True):
        for i, move_count in enumerate(party_moves):
            while(sum(move_count) != 0):
                fish(coords)
                await handleBattle(coords, move_count, getResponse)

            if i < 5:
                log("main", "swapping to next doodle")
                swapToDoodle(coords, i+1)
            else:
                log("main", "resetting doodle to original positions")
                resetDoodleOrder(coords)
                _ = input("done with script, press enter to restart")
                # config.load_config()
        # add logic for healing 
        
if __name__ == "__main__":
    asyncio.run(main())       
