# kaggle
# aws


class Car():
    def __init__(self , brand , model ):
        self.brand = brand
        self.model = model
    
    def move(self):
        return "car move"
class Boat():
    def __init__(self , brand , model ):
        self.brand = brand
        self.model = model
    def move(self):
        return "boat move"
class Plane():
    def __init__(self , brand , model ):
        self.brand = brand
        self.model = model
    def move(self):
        return "plane move"


c1 = Car("abc" , 123)
b1 = Boat("xyz" , 234)
p1 = Plane("plane" , 199)

# c1.move()
vehicels = [c1 , b1 , p1]

for i in vehicels:
    print(i.brand , i.model)
    print(i.move())

# polymorphism example
import random

print(random.randint(1000 , 10_000))