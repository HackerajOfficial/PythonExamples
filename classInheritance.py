#Class Inheritance


class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def out(self):
        print("Name:" +self.name + " Age:" +self.age)

class child(Person):
    pass


kid=child("Sumi","9")
kid.out()

