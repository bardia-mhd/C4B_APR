x, y, l, r = map(int, input().split())

one = []
two = []

X = 1
while X <= r:
    one += [X]
    X   *= x

Y = 1
while Y <= r:
    two += [Y]
    Y   *= y

ans = [l - 1, r + 1]
for x in one:
    for y in two:
        if x + y >= l and x + y <= r:
            ans += [x + y]

ans = sorted(ans)
res = 0
for i in range(1, len(ans)):
    res = max(res, ans[i] - ans[i - 1])


print(res)