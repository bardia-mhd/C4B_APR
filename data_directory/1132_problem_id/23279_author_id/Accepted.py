n = int(input())
for i in range(1,n+1):
    if n%i==0:
        s = list(str(i))
        flag = 0
        for i in s:
            if i!="4" and i!="7":
                flag = 1
                break
        if flag == 0:
            print("YES")
            break
if flag == 1:
    print("NO")