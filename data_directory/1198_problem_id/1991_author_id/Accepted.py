s = input()
ans = False
for a in s:
    if a == "H" or a == "Q" or a == "9" :
        print("YES")
        ans = True
        break
if not ans:
    print("NO")