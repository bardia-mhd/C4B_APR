a, b = map(int, input().split())
if a == 0 and b == 0:
  print('NO')
elif a-b in {1, 0, -1}:
  print('YES')
else:
  print('NO')