import random as rd

def f1(list):
    list.sort()
    print("Sortiruem spisok po velichine znacheniya\n", list)
    num = None
    for i, j in enumerate(list):
        if j < 0:
            num = i
    print("Nahodim index samogo bolshogo otritsatelnogo chisla:", num)        
    
    v = 0
    arr = []
    while v < num:
        i = list[v]
        i = i**2
        arr.append(i)
        v += 1 
    print("Menshiye chisla podnosim k kvadratu ", arr)
    arr += [*list[num:]] #dobavlaem k ostalnomu         
    return arr

def f3(list):
    list.sort()
    print("Sortiruem i perevorachivaem list")
    return list[:-1]

def f4(list):
    


a = []
i = 0
n = int(input("Create a range of numbers from:"))
m = int(input("to:"))
step = int(input("(integer) With step:"))
while i < 11:
    a.append(rd.randrange(n, m, step))
    i += 1
print(a)

b = f1(a)
print("Resheniyem pervogo zadaniya budet list:\n", b)

b = f3(a)
print("Resheniyem tretego zadaniya budet list:\n", b)

b = f4(a)
print(a)