from functools import reduce

numbers=[1,2,3,4,5,6]

def my_sum(x,y):
    return x+y

sum=reduce(my_sum,numbers)

print(sum)
