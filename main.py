c=int(input("Enter the value of c: "))

import math
e = math.sqrt((b**2)-(4*a*c))
d = ((b**2)-(4*a*c))

x1 = (-b+e)/(2*a)
x2 = (-b-e)/(2*a)

print("The roots of x are:", x1,"and", x2)
if d==0:
    e=math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("The value of x is:", x1)
elif d<0:
    print("No result")
else:
    e=math.sqrt(d)
    x1 = (-b + e) / (2 * a)
    x2 = (-b - e) / (2 * a)
    print("The roots of x are:", x1,"and", x2)
