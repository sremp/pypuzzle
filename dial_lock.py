import curses
import time
from random import randrange
import sys
from curses_utils import get_curs, clear_line
from curses import wrapper
from pick import pick

class DialLock():
    def __init__(self, answer, clue):
        self.answer = answer
        self.clue = clue
        self.guess_counter = 0
        self.lock_position = 'A' * len(self.answer) # Set the lock based on number of characters in answer
        self.lock_start_x = 0
        self.dial_window = None 

    def display_dial_window(self, lock_start_y, lock_start_x):
        input_key = 0
        self.lock_start_x = lock_start_x
        self.lock_end_x = self.lock_start_x + len(self.answer) - 1 # This should give the x position of the last dial
        curses.nonl()
        self.dial_window = curses.newwin(0, 0, 0, 0) 
        self.dial_window.scrollok(True)
        self.dial_window.keypad(True)
    
        self.dial_window.addstr(self.clue + " (Press Q to quit)")
        self.dial_window.addstr(10, 0, f"Guess Counter: {self.guess_counter}")
        self.dial_window.addstr(lock_start_y, self.lock_start_x, self.lock_position)
        self.dial_window.move(lock_start_y, self.lock_start_x)
        with open('./wrong_answer_responses.txt', 'r') as f_wrong_responses:
            wrong_responses = f_wrong_responses.readlines()
    
        # Break this out into a separate func??
        while input_key != 113:
            cursor = get_curs(self.dial_window)
            input_key = self.dial_window.getch()
     
            match input_key:
                case 113:
                    self.dial_window.clear()
                    self.dial_window.addstr("\nYou leave the lock alone.")
                    # sleep
                    return False
                case curses.KEY_UP:
                    self.scroll(1)
                case curses.KEY_DOWN:
                    self.scroll(-1)
                case curses.KEY_RIGHT:
                    self.select_dial(1)
                    self.dial_window.refresh()
                    self.dial_window.cursyncup()
                case curses.KEY_LEFT:
                    self.select_dial(-1)
                    self.dial_window.refresh()
                    self.dial_window.cursyncup()
                case 13:
                    self.guess_counter += 1
                    self.lock_position = self.dial_window.instr(lock_start_y, self.lock_start_x, len(self.answer)).decode()
                    if self.lock_position == self.answer:
                        clear_line(self.dial_window, 7)
                        self.dial_window.addstr(7, 0, "DING DING WE HAVE A WINNER")
                        self.dial_window.getch()
                        return True
                    else:
                        self.dial_window.addstr(7, 0, wrong_responses[randrange(4)] + f" (You guessed {self.lock_position})")
                        clear_line(self.dial_window, 10)
                        self.dial_window.addstr(10, 0, f"Guess Counter: {self.guess_counter}")
                        self.dial_window.move(cursor['y'], cursor['x'])

    # Scroll a "column" by grabbing the ASCII code for the next letter
    # cursor_y and cursor_x arguments should be the  
    def scroll(self, direction):
       
        cursor = get_curs(self.dial_window)
        next_letter = cursor['character'] + direction
         
        # Check if the next letter falls outside the ASCII range for uppercase characters (65-90)
        # Return it if it does, otherwise return the current letter
        if next_letter in range(65, 91):
            self.dial_window.addch(next_letter)
        elif next_letter == 91:
            self.dial_window.addch(65)
        elif next_letter == 64:
            self.dial_window.addch(90)
        self.dial_window.move(cursor['y'], cursor['x'])
    
    def select_dial(self, direction):
        cursor = get_curs(self.dial_window)
    
        if cursor['x'] in range(self.lock_start_x + 1, self.lock_end_x) or \
           (cursor['x'] == self.lock_start_x and direction == 1) or \
           (cursor['x'] == self.lock_end_x and direction == -1):
            self.dial_window.move(cursor['y'], cursor['x'] + direction) 
 
# def main(screen):
#     input_key = 0 # represents the player's character inputs
#     test_dial_lock = DialLock("TEST", "\"Test puzzle. The answer is not TEST.\"")
# 
#     while True:
#         puzzle_decision_str, puzzle_decision_index = pick(["I am fearless.", "Nah sounds dumb."], "Welcome epic gamer. Would you like to try and open this lock...???", screen = screen)
#         
#         # Call the player a bitch and exit the program
#         # TODO: wrap in a function for utils or add to a class maybe
#         if puzzle_decision_index == 1:
#             screen.addstr("\n\nPussy.") 
#             screen.refresh()
#             time.sleep(5) # curses.napms(5000)
#             screen.addstr("\nLater bitch.")
#             screen.refresh()
#             time.sleep(2) # curses.napms(2000)
#             # screen.clear()
#             # curses.endwin()
#             break
#         else:
#             screen.addstr("\n\nExcellent...")
#             screen.refresh()
#             time.sleep(3)
#             screen.clear() 
#             test_dial_lock.display_dial_window(4, 8)
#             # display_puzzle("\"I am not a parent, but I raise you. I am not a teacher, but I guide you. I am not a I am not a playmate, but I am a friend. I am not the same age; regardless I will treat you as such. What am I?\" (Press Q to quit)", "UNCLE", puzzle_dial_window input_key)
#         
#         
#             # puzzle_decision_str, puzzle_decision_index = pick(["I am fearless.", "Nah sounds dumb."], "Welcome epic gamer. Would you like to try and open this lock...???", screen = screen)
#             #        curses.endwin()
# 
# wrapper(main)
