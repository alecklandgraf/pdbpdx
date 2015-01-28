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
        from todo import ToDo
        td = ToDo()
        td.add('buy hat')
        td.add('buy sunscreen')
        td.check('buy hat')
        print td  # or just `td` from the shell
        >> todo:
        >> [X] buy hat
        >> [ ] buy sunscreen

        ## dump and load a todo list via json
        data = td.dumps()
        td2 = ToDo(data)
        ### or
        td3 = ToDo()
        td3.loads(td.dumps())

        ## save to file
        with open('workfile', 'w') as f:
            td.dump(f)

        ## load from file
        with open('workfile', 'r') as f:
            td.load(f)

    """
    def __init__(self, todos=None):
        super(ToDo, self).__init__()
        if todos is None:
            self.todos = []
        elif isinstance(todos, list):
            self.todos = todos
        else:
            self.todos = self.loads(todos)

    def __repr__(self):
        newline = '\n'
        todo_repr = newline.join(
            [self._stringify_todo(td) for td in self.todos]
        )
        todo_repr = "todo:\n" + todo_repr
        return todo_repr

    def dumps(self):
        return json.dumps(self.todos)

    def dump(self, f):
        """dump to file object ``f``"""
        json.dump(self.todos, f)

    def loads(self, todos):
        return json.loads(todos)

    def load(self, f):
        """load from file object ``f``"""
        self.todos = json.load(f)

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

    def _stringify_todo(self, td):
        if td['checked']:
            checked = 'X'
        else:
            checked = ' '
        return '[{checked}] {item}'.format(
            checked=checked,
            item=td['item']
        )

    def remove(self, item):
        logger.warning('not working')
        self.todos = filter(lambda td: td['checked'] != item, self.todos)

    @property
    def completed(self):
        completed_todos = filter(lambda td: td['checked'], self.todos)
        return ToDo(completed_todos)

    @property
    def not_completed(self):
        not_completed_todos = filter(lambda td: not td['checked'], self.todos)
        return ToDo(not_completed_todos)
