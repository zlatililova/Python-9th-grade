class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __add__(self, other_obj):
        prs = Person("",0)
        prs.age = self.age + other_obj.age
        return prs.age

    def __sub__(self, other_obj):
        prs = Person("",0)
        prs.age = self.age - other_obj.age
        return prs.age

    def __mul__(self, other_obj):
        prs = Person("",0)
        prs.age = self.age * other_obj.age
        return prs.age

    def __truediv__(self, other_obj):
        prs = Person("",0)
        prs.age = self.age / other_obj.age
        return prs.age


p = Person("Alex", 15)
p1 = Person("Pesho", 10)
print(p + p1)
print(p - p1)
print(p * p1)
print(p / p1)