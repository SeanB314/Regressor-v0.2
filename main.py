# Imports
import time
from classes import *
from narrative import *


# Initial setup
d = 1
totalTurns = 5
running = True
timeline = Timeline(totalTurns)
regressor = Attribute("REGRESSOR", 0)
soul = Attribute("SOUL", 1)


# Gameplay 
name = input("Enter player name: ")
player = Player(name, 10., attributes = [regressor, soul]) 

while running:
    # If regressing, reset stats, timeline, and turn index.
    if player.regressions > 0:
        timeline.resetIndex()
        player.regress()

    # TEMPORARILY SKIP TURNS - REMOVE LATER
    # for i in range(4):
    #     timeline.turnList[i] = True
    #     timeline.turnIndex = 3

    # TEMPORARILY PRESET PLAYER STATS - REMOVE LATER
    # player.adjustEssence(45)
    
    # Turn 1
    if timeline.turnList[0]:
        player, timeline = turn1(player, timeline)
        
    # Turn 2
    if timeline.turnList[1]:
        player, timeline = turn2(player, timeline)

    # Turn 3
    if timeline.turnList[2]:
        player, timeline = turn3(player, timeline)

    # Turn 4 
    if timeline.turnList[3]:
        player, timeline = turn4(player, timeline)

    # End the game if all the turns have been completed.
    if all(timeline.turnList):
        break

    # End the game if the player chooses to quit.
    if timeline.turnList[timeline.turnIndex] and timeline.turnList[timeline.turnIndex + 1] == False:
        break