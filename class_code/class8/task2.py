# read write and append mode 
# introduction

from nt import read
from turtle import pen

import app


my_introduction = '''
my name is sharjeel. my father name is afzal ali bari . i have done intermediate . now i am learnig artificial intellece from saylani mass it training.
'''

# read mode 


def write_mode():
    with open("sharjeel.txt" , "w") as file :
        file.write(my_introduction)
def read_mode():
    with open("sharjeel.txt" , "r") as file :
        file.read()    
def append_mode():
    with open("sharjeel.txt" , "a") as file :
        file.write(f"i live in karachi")


# write_mode()
# read_mode()
# append_mode()
# '' ""

# csv excel file 

import csv
# with open("students_data.csv" , "w" , newline="") as file:
#     data_handler = csv.writer(file , delimiter=",")
#     data_handler.writerow(['name' , 'campus' , 'rollno' , 'age'])
player_list = [
    ['Chris Gayle', 'IPL', '333', '40'],
    ['Virat Kohli', 'IPL', '122', '34'],
    ['AB de Villiers', 'IPL', '133', '39'],
    ['MS Dhoni', 'IPL', '183', '41'],
    ['Rohit Sharma', 'IPL', '109', '36'],
    ['David Warner', 'BBL', '126', '37'],
    ['Steve Smith', 'BBL', '124', '35'],
    ['Glenn Maxwell', 'BBL', '154', '34'],
    ['Kane Williamson', 'CPL', '121', '33'],
    ['Brendon McCullum', 'CPL', '158', '42'],
    ['Shane Watson', 'IPL', '117', '42'],
    ['Andre Russell', 'CPL', '121', '35'],
    ['Sunil Narine', 'CPL', '109', '35'],
    ['Kieron Pollard', 'CPL', '104', '36'],
    ['Faf du Plessis', 'IPL', '120', '39'],
    ['Shikhar Dhawan', 'IPL', '106', '37'],
    ['Jos Buttler', 'IPL', '124', '33'],
    ['Ben Stokes', 'IPL', '107', '32'],
    ['KL Rahul', 'IPL', '132', '31'],
    ['Rishabh Pant', 'IPL', '128', '26']
]


# append mode
with open("students_data.csv" , "a" , newline="") as file:
    data_handler = csv.writer(file , delimiter=",")
    # data_handler.writerow(['ab devellers' , 'ipl' , '17' , '38'])
    data = data_handler.writerows(player_list)
    # print(data)
# read method
with open("students_data.csv" , "r" , newline="") as file:
    reader = csv.reader(file)
    print(reader)
    data = []
    for i in reader:
        # data += i
        data.append(i)
print(data)

