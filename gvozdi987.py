# https://www.e-olymp.com/ru/problems/987 
n = 7
a = [1, 6, 9, 22, 13, 28, 40]
a.sort()
al = []
i = 0
while i < n:
    al.append(0)
    i+=1
i = 3
print(n, a) 
al[1] = abs(a[1] - a[0])
al[2] = abs(a[2] - a[0])
while i<n:
    al[i] = abs(min(al[i-1],al[i-2]) + a[i] - a[i-1])
    i+=1
print('', al)
print(al[-1])    


'''
al = []
a.sort()
i=0
while i < n-1: 
    al.append(a[i+1]-a[i])
    i+=1
if n > 2: al.insert(1, al[1]+al[0])
i=2
while i < n-1:
    al.insert(i, min(al[i-1], al[i-2]))
    i+=1
print(al)
'''


"""
while i < n:
    a.append(int(input()))

a.sort()
print(a)
"""