import json
import logging
FORMAT = (
    "%(levelname)s [%(filename)s:%(lineno)s - %(funcName)20s() ] %(message)s"
)
logging.basicConfig(format=FORMAT, level=logging.DEBUG)
logger = logging.getLogger(__name__)


class ToDo(object):
    """todo list
    Usage:
        ## basic
        from todo import ToDo
        td = ToDo()
        td.add('buy hat')
        td.add('buy sunscreen')
        td.check('buy hat')
        print td  # or just `td` from the shell
        >> [X] buy hat
        >> [ ] buy sunscreen

        ## dump and load a todo list via json
        td.dump()
        '[
            {"item": "buy sunscreen", "checked": false},
            {"item": "buy hat", "checked": true}
        ]'
        td2 = ToDo(td.dump())
        ### or
        td3 = ToDo()
        td3.load(td.dump())

    """
    def __init__(self, todos=None):
        super(ToDo, self).__init__()
        if todos:
            self.todos = self.load(todos)
        else:
            self.todos = []

    def __repr__(self):
        newline = '\n'
        return newline.join(
            [self.stringify_todo(td) for td in self.todos]
        )

    def dump(self):
        return json.dumps(self.todos)

    def load(self, todos):
        return json.loads(todos)

    def add(self, item):
        logger.debug('adding todo: {}'.format(item))
        self.todos.append({'checked': False, 'item': item})

    def check(self, item):
        logger.debug('checking todo: {}'.format(item))
        for td in self.todos:
            if td['item'] == item:
                td['checked'] = True

    def uncheck(self, item):
        for td in self.todos:
            if td['item'] == item:
                td['checked'] = False

    def toggle(self, item):
        for td in self.todos:
            if td['item'] == item:
                td['checked'] = not td['checked']

    def stringify_todo(self, td):
        if td['checked']:
            checked = 'X'
        else:
            checked = ' '
        return '[{checked}] {item}'.format(
            checked=checked,
            item=td['item']
        )

    def remove(self, item):
        logger.warning('not implemented')
