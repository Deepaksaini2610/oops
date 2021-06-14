#first create class
#self represet object when we create object 
class Person:
    def __init__(self,first_name,last_name,age):
        # instance variable initilise
        print("init method // constructor get called")
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
p1 = Person('deepak','saini',45)
p2 = Person('rahul','saini',67)
print(p1.first_name)
        