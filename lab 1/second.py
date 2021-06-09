import math

a = 18.5
x = []
i = 0.4
while i <= 2:
    x.append(round(i,1))
    i += 0.2

print('Друге завдання:\n',x)

for i in x:
    if i <= 1:        
        print('y =', pow(math.sin(math.sqrt(abs(a*i))),2))
    else:        
        print('y =', math.log(i+1) )  



