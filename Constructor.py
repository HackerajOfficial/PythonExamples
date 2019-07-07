#Demostrate Constructor

class Person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def output(self):
        print("Name:" +self.name + "Age:" +self.age)


sumed=Person("Sumed","28")
sumed.output()
print("=================================")
om=Person("OM","27")
om.output()