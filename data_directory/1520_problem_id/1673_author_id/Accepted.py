n,a,b,c = list(map(int,input().split()))
D = [-10000]*(n+1)
D[0] = 0
for i in range(1,n+1):
    javobho = []
    for x in {a, b, c}:
        if i >= x:
            javobho.append(D[i-x] + 1)
    D[i] = max(javobho) if javobho else -10000
print(D[-1])