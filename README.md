# pypuzzle

Library for simple text-based puzzles using curses overlays.

Currently, only dial-based lock "puzzles" are demonstrated.

## Dependencies

- Python 3.10+
- [curses](https://docs.python.org/3/howto/curses.html) 
- [pick](https://github.com/wong2/pick)
- [pynput](https://pypi.org/project/pynput/)

## How to play

```
pip install requirements
python puzzle_dial.py
```

## Known Issues & TODOs

- Cursor goes out of bounds of dial characters moving left or right
- Dials currently scroll through all ASCII characters, need to confine to capital letters
- Wrap dial screen in a class
