# Imports
import time

# d 
d = 1

# Define functions    
def isDead(char):
    """Accepts a character and returns True if it is dead, i.e. will is 0."""
    if char.will <= 0:
        return True
    return False

def inputLoop(player, *args, endTurn = []):
    """Accepts the player, strings as arguments, and a list of booleans called endTurn, which indicates if the choice ends the turn. Prints the 
    next choice, accepts player input, facilitates viewing stats and attributes, and returns a string of the user input."""
    loop = True
    options = ""
    while loop:
        print("[Choose an action:]")
        for i, ar in enumerate(args):
            options = options + str(i + 1)
            if endTurn[i]:
                print("[" + str(i + 1) + " - " + ar + "] [END TURN]")
            else:
                print("[" + str(i + 1) + " - " + ar + "]")
        print("[a - Check attributes]")
        print("[i - Check inventory]")
        print("\n")

        inputStr = input()

        if inputStr == "a":
            player.checkAtts()
            
        elif inputStr == "i":
            player.checkInv()
            
        elif inputStr == "quit":
            loop = False
            return "quit"
            
        elif inputStr in options:
            loop = False
            return inputStr
            
        else:
            print("Invalid input.")
            print("\n")
            time.sleep(d)
    
def get_battle(char1, char2):
    """Determines which battle function to use based on the attributes of the two given characters."""
    execute = False
    resilience = False

    for att in char1.attributes + char2.attributes:
        if att.name == "EXECUTE":
            execute = True
        if att.name == "RESILIENCE":
            resilience = True

    if execute and resilience:
        print("Adjusted battle function goes here")
        # Unfinished
        return None
        
    elif execute:
        print("Adjusted battle function goes here")
        # Unfinished
        return None
        
    elif resilience:
        print("Adjusted battle function goes here")
        # Unfinished
        return None
        
    else:
        # Default battle function
        def battle(char1, char2):
            """Accepts two characters as arguments and prints the ensuing battle."""

            while char1.will > 0 and char2.will > 0:
                time.sleep(d)
                print(char1.name + "\'s Force (% Will)" + "\t\t" + char2.name + "\'s Force (% Will)")
                print(str(round(char1.force, 2)) + " (" + str(round(char1.will, 2)) + "%)" + "\t\t\t" 
                      + str(round(char2.force, 2)) + " (" + str(round(char2.will, 2)) + "%)")
                temp = char1.force
                char1.takeDamage(char2.force)
                char2.takeDamage(temp)
        
                if isDead(char1) or isDead(char2):
                    time.sleep(d)
                    print(char1.name + "\'s Force (% Will)" + "\t\t" + char2.name + "\'s Force (% Will)")
                    print(str(round(char1.force, 2)) + " (" + str(round(char1.will, 2)) + "%)" + "\t\t\t" + str(round(char2.force, 2))
                        + " (" + str(round(char2.will, 2)) + "%)")
            
                    if isDead(char1):
                        time.sleep(d)
                        print("[" + char2.name + " has shattered " + char1.name + ".]")
                        char1.death(char2)
        
                    elif isDead(char2):
                        print("[" + char1.name + " has shattered " + char2.name + ".]")
                        char2.death(char1)
        return battle