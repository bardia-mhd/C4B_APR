team=input()
d=0
d_max=0
current=team[0]
for i in team:
    if (i==current):
        d+=1
    else:
        if (d>d_max):
            d_max=d
        current=i
        d=1
if (d>d_max):
    d_max=d
if (d_max>=7):
    print('YES')
else:
    print('NO')