'''input
4
'''
def is_prime(n):
	if n < 2: return False
	elif n == 2: return True
	elif n % 2 == 0: return False
	elif all(n % i != 0 for i in range(3, int(n**0.5)+1, 2)): return True
	return False

n = int(input())
print(1 if is_prime(n) else 2 if n % 2 == 0 or is_prime(n-2) else 3)