from util import input_handler
from pynput import keyboard

# Globals
alphabet = ("a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z")

password = "test"
password_attempt = ""

# This will go away
# for letter in range(len(password)):
#     dial_number = letter + 1
#     password_attempt = password_attempt + str(input(f"What is the letter for Dial {dial_number}? "))

# Put this in a method
if password_attempt.lower() == password.lower():
    print("Password correct. Unlocked.")
else:
    print("Incorrect. Please try again.")

class DialLock:
    ''' Basic implementation of a simple password-based lock puzzle '''
    def __init__(self, password):
        self.password = password
        self.dial = alphabet



input_handler()

