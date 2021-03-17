import random
import numpy as np  
 
def cArr(n, m):
    x = int(input("Введите первый индекс массива: "))
    y = int(input("Введите второй индекс массива: "))
    return [[random.randint(n, m) for i in range(x)] for j in range(y)], x, y

def switch_case(arg):
    switcher = {
        1: [-10, 10],
        2: [0, 20]
    }
    val = switcher[arg]
    return val

def f1(arr, q):    
    def attrib(arr):
        arr1 = []
        arr2 = []
        for i in arr :
            for j in i:
                if j > 0:
                    arr1.append(j)
                elif j < 0:
                    arr2.append(j)    
        
        a = np.where(arr==min(arr1))
        b = np.where(arr==max(arr2))
        print("Минимальное положительное число первый раз встречается в колонке: ", a[1][0],
        '(',min(arr1),')')
        print("Максимальное отрицателькое число первый раз встречается в колонке: ", b[1][0],
        '(',max(arr2),')')
        return a[1][0], b[1][0]
    if q == 1:
        c1, c2 = attrib(arr)
    elif q == 2:
        c1 = 1
        c2 = 0
        с2 = np.where(arr==arr.max())[0][0]
    else: 
        print("Ошибка")
    if c1 != c2:
        ar = []
        for i in range(M):
            arr[i][c1], arr[i][c2] = arr[i][c2], arr[i][c1]
            ar.append(arr[i])
        ar = np.array(ar)
        print(ar)
    else:
        print("Оба числа находятся в одной и той же колонке")
  

val1, val2 = switch_case(int(input("Диапазон чисел(1 = -10,10; 2 = 0,20): ")))
Arr, N, M = cArr(val1,val2)
arr = np.array(Arr)
print(arr)

f = int(input("Выберите задание(1, 2, 3): "))
if f == 1 or 2:
    f1(arr, f)    
elif f == 3:
    print("Количество уникальных знаков =", np.count_nonzero(np.unique(arr)), np.unique(arr))
else:
    print("Такого задания я не сделал:(")

input()    