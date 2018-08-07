import curses

def handleKey(key, stdscr):
    if key == ord('q'):
        stdscr.addstr(1, 0, "Stopping episode...")
        return None


    if key == curses.KEY_UP:
        stdscr.addstr(4, 10, "Up   ")
        action = [1,0]
    elif key == curses.KEY_DOWN:
        stdscr.addstr(4, 10, "Down ")
        action = [-1,0]
    elif key == curses.KEY_RIGHT:
        stdscr.addstr(4, 10, "Right")
        action = [.1, -1]
    elif key == curses.KEY_LEFT:
        stdscr.addstr(4, 10, "Left ")
        action = [.1, 1]

    return action

