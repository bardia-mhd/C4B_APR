digits = [2, 3, 5, 6]
string = input()
numbers = string.split(" ")
for x in range(4):
    numbers[x] = int(numbers[x])
maximum = min([numbers[0], numbers[2], numbers[3]])
numbers[0] -= maximum
maximum *= 256
maximum += min([numbers[0], numbers[1]]) * 32
print(maximum)