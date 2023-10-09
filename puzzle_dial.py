import curses
import time
from random import randrange
# import tty
import sys
from curses import wrapper
from pick import pick
# from utils import alphabet

# Set noecho and character break and start curses main screen
# screen = curses.initscr()
# screen.scrollok(True)
# screen.keypad(True)
# curses.cbreak()
# curses.noecho()
# curses.curs_set(True)

# Return the character at the current cursor position for a given curses window
# Why isn't this a built-in function???
def getch_curs(window):
    cursor_y, cursor_x = curses.getsyx()
    return window.inch(cursor_y, cursor_x)

# TODO: refactor to handle windows instead of individual key inputs
# def dial_handler(input_key, window)
#     if input_key == 113:
#         # puzzle_window.clear()
#         window.clear()
#         window.addstr("\nYou leave the lock alone.")
#         return False
#     elif input_key == 27:
#         window.getch()
#         arrow_code = window.getch()
#         match arrow_code:
#             case 65:
#                 window.addch(getch_curs(window) + 1)
#             case 66:
#                 window.addch(getch_curs(window) - 1)
#             case 67:
#                 curses.setsyx(curses.getsyx()[1] + 1)
#             case 68:
#                 curses.setsyx(curses.getsyx()[1] - 1)
#         return arrow_code
        
        
def display_puzzle(clue, answer, window, input_key):
    curses.nonl()
    lock_init = 'A' * len(answer) # Set the lock based on number of characters in answer
    window.keypad(True)
    window.addstr(clue + " (Press Q to quit)")
    window.addstr(4, 8, lock_init)
    window.move(4, 8)
    guess_counter = 0
    with open('./wrong_answer_responses.txt', 'r') as f_wrong_responses:
        wrong_responses = f_wrong_responses.readlines()
    
    while input_key != 113:
        cursor_y_last, cursor_x_last = window.getyx()
        
        # window.addstr(13, 0, f"enter: {curses.KEY_ENTER}")
        # window.addstr(12, 0, f"Last pressed keycode: {input_key}") 
        
        window.move(cursor_y_last, cursor_x_last)
        
        input_key = window.getch()

        
        match input_key:
            case 113:
                window.clear()
                window.addstr("\nYou leave the lock alone.")
                return False
            case curses.KEY_UP:
                window.addch(getch_curs(window) + 1)
                window.move(cursor_y_last, cursor_x_last)
            case curses.KEY_DOWN:
                window.addch(getch_curs(window) - 1)
                window.move(cursor_y_last, cursor_x_last)
            case curses.KEY_RIGHT:
                cursor_y, cursor_x = window.getyx()
                window.move(cursor_y, cursor_x + 1)
                window.refresh()
                window.cursyncup()
                # curses.doupdate()
            case curses.KEY_LEFT:
                cursor_y, cursor_x = window.getyx()
                window.move(cursor_y, cursor_x - 1)
                window.refresh()
                window.cursyncup()
                # curses.doupdate()
            case 13:
                guess_counter += 1
                lock_current = window.instr(4, 8, len(answer))
                if lock_current.decode() == answer:
                    window.addstr(7, 0, "DING DING WE HAVE A WINNER")
                    window.getch()
                    return True
                else:
                    window.addstr(7, 0, wrong_responses[randrange(4)] + f" (You guessed {lock_current})")
                    window.addstr(10, 0, f"Guess Counter: {guess_counter}")
                    window.move(cursor_y_last, cursor_x_last)
            
            
def main(screen):
    input_key = 0 # represents the player's character inputs

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
            puzzle_window = curses.newwin(0, 0, 0, 0) 
            puzzle_window.scrollok(True)
            screen.addstr("\n\nExcellent...")
            screen.refresh()
            time.sleep(3)
            screen.clear() 
            display_puzzle("\"Test puzzle. The answer is not TEST.\"", "TEST", puzzle_window, input_key)
            # display_puzzle("\"I am not a parent, but I raise you. I am not a teacher, but I guide you. I am not a I am not a playmate, but I am a friend. I am not the same age; regardless I will treat you as such. What am I?\" (Press Q to quit)", "UNCLE", puzzle_window, input_key)
        
        
            # puzzle_decision_str, puzzle_decision_index = pick(["I am fearless.", "Nah sounds dumb."], "Welcome epic gamer. Would you like to try and open this lock...???", screen = screen)
            #        curses.endwin()

wrapper(main)
