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

def newlist(list):
    temp = []
    for i in list:
        if i > 0:
            temp.append(i)
        else:
            temp.append(1)
    return temp

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
    mess = ""

    while b == 1:
        for i in list:
            if i <= temp:
                temp = i
                mess = "umenshaetsya"
                answer = mess
            elif i > temp:
                b = 0
                print("chisla idut ne po poryadku, zamenyaem otritsatelniye na 1")         
                answer = newlist(list)
                break
    return answer

def f3(list):
    list.sort()
    print("Sortiruem i perevorachivaem list")
    return list[:-1]


a = []
i = 0
n = int(input("Create a range of numbers from:"))
m = int(input("to:"))
step = int(input("(integer) With step:"))
while i < 11:
    a.append(rd.randrange(n, m, step))
    i += 1
print(a, "\n\n")

b = f1(a)
print("Resheniyem pervogo zadaniya budet list:\n", b, "\n\n")

b = f2(a)
print("Resheniyem vtorogo zadaniya budet list:\n", b, "\n\n")

b = f3(a)
print("Resheniyem tretego zadaniya budet list:\n", b, "\n\n")

input()