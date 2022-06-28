import os
import requests
from dotenv import dotenv_values

DOOR = dotenv_values('.door')

def grab_file(raw_path: str, file_name: str):
    raw = requests.get(raw_path)
    text = str(raw.text)
    file = open(file_name, "x")
    file.write(text)
    file.close()


def main():
    print()
    note_exists = os.path.exists("garage-door-note.md")
    if note_exists == True:
        garage_interior_exists = os.path.exists("/garage-interior")
        if garage_interior_exists == True:
            print("The door's already unlocked. Not much else to see here.")
            print()
        else:
            user_code = input("Please enter 4-digit passcode: ")
            print()
            if user_code == DOOR["CODE"]:
                print("That is correct. Unlocking garage...")
                print()
                #NEED TO ADD GARAGE-INTERIOR FOLDER
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
        grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/garage-door-note.md", "garage-door-note.md")
        print("Attached to the note are two small...thingies? They're hard to describe.")
        print("They're small machines of some sort.")
        print("Maybe the note will shed some light on this whole situation.")
        print()
        grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy-one.py", "thingy-one.py")
        grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy-two.py", "thingy-two.py")

if __name__ == "__main__":
    main()