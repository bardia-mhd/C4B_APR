a,b,c=list(map(int,input().split()))
mas=[]
mas.append(a+b+c)
mas.append(a+a+b+b)
mas.append(a+c+c+a)
mas.append(b+c+c+b)
print(min(mas))