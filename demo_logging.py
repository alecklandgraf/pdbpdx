"""demo logging
Usage:
    $ python run_todo.py
"""

from todo import ToDo


def main():
    td = ToDo()
    td.add('build up tolerance to spice')

if __name__ == "__main__":
    main()
