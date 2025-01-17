# Imports
import time
from classes import Character
from functions import *
from interactions import *

# Time step
d = 1

# Turns
def turn1(player, timeline):
    """Turn 1. Accepts the player and the timeline. Adjusts the player according to the scenario and adjusts the timeline according to if the 
    scenario has been completed or if quitting."""
    
    # Opening narrative
    if player.regressions == 0:
        time.sleep(d)
        print("*in*")
        time.sleep(d)
        print("*out*")
        time.sleep(d)
        print("Breathe.")
        time.sleep(d)
        print("Power wins the game.\n")
        time.sleep(d)

    # Turn 1
    time.sleep(d)
    print("[Turn 1]\n")
    time.sleep(d)
    
    inputStr = inputLoop(player, "Gather nearby essence (10)", "Wait", endTurn = [True, True])

    if inputStr == "1":
        print("[Gained 10 essence.]")
        print("\n")
        player.adjustEssence(10)
        timeline.advance()
    
    elif inputStr == "2":
        print("[Waiting.]")
        print("\n")
        timeline.advance()

    elif inputStr == "quit":
        return player, timeline
            
    return player, timeline

def turn2(player, timeline):

    time.sleep(d)
    print("[Turn 2]\n")
    time.sleep(d)

    inputStr = inputLoop(player, "Gather nearby essence (10)", "Wait", endTurn = [True, True])

    if inputStr == "1":
        print("[Gained 10 essence.]")
        print("\n")
        player.adjustEssence(10)
        timeline.advance()
    
    elif inputStr == "2":
        print("[Waiting.]")
        print("\n")
        timeline.advance()

    elif inputStr == "quit":
        return player, timeline
            
    return player, timeline

def turn3(player, timeline):
    enemy = Character("[Unknown]", 25.)

    time.sleep(d)
    print("[Turn 3]\n")
    time.sleep(d)
    print("[An unknown force is attacking!]")
    time.sleep(d)
    print("[You must defend yourself!]")
    battle = get_battle(player, enemy)
    battle(player, enemy)

    if isDead(player):
        timeline.resetList()
        return player, timeline
    else:
        print("[You have defeated the unknown force.]\n")

        inputStr = inputLoop(player, "Continue", endTurn = [True])
        
        if inputStr == "1":
            print("[Continue.]")
            print("\n")    
            player.heal()
            timeline.advance()

        elif inputStr == "quit":
            return player, timeline
                
    return player, timeline

def turn4(player, timeline):
    time.sleep(d)
    print("[Turn 4]\n")
    time.sleep(d)
    print("[There is no more essence nearby.]")
    time.sleep(d)
    print("[With the gathered essence, your senses begin to sharpen.]")
    time.sleep(d)
    print("[In one direction you detect several presences of various strengths.]")
    time.sleep(d)
    print("[In another direction there is a faint presence that radiates desperation.]\n")

    inputStr = inputLoop(player, "Pursue the cluster of presences", "Pursue the faint presence", endTurn = [False, False])

    if inputStr == "1":
        print("[Pursue the cluster of presences.]")
        print("\n")

    elif inputStr == "2":
        timeline.branch = 1
        print("[Pursue the faint presence.]")
        print("\n")

    elif inputStr == "quit":
        return player, timeline

    # Timeline: abandon Ternan
    if timeline.branch == 0:
        enemyChosen = 0
        time.sleep(d)
        print("[Many presences are battling.]")
        time.sleep(d)
        print("[[Unknown] has shattered [Unknown]!]")
        time.sleep(d)
        print("[[Unknown] has shattered [Unknown]!]")
        print("\n")

        inputStr1 = inputLoop(player, "Target mid-strength presence", "Target weak presence", "Escape", endTurn = [False, False, True])

        if inputStr1 == "1":
            enemyChosen = 1
            print("[Target mid-strength presence.]")
            print("\n")

        elif inputStr1 == "2":
            enemyChosen = 2
            print("[Target weak presence.]")
            print("\n")

        elif inputStr1 == "3":
            print("[Escape.]")
            print("\n")

        elif inputStr1 == "quit":
            return player, timeline

        # if enemyChosen == 1:
            

        
        
    # Timeline: find Ternan
    # if timeline.branch == 1:
        
        
    
        
    



    return player, timeline