# with ("index.txt" , "r") as file:
#     pass
# write mode txt file open 
# filename , mode 
# w is compulsory for writing mode 
# with open("students.txt" , "") as file:

long_string = '''
Python powers major aspects of Abridge’s ML lifecycle, including data annotation, research and experimentation, and ML model deployment to production.
'''
# with open("students.txt" , "a") as file:
#     file.write(long_string)

with open("students.txt" , "r") as file:
    # print(file.read())
    msg = file.read()
    print(msg)
# read mode txt file opmsgen 
# filename , mode 
# r is compulsory for reading mode 
