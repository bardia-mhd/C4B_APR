n = int(input())

f = [0] * 200
f[0] = 1
f[1] = 2
for k in range(2, 101):
	f[k] = f[k-1] + f[k-2]
for k in range(1, 100):
	if n >= f[k] and n < f[k+1]:
		print(k)
		exit()