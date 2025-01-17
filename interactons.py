# imports
import time

# d
d = 1

def ternanIntro(ternan):
    """Accepts ternan as input, plays the first interaction with Ternan, returns the new ternan with updated stats and an input
    string."""
    # Unfinished
    loop1 = True
    route = 0
    while loop1:
        print("1 - Who are you?")
        print("2 - [Attack] [END INTERACTION]")
        print("\n")

        inputStr = input()

        if inputStr == "1":
            print("Who are you?\n")
            time.sleep(d)
            print("[Unknown]:")
            time.sleep(d)
            print("\"...I am Ternan.\"")
            time.sleep(d)
            print("[Ternan]:")
            time.sleep(d)
            print("\"Please...have mercy. I have little essence.\"")
            print("\n")
            time.sleep(d)
            loop1 = False
            
        elif inputStr == "2":
            loop1 = False
            return ternan, inputStr

        else:
            print("Invalid input.")
            print("\n")

    loop2 = True
    while loop2:
        print("1 - Don't be afraid. I won't hurt you.")
        print("2 - Tell me why I shouldn't kill you.")
        print("\n")

        inputStr = input()

        if inputStr == "1":
            ternan.trust += 10
            print("Don't be afraid. I won't hurt you.\n")
            time.sleep(d)
            print("[Ternan's fear subsides.]")
            time.sleep(d)
            print("\"Who are you?\"")
            print("\n")
            time.sleep(d)
            route = 1
            loop2 = False

        elif inputStr == "2":
            ternan.trust -= 10
            print("Tell me why I shouldn't kill you.")
            time.sleep(d)
            print("[Ternan is shaking.]")
            time.sleep(d)
            print("\"I am weak...but I can become strong!\"")
            print("\n")
            time.sleep(d)
            route = 2
            loop2 = False

        else: 
            print("Invalid input.")
            print("\n")

    loop3 = True
    if route == 1:
        print("1 - ")
            
            








