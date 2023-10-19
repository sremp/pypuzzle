'''
Utility functions for making certain curses things easier, like:
    - getting cursor coordinates + cursor character
    - clearing a line without moving the cursor 
'''
import curses

# Retrieve a bundle of information about the cursor
def get_curs(window):
    cursor_y, cursor_x = window.getyx()
    window.move(cursor_y, cursor_x) # Need to "reset" cursor to current position to keep it in place
    
    return {
        'y': cursor_y,
        'x': cursor_x,
        'character': window.inch(cursor_y, cursor_x)
    }

# Clear the line at the specified row number then set the cursor back to where it was
def clear_line(window, line):
    cursor_y, cursor_x = window.getyx()
    window.move(line, 0)
    window.clrtoeol()
    window.move(cursor_y, cursor_x)
