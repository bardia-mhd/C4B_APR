n = input()
if n[1:] == n[1:].upper():
    print(n[0].upper() + n[1:].lower())
else:
    print(n)