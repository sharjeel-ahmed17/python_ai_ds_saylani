# privacy hide data
# friend list 
# request accept then add
# direct add in id not prvacy

# hide the internal details 
# encapsulation
# capsule
# closed || store || not publically avaible || private  data 

# hospital data
# docotor and pateints

#  public || private || protected


class Emplyee():
    def __init__(self , name , salary):
        self.name = name # public
        self.__salary = salary # private
    def __my_salary(self):
        print(f"my salary is {self.__salary}")

e1 = Emplyee("abc" , 12)
print(e1._Emplyee__salary)  # aceess privates
# e1.__salary = 7500
# print(e1.__salary)
e1._Emplyee__my_salary() # aceess private



