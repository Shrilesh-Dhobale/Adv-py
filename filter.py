def is_even(num):
    return num%2 == 0
num=[1,2,3,4,5,6,]
filtered=filter(is_even,num)
print(list(filtered))