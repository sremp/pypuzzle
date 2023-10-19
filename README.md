# pypuzzle

Library for simple text-based puzzles using curses overlays.

Currently, only dial-based lock "puzzles" are demonstrated.

## Dependencies

- Python 3.10+
- [curses](https://docs.python.org/3/howto/curses.html) 
- [pick](https://github.com/wong2/pick)
- [pynput](https://pypi.org/project/pynput/)

## How to play

### Running the sample

First, pull down by cloning the repo and installing requirements:
```
cd pypuzzle
pip install requirements
```

Then run the sample:

```
python main.py
```

### Operating the dial

Use left and right arrow keys to move the cursor between the dials of the lock. Use up and down arrow keys to scroll through the letters of the dial. Press enter to attempt to open the lock. Press Q to go back to the main menu.

## Known Issues & TODOs

- Cursor goes out of bounds of dial characters moving left or right
- Dials currently scroll through all ASCII characters, need to confine to capital letters
- Wrap dial screen in a class
