n, k = map(int, input().split())

ans = 0
while k + 5 * ans < 240:
	k += 5 * ans
	ans += 1
	if ans == n:
		break
if k + 5 * ans > 240:
	ans -= 1
print(ans)