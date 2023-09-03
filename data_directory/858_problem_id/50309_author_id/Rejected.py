#! /bin/env python3

def comparator(amount, a, b, c):
	if amount == 4:
		return 0
	elif amount == 1:
		return a if (a < b + c) else b + c
	elif amount == 2:
		tmp = 2 * a if (2*a < b) else b
		return tmp if (tmp < 2 * c) else 2 * c
	else:
		tmp = 3 * a if (3 * a < a + b) else a + b
		return tmp if (tmp < c) else c

line = input()

lines = line.split(" ", 4)
n = int(lines[0])
a = int(lines[1])
b = int(lines[2])
c = int(lines[3])

amount = 4 - n % 4

answ = comparator(amount, a, b, c)

print(answ)