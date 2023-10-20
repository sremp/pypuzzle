# pypuzzle

Library for simple text-based puzzles using curses overlays.

Currently, only dial-based lock "puzzles" are demonstrated.

## Demo

DialLock

![dial](https://i.ibb.co/PwXxzb5/Dial-Lock-Demo.gif)

## Dependencies

- Python 3.10+
- [curses](https://docs.python.org/3/howto/curses.html) 
- [pick](https://github.com/wong2/pick)

## How to play

### Running the sample

First, pull down by cloning the repo and installing requirements:
```
cd pypuzzle
pip install -r requirements.txt
```

Then run the sample:

```
python main.py
```

### Operating the dial

(For a visual guide, refer to the GIF above)

Use left and right arrow keys to move the cursor between the dials of the lock. Use up and down arrow keys to scroll through the letters of the dial. Press enter to attempt to open the lock. Press Q to go back to the main menu.

## Known Issues & TODOs

- Guess counter doesn't register correct guesses or update the "You Guessed" output
- Comments suck ass
- Cross-platform stuff
