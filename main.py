import time
from dial_lock import DialLock
from curses import wrapper
from pick import pick

def main(screen):
    input_key = 0 # represents the player's character inputs
    # test_dial_lock = DialLock("TEST", "\"Test puzzle. The answer is not TEST.\"")
    uncle_dial_lock = DialLock("UNCLE","\"I am not a parent, but I raise you. I am not a teacher, but I guide you. I am not a I am not a playmate, but I am a friend. I am not the same age; regardless I will treat you as such. What am I?\"")

    while True:
        puzzle_decision_str, puzzle_decision_index = pick(["I am fearless.", "Nah sounds dumb."], "Welcome epic gamer. Would you like to try and open this lock...???", screen = screen)
        
        # Call the player a bitch and exit the program
        # TODO: wrap in a function for utils or add to a class maybe
        if puzzle_decision_index == 1:
            screen.addstr("\n\nPussy.") 
            screen.refresh()
            time.sleep(5) # curses.napms(5000)
            screen.addstr("\nLater bitch.")
            screen.refresh()
            time.sleep(2) # curses.napms(2000)
            # screen.clear()
            # curses.endwin()
            break
        else:
            screen.addstr("\n\nExcellent...")
            screen.refresh()
            time.sleep(3)
            screen.clear() 
            uncle_dial_lock.display_dial_window(4, 8)
        
        
            # puzzle_decision_str, puzzle_decision_index = pick(["I am fearless.", "Nah sounds dumb."], "Welcome epic gamer. Would you like to try and open this lock...???", screen = screen)
            #        curses.endwin()

wrapper(main)

