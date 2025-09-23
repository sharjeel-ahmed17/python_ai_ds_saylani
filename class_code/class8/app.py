

# 1 to 3000
# 3 and 5 divivible + 10
# 20 and 40 divivible (sum of all number)
# check how many even and odd number are there
sum : list[int]= []
sum2 : int = 0
even_list : int = 0
odd_list : int = 0
for i in range(1 , 3401):
    # task 1
    if i % 3 == 0 and i % 5 == 0:
        sum.append(i + 10)
    # task 2
    if i % 20 == 0 or i % 40 == 0:
        sum2 += i
    # task 3
    if i % 2 == 0:
        even_list += 1
    else:
        odd_list += 1

# print(sum)
# print(sum2)
print(even_list)    # task 3    
print(odd_list)    # task 3






    


