b=[]
a=str(input()).split()
for i in range(4):
    if a[i] not in b:
        b.append(a[i])
print(4-len(b))