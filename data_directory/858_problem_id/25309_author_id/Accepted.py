from itertools import product
n, p1, p2, p3 = (int(x) for x in input().split())
best_price = 10**12
for i in product(range(50), repeat=3):
    k, l, m = i
    if (n + k + 2 * l + 3 * m) % 4 == 0:
        price = k * p1 + l * p2 + m * p3
        best_price = min(best_price, price)

print(best_price)