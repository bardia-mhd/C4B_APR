n,m,k=int(input())

r = (((k+1)//2) // m) + 1

d = ((k+1)//2) % m
if (d==0):
    d=m
    r = r-1
if (k%2 == 0):
    s = "R"
else:
    s = "L"
print (r,d,s)