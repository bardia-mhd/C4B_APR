n=input().strip()
n=list(n)
def lets_check(n):
    su=0
    for i in range(1, len(n)):
        if su>5:
            return("YES")
        if n[i]==n[i-1]:
            su+=1
        else:
            su=0
    return("NO")
print(lets_check(n))