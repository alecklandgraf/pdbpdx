import os
import time
from terminal_utils import getTerminalSize


def print_progress_bar(counter):
    """print `#` progress bars over ``counter`` seconds
    Usage:
        from progress_bar import print_progress_bar
        print_progress_bar(10)
    """
    width = getTerminalSize()[1] / counter
    for i in range(1, counter + 1):
        os.system('clear')
        print('#' * (width * i))
        time.sleep(1)
