# https://www.e-olymp.com/ru/problems/987 
n = int(input())
a = input()
a = a.split(' ')
for i, j in enumerate(a):
    a[i] = int(j)
a.sort()
al = []
i = 0
while i < n:
    al.append(0)
    i+=1
i = 3
print("Для помощи в обчислениях\n", a) 
al[1] = abs(a[1] - a[0])
al[2] = abs(a[2] - a[0])
while i<n:
    al[i] = abs(min(al[i-1],al[i-2]) + a[i] - a[i-1])
    i+=1
print('', al)
print("Ответ:", al[-1])    
