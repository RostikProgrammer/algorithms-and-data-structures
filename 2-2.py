import random
import numpy as np  
 
def cArr(n, m):
    x = int(input("Введите первый индекс массива: "))
    y = int(input("Введите второй индекс массива: "))
    return [[random.randint(n, m) for i in range(x)] for j in range(y)], x, y

def switch_case(arg):
    switcher = {
        0: [-10, 10],
        1: [0, 20]
    }
    val = switcher[arg]
    return val

def attrib(arr):
    print('\n\n')    
    arr1 = np.clip(arr, 0, 20)
    print("1",arr1)
    arr2 = np.clip(arr, -10, 0)    
    print("2",arr2)
    i = 0
    a=[]
    for i in arr1:
        if i != 0:
            a.append(i)
    print(a)  
    

        


val1, val2 = switch_case(int(input("Введите кейс: ")))
Arr, N, M = cArr(val1,val2)
arr = np.array(Arr)

print(arr)

attrib(arr)


print('\n')

c1 = 1
c2 = 0
ar = []
for i in range(M):
    arr[i][c1], arr[i][c2] = arr[i][c2], arr[i][c1]
    ar.append(arr[i])

ar = np.array(ar)
print(ar)