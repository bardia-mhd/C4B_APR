n = int(input())
ans = 0
if n % 2 == 0:
  ans = n // 4
  if n % 4 == 0:
    ans -= 1
print(ans)