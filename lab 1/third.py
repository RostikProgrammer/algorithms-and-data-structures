import math
print('Трете завдання:')
n = int(input('Введiть N: '))
arr = range(1,n)
j = 0

for i in arr:
    j +=  pow(-1,i+1)/i*(i+1)

print('Вiдповiдь:',j)