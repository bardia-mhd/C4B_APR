k = int(input())
l = int(input())
m = int(input())
n = int(input())
d = int(input())

if k == 1 or l == 1 or m == 1 or n == 1:
	print (d)
	exit()
first_sum = 0
first_list = []
while first_sum + k <= d:
	first_sum = first_sum + k
	first_list = first_list + [first_sum]
	if first_sum % l == 0 or first_sum % m == 0 or first_sum % n == 0:
		first_list.remove(first_sum)


second_sum = 0
second_list = []
while second_sum + l <= d:
	second_sum = second_sum + l
	second_list = second_list + [second_sum]
	if second_sum % m == 0 or second_sum % n == 0:
		second_list.remove(second_sum)

	
third_sum = 0
third_list = []
while third_sum + m <= d:
	third_sum = third_sum + m
	third_list = third_list + [third_sum]
	if third_sum % n == 0:
		third_list.remove(third_sum)


forth_sum = 0
forth_list = []
while forth_sum + n <= d:
	forth_sum = forth_sum + n
	forth_list = forth_list + [forth_sum]


ans = len(first_list) + len(second_list) + len(third_list) + len(forth_list)


print (ans)