import random as rd

def f1(list):
    list.sort()
    print("1. Сортируем список по величине значения\n", list)
    num = None
    for i, j in enumerate(list):
        if j < 0:
            num = i
    print("Находим индекс самого большого отрицательного числа:", num)        
    
    v = 0
    arr = []
    while v < num:
        i = list[v]
        i = i**2
        arr.append(i)
        v += 1 
    print("Меньшие числа подносим к квадрату ", arr)
    arr += [*list[num:]] #dobavlaem k ostalnomu         
    return arr

def f2(list):

    def newlist(list):
        temp = []
        for i in list:
            if i > 0:
                temp.append(i)
            else:
                temp.append(1)
        return temp

    b = 1
    temp = 1000
    
    print("2. Проверяем порядок чисел в списке")
    while b == 1:
        for i in list:
            if i <= temp:
                temp = i
                answer = "Уменшается"
            elif i > temp:
                b = 0
                print("Числа идут не по-порядку, заменяем отрицательные на 1")         
                answer = newlist(list)
                break
    return answer

def f3(list):
    list.sort()
    print("3. Сортируем и переворачиваем список")
    return list[:-1]


a = []
i = 0
n = int(input("Создать список с числами от:"))
m = int(input("до:"))
step = int(input("С шагом(integer):"))
while i < 11:
    a.append(rd.randrange(n, m, step))
    i += 1
print(a, "\n\n")

b = f1(a)
print("Ответом первого задания будет список:\n", b, "\n\n")

b = f2(a)
print("Решением второго задания будет список:\n", b, "\n\n")

b = f3(a)
print("Решением третего задания будет список:\n", b, "\n\n")

input()