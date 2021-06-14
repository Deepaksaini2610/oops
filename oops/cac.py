class Person:
    ci = 0
    def __init__(self,lastn,fn,age):
        Person.ci += 1
        self.fn = fn
        self.lastn = lastn
        self.age = age
    @classmethod
    def from_string(cls,string):
        first,last,age = string.split(',')
        return cls(first,last,age)
    @classmethod
    def count_instance(cls):
        return f"you have to created {cls.ci} of"
    def full_name(self):
        return f"your nameis {self.fn} {self.lastn} is"
    def is_above_18(self):
        return self.age>18
    def is_below_18(self):
        return self.age<18
p1 = Person("deepak","saini",78)
p2 = Person("deepanshu",'chauhan',90)
p3 = Person.from_string('deepak,saini,78')
print(p3.full_name())

