""" launch_ipdb_on_exception demo:

$ ipython
In [1]: from ipdb import launch_ipdb_on_exception
In [2]: from launch_on_exception import print_progress
In [3]: with launch_ipdb_on_exception():
    ...     print_progress(19, 30)
"""


def print_progress(counter, total):
    while counter:
        total -= 1
        print(float(counter) / total)
