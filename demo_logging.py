"""demo logging
Usage:
    $ python run_todo.py
"""

from todo import ToDo


def main():
    td = ToDo()
    td.add('build up tolerance to spice')
    td.add('get some new shades')
    td.check('build up tolerance to spice')
    print td

if __name__ == "__main__":
    main()
