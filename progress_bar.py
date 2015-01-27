import time
from .terminal_utils import getTerminalSize


def print_progress_bar(counter):
    """print `#` progress bar"""
    width = getTerminalSize()[1]
    while counter:
        counter -= 1
        print('#' * (width / counter))
        time.sleep(1)
