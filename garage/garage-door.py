import os
import requests
from dotenv import dotenv_values

DOOR = dotenv_values('.door')

def main():
    print()
    note_exists = os.path.exists("garage-door-note.md")
    if note_exists == True:
        inner_garage_exists = os.path.exists("/inside-the-garage")
        if inner_garage_exists == True:
            print("The door's already unlocked. Not much else to see here.")
            print()
        else:
            user_code = input("Please enter 4-digit passcode: ")
            print()
            if user_code == DOOR["CODE"]:
                print("That is correct. Unlocking garage...")
                print()
                #NEED TO ADD GARAGE FOLDER
            else:
                print("Sorry, that is incorrect.")
                print()
    else:
        print("The garage door is firmly locked.")
        print("You see a keypad that takes a 4-digit code...")
        print("...but you don't remember The Landlord giving you any codes...")
        print()
        print("However, you do see a note taped on the door.")
        print()
        note = requests.get("https://raw.githubusercontent.com/term-world/world-flavor/main/garage-door-note.md")
        note_stringified = str(note.text)
        new_file = open("garage-door-note.md", "x")
        new_file.write(note_stringified)
        new_file.close()
        print("Attached to the note are two small...thingies? They're hard to describe.")
        print("They're small machines of some sort.")
        print("Maybe the note will shed some light on this whole situation.")
        print()
        thingy_one = requests.get("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy_one.py")
        thingy_one_stringified = str(thingy_one.text)
        new_thingy_one = open("thingy_one.py", "x")
        new_thingy_one.write(thingy_one_stringified)
        new_thingy_one.close()
        thingy_two = requests.get("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy_two.py")
        thingy_two_stringified = str(thingy_two.text)
        new_thingy_two = open("thingy_two.py", "x")
        new_thingy_two.write(thingy_two_stringified)
        new_thingy_two.close()

if __name__ == "__main__":
    main()