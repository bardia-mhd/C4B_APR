import sys
def f(m):
	if m - 1 < 0:
		return 0
	return (m - 1)* m // 2

def calc(m, K):
	rest = K - m
	return K + f(K - 1) - f(rest)

if __name__ == "__main__":
	N,K = map(int, input().split())
	if N == 1:
		print (0)
		sys.exit()
	if N <= K:
		print (1)
		sys.exit()
	left = 0
	right = K + 1
	result = 10 ** 10
	while (right - left > 1):
		med = (right + left) // 2
		res = N - calc(med, K)
		if res == 0:
			print (med)
			sys.exit()
		if res > 0:
			rest = K - med - 1
			if rest >= res:
				result = min(result, med + 1)
			left = med
		else:
			right = med
	if result >= 10 ** 10:
		result = -1
	print (result)