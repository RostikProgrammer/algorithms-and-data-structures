import random
import numpy as np  
 
def cArr(n, m):
    x = int(input("Введите первый индекс массива: "))
    y = int(input("Введите второй индекс массива: "))
    return [[random.randint(n, m) for i in range(x)] for j in range(y)], x

def switch_case(arg):
    switcher = {
        0: [-10, 10],
        1: [0, 20]
    }
    val = switcher[arg]
    return val

'''def attrib(arr):
    for ind, val in arr:'''
        


val1, val2 = switch_case(int(input("Введите кейс: ")))
Arr, N = cArr(val1,val2)
arr = np.array(Arr)
print(arr)
#print(N)
#print(attrib(Arr))

print(Arr)
print(max(Arr))



