import math

r = 5
k = 1.24*10**-7
t = 0.1*10**-6
z = 0.5*10**2

x = (1/r)*(1-math.exp(-r*(t/k)))
y = (z**2)*math.asin(r/(math.sqrt(100-r**2)))

print('Перше завдання: ','\nx =', x, '\ny =', y)