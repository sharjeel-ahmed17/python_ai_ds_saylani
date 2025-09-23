# inheritance
# parent and child
# base class
# parent -> provider || child -> user
# provide functionality to the child class and used it .

# parent class

# login / signup
# signup as a teacher
 
# child

# signup as a student
# signup as a teacher

# child

# login as a student
# login as a teacher

# types : 

# single ✔
# multiple
# multi_level
# herarical 
# hybrid

class User ():
    def __init__(self , name="sharjeel"):
        self.name= name
    def login(self):
        print("login")
    def register(self):
        print("register")
class student(User):
    def __init__(self):
        super().__init__()
    
    def enroll(self):
        print("enroll")

    def review(self):
        print("review")
class Teacher(User):
    def __init__(self):
        
        super().__init__()

# parent class
# u1 = User()
# u1.login()
# child class
# s1 = student()
# s1.enroll()
# s1.login()
# print(s1.name)

class Car():
    def __init__(self , seats , tyres , stairring , brake , horn , car_name):
        self.seats= seats
        self.tyres = tyres
        self.stairring = stairring
        self.brake = brake
        self.horn = horn
        self.car_name = car_name

    def describe_car (self):
        print("""
car tyres : {self.tyres}
car stairring : {self.stairring}
car horn : {self.horn}
car car_name : {self.car_name}

""")

    def speed (self):
        print(f"car speed")


    def describe_car (self):
        print(f"car speed")

class ElectricCar(Car):
    def __init__(self, seats, tyres, stairring, brake, horn, car_name, make, model, year, engine):
        super().__init__(seats, tyres, stairring, brake, horn, car_name)
        self.make = make
        self.model = model
        self.year = year
        self.engine = engine
        

    def decribe_elctric_car(self):
        print(f"electric car make is {self.make} and model is {self.model} and year is {self.year} and engine is {self.engine}")



e1 = ElectricCar(12  , 34, 56, 234, 45, "Tesla" , "honda" , 23444 , 2025 , "lts")
e1.decribe_elctric_car()


