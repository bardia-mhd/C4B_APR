n,k = list(map(int,input().split()))

l = [i*5 for i in range(1,n+1)]
count = 0
for i in range(n):
    if sum(l[:i+1]) > 240-k:
        break
    count += 1
print (count)