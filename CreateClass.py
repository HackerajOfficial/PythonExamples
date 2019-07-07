#Demostrate Create a class

class Person():
    def insert(self,name,age):
        self.name=name
        self.age=age

    def output(self):
        print("Your name is " + self.name + " And Your Age " +self.age)


j=Person()
j.insert("Sumed","28")
j.output()