n = int(input())
n -= 10
a = [1,2,3,4,5,6,7,8,9,10,10,10,10]
cnt = 0
for i in range(13):
    if a[i] == n:
        cnt += 1

cnt *= 4
if n == 10:
    cnt -= 1

print(cnt)