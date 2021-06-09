import random
s = []
temp = 0
i = 0
j = int(input("Vvedit dovjinu S: "))

def cum(s, i , j):
    if s[i] == s[j] and i-j < 0:
        print("tik")
        i+=1
        j=j-1
        cum(s, i, j)
    elif i-j >= 0:
        print("cum")
    else: print("ne cum") 

while temp < j:
    s.append(random.randrange(1, 10, 1))
    temp += 1
print(s)

cum(s, i , j-1)

s += s[::-1]
print(s)
cum(s, i, (j-1)+j)
