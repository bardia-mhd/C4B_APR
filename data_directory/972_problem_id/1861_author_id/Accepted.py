a, b = (int(i) for i in input().split())
print("YES" if abs(a - b) <= 1 and (a + b) > 0 else "NO")