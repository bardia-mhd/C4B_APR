n = sum([1 for i in input() if i in (4, 7)])
print("YES" if set(str(n)).issubset(set("47")) else "NO")