import random  
 
def cArr(n, m):
    x = int(input("Введите первый индекс массива: "))
    y = int(input("Введите второй индекс массива: "))
    return [[random.randint(n, m) for i in range(x)] for j in range(y)]

def switch_case(arg):
    switcher = {
        0: [-10, 10],
        1: [0, 20]
    }
    val = switcher[arg]
    return val

val1, val2 = switch_case(int(input("Введите кейс: ")))
Arr = cArr(val1,val2)

print(Arr)
print(max(Arr))

