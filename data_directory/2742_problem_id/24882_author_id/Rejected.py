n = int(input())
ans = ''
if n % 2 == 0:
    ans = ans + '1' * (n // 2)
elif n == 3:
    ans = '7'
else:
    n -= 3
    ans = ans + '1' * (n // 2)
    ans = ans + '7'

print(ans)