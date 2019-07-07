#lambda2 demostration

class Test:
    def __init__(self, first='', last=''):
        self.first = first
        self.last = last
    def test(self, formatter):
        """
            Test for lambdas.
            formatter is a function taking 2 arguments, first and last
                    names. It should return the formatted name.
        """
        msg = 'My name is %s' %(formatter(self.first, self.last))
        print(msg)

def test():
    t = Test('sumed', 'Kushwaha')
    t.test(lambda first, last: '%s %s' % (first, last))
    t.test(lambda first, last: '%s, %s' % (last, first))
test()