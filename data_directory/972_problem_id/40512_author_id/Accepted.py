x, y = input().split()
x = int(x)
y = int(y)

if x-y>1 or x-y<-1 or (x==0 and y==0):
    print("NO")
else:
    print("YES")