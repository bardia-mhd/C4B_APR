x = input()
z = 1
i = 0
lst = []
lst2 = ['A','E','U','I','O','Y']
while(i<len(x)):
    if(x[i] not in lst2):
        z += 1
    else:
        z = 1
    lst.append(z)
    i += 1
print(max(lst))