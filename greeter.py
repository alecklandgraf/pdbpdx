class Greeter(object):
    def __init__(self, name='Aleck'):
        super(Greeter, self).__init__()
        self.name = name

    def greet(self):
        """prints hello ``self.name``"""
        print 'hello {}'.format(self.name)
