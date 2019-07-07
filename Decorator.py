'''Decorator'''
def decor(func):
    def wrap():
        print("===============")
        func()
        print("===============")
    return wrap

def print_text():
    print("Hello World!")


decorted=decor(print_text)
decorted()