s = input()
a = s.split()
for i in range(len(a)):
	a[i] = int(a[i])
a.sort()
i = 0
while i < len(a)-1:
	if a[i] == a[i+1]:
		a.remove(a[i])
	else:
		i += 1

print(4 - len(a))