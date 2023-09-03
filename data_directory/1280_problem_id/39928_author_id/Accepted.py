# http://codeforces.com/problemset/problem/149/A
target_height = int(input())
growth = sorted([int(x) for x in input().split(' ')], reverse=True)
months = 0

while sum(growth[0:months]) < target_height and months < 12:
    months += 1

if sum(growth[0:months]) < target_height:
    print(-1)
else:
    print(months)