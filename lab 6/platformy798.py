#https://www.e-olymp.com/ru/problems/798
plat_am = int(input())
height = input()
height = height.split(' ')
for i,j in enumerate(height):
    height[i] = int(j)
energy = [0] * plat_am
plat = [0] * plat_am
list_of_plat = [0] * plat_am
energy[1] = abs(height[1]-height[0])
plat[0]=-1
plat[1]=1
i = 2
while i < plat_am:
    if (energy[i-1]+abs(height[i]-height[i-1])) < (energy[i-2]+3*abs(height[i]-height[i-2])):
        energy[i] = energy[i-1]+abs(height[i]-height[i-1])
        plat[i] = i
    else:
        energy[i] = energy[i-2]+3*abs(height[i]-height[i-2])
        plat[i] = i-1
    i+=1
ans = 0
i = plat_am
while i > 0:
    list_of_plat[ans] = i
    ans += 1
    i = plat[i-1]
print('\n',energy[plat_am-1],'\n',ans)
i = ans-1
print(*list_of_plat[::-1])

'''
ввод
4
1 2 3 30 	
вывод
29
4
1 2 3 4
ввод
2
7 23 
вывод
16
2
1 2
ввод
5
0 1 0 1 0
вывод
0
3
1 3 5
'''