"""demo logging
Usage:
    $ python demo_logging.py
"""
from todo import ToDo


def main():
    td = ToDo()
    td.add('build up tolerance to spice')
    td.add('get some new shades')
    td.add('buy sunscreen')
    td.check('build up tolerance to spice')
    td.remove('get some new shades')
    print(td)
    print('completed ' + str(td.completed))
    print('left ' + str(td.not_completed))

    # save our todo
    with open('workfile', 'w') as f:
        td.dump(f)


if __name__ == "__main__":
    main()
