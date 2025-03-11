import math
y = 0
x = 0.2
n = 1
while math.sin(x**n)/x > 0.01:
    y = y + math.sin(x**n)/x
    n = n + 1
print(y)
