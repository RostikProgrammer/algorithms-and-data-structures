a = [-4, 0, -10, 6, 5, 7, -2, -2, -2, 3, 7]

'''a = [i for i in range(1,11)]
a.reverse()'''

#a = [10, 10, 1, 7, 6, 5, 4, 2, 1]

print(a)

bool = 1
temp = 1000
mess = ""

def newlist(list):
    temp = []
    for i in list:
        if i > 0:
            temp.append(i)
        else:
            temp.append(1)
    return temp


while bool == 1:
    for i in a:
        if i <= temp:
            temp = i
            mess = "umenshaetsya"
            print(i, mess)
        elif i > temp:
            bool = 0         
            mess = "ne umenshaetsya"
            print(i, mess)
            print(newlist(a))
            break
            

