n = int(input())
pairs = n // 2
leftover = n % 2
ans = ["aa" if x % 2 == 0 else "bb" for x in range(pairs)]
if leftover:
    if len(ans) > 0:
        ans += (["b"] if ans[-1] == "aa" else "a")
    else:
        ans = ["a"]
print("".join(ans))