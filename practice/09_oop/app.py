# l = [1 ,2 , 3, 4]
# print(type(l))

# class 
class Myclass :
    x = 5
    def __str__(self):
        return f"Myclass(x={self.x})"

# object
m1 = Myclass()
m1.x = 10
# print(m1.x)


# l1 = [1 , 2, 3, 4]
# print(len(l1))
# l1.append(5)
# print(l1)


class Student(): 

    name = "John"
    roll_no  = 101
    course = "Python"
    location = "USA"

    def __str__(self):
        return f"Student(name={self.name}, roll_no={self.roll_no}, course={self.course}, location={self.location})"

    # method
    def study(self):
        print(f"{self.name} is studying {self.course}")
    def exam(self):
        print(f"{self.name} is taking an exam")
    def fee(self):
        print(f"{self.name} is paying fee")


s1 = Student()
# print(s1.name)
# print(s1.roll_no)
# print(s1.course)
# print(s1.location)

# s1.study()
# s1.exam()
# s1.fee()

class Person():
    def __init__(self, name , age ) -> None:
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"
        
# p1 = Person()
# p1 = Person("John" , 25)
# p1 = Person("John" , 30 , "USA", "Engineer")



class Teacher():
    def __init__(self , name , tech , school) :
        self.name = name
        self.tech = tech
        self.school = school

    def show_name(self) :
        print(f"Teacher name is {self.name}")
    @staticmethod
    def show_tech():
        print("Teacher teaches Python")
    def show_school(self):
        print(f"Teacher works at {self.school}")

    # def __str__(self):
    #     return f"Teacher(name={self.name}, tech={self.tech}, school={self.school})"
t1 = Teacher("Alice" , "Math" , "High School")
t1.show_name()
t1.show_school()
# t1.show_tech()