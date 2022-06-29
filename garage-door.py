import os
import gitit
from dotenv import dotenv_values

PAD = dotenv_values('.pad')

def make_muck(muck: str):
    gitit.grab_file(
        f"https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/dirty-garage-floor/{muck}.py",
        f"dirty-garage-floor/{muck}.py"
        )

def main():
    print()
    note_exists = os.path.exists("garage-door-note.md")
    if note_exists == True:
        garage_interior_exists = os.path.exists("robo-vac.py")
        if garage_interior_exists == True:
            print("The power's already turned on. Not much else to see here.")
            print()
        else:
            user_code = input("Please enter 4-digit passcode: ")
            print()
            if user_code == PAD["CODE"]:
                print("WELCOME TO THE WORKSHOP. ENGAGING POWER PROTOCOLS.")
                print()
                print("Vibrations suddenly rock the floor and you hear a whirring sound start up all around you.")
                print()


                # Add files to garage directory
                gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/.vac-eq", ".vac-eq")
                gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/robo-vac.py", "robo-vac.py")
                gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/robo-vac-instructions.md", "vacuum-instructions.md")

                # Create the garage floor
                os.mkdir("dirty-garage-floor")

                # Add files to dirty-garage-floor directory
                make_muck("a-few-loose-screws")
                make_muck("air-freshener")
                make_muck("art-deco-book")
                make_muck("beadless-abacus")
                make_muck("beanbag")
                print("WORKSHOP 5% POWERED.")
                print()
                print("...5%? You suspect this might take a minute.")
                print()
                make_muck("bolts")
                make_muck("box-shaped-jello")
                make_muck("brass-tacks")
                make_muck("broken-glass")
                make_muck("brown-paper-bag")
                make_muck("busted-bifocals")
                make_muck("cardboard")
                make_muck("chipped-marble")
                make_muck("clown-college-rejection-letter")
                make_muck("coffee-stained-coaster")
                make_muck("crap")
                make_muck("crud")
                make_muck("crumbs")
                make_muck("crusty-object")
                make_muck("debris")
                make_muck("definitely-not-chocolate")
                make_muck("detritus")
                make_muck("dirt")
                make_muck("dirty-sock")
                make_muck("dust")
                print("WORKSHOP 25% POWERED.")
                print()
                print("The lights still haven't turned on. You twiddle your thumbs.")
                print()
                make_muck("earring-stud")
                make_muck("empty-seltzer-can")
                make_muck("enigmatic-invention")
                make_muck("etch-a-sketch")
                make_muck("everyone-loves-robert-season-four-dvd-with-extra-commentary")
                make_muck("eviction-notice")
                make_muck("filled-out-madlibs")
                make_muck("final-fantasy-xxvii")
                make_muck("five-second-rule-sandwich")
                make_muck("friendship-bracelet")
                make_muck("gamegirl-advance")
                make_muck("glass-eye")
                make_muck("golfball")
                make_muck("greasy-griddle")
                make_muck("half-eaten-two-musketeers")
                make_muck("half-melted-crayon")
                make_muck("headless-doll")
                make_muck("holographic-nokemon-card")
                make_muck("inkless-pen")
                make_muck("javascript")
                make_muck("junk")
                make_muck("little-foosball-guy")
                make_muck("maybe-chocolate")
                make_muck("mood-ring")
                make_muck("motivational-cat-poster")
                print("WORKSHOP 50% POWERED.")
                print()
                print("You can almost *feel* the steady hum of electricity all around you.")
                print("Just what is this place?")
                print()
                make_muck("mummified-flea")
                make_muck("mysterious-cable")
                make_muck("note-to-self")
                make_muck("number-one-pencil")
                make_muck("nuts")
                make_muck("old-wiring")
                make_muck("origami-duck")
                make_muck("other-dirty-sock")
                make_muck("paperclip-shaped-like-an-s")
                make_muck("perfectly-good-umbrella")
                make_muck("permanent-marker")
                make_muck("petrified-mouse")
                make_muck("pile-of-postage-stamps")
                make_muck("ping-pong-paddle")
                make_muck("pizza-box")
                make_muck("plastic-straw")
                make_muck("priceless-artifact")
                make_muck("protractor")
                make_muck("puka-shell-necklace")
                make_muck("puzzle-piece")
                make_muck("questionable-substance")
                make_muck("rose-tinted-spectacles")
                make_muck("rusty-bucket")
                make_muck("rusty-nail")
                make_muck("sandwich-crust")
                print("WORKSHOP 75% POWERED.")
                print()
                print("You hum a little tune. You're actually getting a little nervous.")
                print()
                make_muck("second-rusty-nail")
                make_muck("settlers-of-batan")
                make_muck("shipping-label")
                make_muck("shoe-string")
                make_muck("soggier-papers")
                make_muck("soggiest-papers")
                make_muck("soggy-papers")
                make_muck("spent-battery")
                make_muck("splotchy-dishrag")
                make_muck("sponge-labeled-bob")
                make_muck("styrofoam")
                make_muck("tambourine")
                make_muck("tapeless-cassette-tape")
                make_muck("thingy-three")
                make_muck("tin-foil-hat")
                make_muck("trekking-stars-fanfiction")
                make_muck("triangular-sales-brochure")
                make_muck("unlabeled-folder")
                make_muck("unmailed-mail-in-rebate")
                make_muck("unpaid-phone-bill")
                make_muck("untouched-sudoku-puzzle")
                make_muck("walkman")
                make_muck("worn-tread")
                make_muck("yellow-guitar-pick")
                print("WORKSHOP 100% POWERED.")
                print()
                print("Suddenly, the lights in the garage power on.")
                print("You were expecting some great spectacle with all that hullabaloo.")
                print("But all you see...is junk.")
                print("Like, lots of it. It's kinda gross, really.")
                print()
                print("But over in the corner you see something else, a little metal cube.")
                print("Might be worth checking out.")
                print()
                
            else:
                print("Sorry, that is incorrect.")
                print()
    else:
        print("The garage is pitch black inside. You flick a nearby light switch, but nothing happens.")
        print("Next to the light switch, you see a dimly glowing keypad that appears to take a 4-digit code...")
        print('...along with the label "FOR GARAGE POWER".')
        print()
        print("Frustratingly, you don't remember the Landlord giving you any codes.")
        print()
        print("However, you do see a note in his handwriting taped next to the keypad.")
        print("You can sorta read it from the light coming in from the open door.")
        print()
        gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/garage-door-note.md", "garage-door-note.md")
        print("Clipped to the note are two small...thingies? They're hard to describe.")
        print("They're small machines of some sort.")
        print("Maybe the note will shed some light on this whole situation.")
        print()
        gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy-one.py", "thingy-one.py")
        gitit.grab_file("https://raw.githubusercontent.com/term-world/world-additions/main/week-1-additions/thingy-two.py", "thingy-two.py")
        print("~There are some new files in the garage folder worth checking out via your File Explorer!~")
        print()

if __name__ == "__main__":
    main()
