x = int(input())
a,b,c,d,e,f,g,h,i,j,k,l = map(int,input().split())
lst = [a,b,c,d,e,f,g,h,i,j,k,l]
lst.sort(reverse=True)
z = 0
if(x==0):
    print("0")
else:
    for i in range(x):
        z += lst[i]
        if(z >= x):
            print(i+1)
            break