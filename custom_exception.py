class MyError(Exception):
    def __init__(self, *args):
        print ('calling init')
        if args:
            self.message = args[0]
        else:
            self.message = ''

    def __str__(self):
        print ('calling str')
        if self.message:
            return "MyError exception with a message:  {0}".format(self.message)
        else:
            return "MyError exception"