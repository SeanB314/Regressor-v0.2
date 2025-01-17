# Imports
import time 

# required stuff
d = 1

# Define classes
class Attribute():
    """Store a name and a level of an attribute."""
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def setLevel(self, int):
        self.level = int
        

class Timeline():
    """Store information relating to which turns have been completed."""
    def __init__(self, totalTurns):
        self.totalTurns = totalTurns
        self.turnIndex = 0
        self.turnList = [False for i in range(self.totalTurns)]
        self.turnList[0] = True
        self.branch = 0

    def advance(self):
        """Increment the turnIndex and mark that turn True so it can start."""
        self.turnIndex += 1
        self.turnList[self.turnIndex] = True

    def resetList(self):
        """Reset the timeline to the initial position."""
        self.turnList = [False for i in range(self.totalTurns)]
        self.turnList[0] = True

    def resetIndex(self):
        """Reset the turnIndex to 0."""
        self.turnIndex = 0

class Character():
    def __init__(self, name, base_max_force, essence = 0, attributes = [], inventory = []):
        self.name = name
        self.base_max_force = base_max_force
        self.max_force = base_max_force
        self.force = base_max_force
        self.essence = essence
        self.attributes = attributes
        self.inventory = inventory
        self.will = self.force / self.max_force * 100.

    def adjustWill(self):
        """Adjust will according to the current values for max_force and force. Round the value."""
        self.will = self.force / self.max_force * 100.
        self.will = round(self.will, 2)   

    def adjustEssence(self, amount):
        """Adjust essence, max_force, force, and will according to a gain or loss in essence. Round each value."""
        self.max_force += amount
        self.max_force = round(self.max_force, 2)
        self.force += amount
        self.force = round(self.force, 2)
        self.essence += amount
        self.essence = round(self.essence, 2)
        self.adjustWill()

    def checkAtts(self):
        """Print force, essence, attributes, and alignment. If there is nothing in the lists, print None."""
        print("\n")
        print(self.name)
        print("Force: \t\t" + str(self.force) + " (" + str(self.will) + "% Will)")
        print("Essence: \t" + str(self.essence))
        
        print("Attributes: \t")
        if self.attributes == []:
            print("\t" + "None")
        else:
            for att in self.attributes:
                if att.level == 0:
                    print("\t" + att.name)
                    continue
                print("\t" + att.name + " (" + str(att.level) + ")")
                
        print("Alignments: \t")
        if self.alignments == []:
            print("\t" + "None")
        else:
            for ali in self.alignments:
                print("\t" + ali.name)
        print("\n")

    def takeDamage(self, enemy_force):
        """Calculates damage taken and adjusts force and will accordingly."""
        self.force = self.force - enemy_force * 0.2
        if self.force < 0:
            self.force = 0
        self.adjustWill()

    def death(self, *args):
        """Die, giving essence (and items?) evenly to the characters who killed this character if applicable."""
        bounty = self.max_force / len(args)
        for ar in args:
            ar.adjustEssence(bounty)
            print("[" + ar.name + " has gained " + str(round(bounty, 2)) + " essence.]")
            time.sleep(d)
        print("\n")

    def heal(self):
        """Sets force to max_force."""
        self.force = self.max_force
        self.adjustWill()


class KeyCharacter(Character):
    """A more important character with some additional functions"""
    def __init__(self, name, base_max_force, essence = 0, attributes = [], inventory = [], alignments = [], trust = 50):
        self.name = name
        self.base_max_force = base_max_force
        self.max_force = base_max_force
        self.force = base_max_force
        self.essence = essence
        self.attributes = attributes
        self.inventory = inventory
        self.will = self.force / self.max_force * 100.

        # Additional attributes
        self.alignments = alignments

        # KeyCharacter specific attributes
        self.trust = trust

    def checkInv(self):
        """Print inventory."""
        print("\n")
        print(self.name)
        print("Inventory:")
        if self.inventory == []:
            print("\t" + "Empty")
        else:
            for i, entry in enumerate(self.inventory):
                print(self.inventory[i])
        print("\n")

    def adjustEssence(self, amount):
        """Like the previous adjustEssence function, but accounts for limits imposed by the SOUL attribute."""
        for att in self.attributes:
            if att.name == "SOUL":
                soulLevel = att.level

        super().adjustEssence(amount)

        if self.max_force >= (10. ** (soulLevel + 1)) or self.force > (10. ** (soulLevel + 1)):
            self.max_force = (10. ** (soulLevel + 1))
            self.force = (10. ** (soulLevel + 1))
            self.adjustWill()
        else:
            self.max_force = self.base_max_force + self.essence
            self.adjustWill()

    def checkAtts(self):
        """Like the previous checkAtts, except refreshes force and max_force first to account for possible changes in the SOUL attribute."""
        self.adjustEssence(0)
        super().checkAtts()


class Player(KeyCharacter):
    def __init__(self, name, base_max_force, essence = 0, attributes = [], inventory = [], alignments = []):
        self.name = name
        self.base_max_force = base_max_force
        self.max_force = base_max_force
        self.force = base_max_force
        self.essence = essence
        self.attributes = attributes
        self.inventory = inventory
        self.will = self.force / self.max_force * 100.
        self.alignments = alignments

        # Player specific attributes
        self.awareness = 0
        self.regressions = 0

    def death(self, *args):
        """Prints some lines, increments regression counter and resets timeline."""
        self.regressions += 1
        time.sleep(d)
        print("No...")
        time.sleep(d)
        print("[You have shattered!]")

    def regress(self):
        """Print lines. Reset max_force, force, will, essence, attributes, alignments, and inventory to initial positions."""
        regressor = Attribute("REGRESSOR", 0)
        soul = Attribute("SOUL", 1)

        self.base_max_force = 10.
        self.max_force = self.base_max_force
        self.force = self.base_max_force
        self.adjustWill()
        self.essence = 0
        self.attributes = [regressor, soul]
        self.alignments = []
        self.inventory = []

        time.sleep(d*2)
        print("\n")
        print("[You have regressed.]")
        time.sleep(d)
        print("...What?\n")