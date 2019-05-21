import sys
import termios
import tty


def _get_char():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def get_user_input():
    while True:
        print("Select traffic light state: (r)ed, (y)ellow, (g)reen, (u)nknown, (p)ause: ")
        state = _get_char().lower()
        if state in ("r", "y", "g", "u", "p"):
            return state
        print("\nPlease select a valid input!\n")
