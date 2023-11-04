import math


x=[]
y=[]
xs = 0
ys = 0
a = b = c = d = 0
corr = 0
n = int(input("enter numbers of arr: "))
print("enter you elemnet (x)")
for i in range(0, n):
    
    x.append(int(input()))
    xs += x[i]
xs = xs / n
print("enter you elemnet (y)")
for i in range(0, n):
    
    y.append(int(input()))
    ys += y[i]
ys = ys / n
for i in range(0, n):
    a += (x[i] - xs) * (y[i] - ys)
    b += (x[i] - xs) ** 2
    c += (y[i] - ys) ** 2
d = b * c
corr = a / math.sqrt(d)
print(corr)
