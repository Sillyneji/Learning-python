import math

def maclaurin(n,x):
    s = 0
    for i in range(n + 1):
        t = ((-1) ** i) * (math.pow(x, 2 * i + 1)) / math.factorial(2 * i + 1)
        s = s + t
    return s



n=int(input("enter the number of terms you want to calculate  :"))
deg=float(input("enter the angles in degrees :"))
x=deg*math.pi/180

s=maclaurin(n,x)

print(f"The approximate value of sin{deg} is ",s)
print(f"the actual value sin{deg} is ",math.sin(x))

