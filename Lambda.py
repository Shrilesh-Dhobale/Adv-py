def appl(fx,value):
    return 6 + fx(value)

double=lambda x:x*2
cube=lambda x:x*x*x
avg=lambda x,y,z:(x+y+z)/3

print(double(6))
print(cube(4))
print(avg(2,5,6))

print(appl(avg,2,3,4,))