alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
string = input()
n = len(string)
results = "NO"
for x in range(n):
    for y in alphabet:
        temp = list(string)
        a = temp[x]
        temp[x] = y
        if temp[::-1] == temp and a != y:
            results = "YES"
            break
    if results == "YES":
        break
print(results)