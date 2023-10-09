# Need to run in interactive mode due to inability to handle ansi escape characters
from pynput import keyboard


# class DialInterface:

def on_press(key_input):
    try:
        if key_input == keyboard.Key.up:
            print("uppies")
        elif key_input == keyboard.Key.down:
            print("downies")
        elif key_input == keyboard.Key.left:
            print("lefties")       
    except AttributeError:
        print('special key {0} pressed'.format(
            key_input))

def on_release(key_input):
    if key_input == keyboard.Key.esc:
        # Stop listener
        return False

# Need to suppress python interpreter history when thread is running in the interpreter
def input_handler():
    # Collect events until released
    with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()

# Use for GUI integrations or other stuff that requires current thread to continue
# listener = keyboard.Listener(
#     on_press=on_press,
#     on_release=on_release)
# listener.start()



input_handler()
# Using input method after input_handler function results in the second key-press successfully ignoring ansi in non-interactive mode. Something to do with Threading here?
# input()
