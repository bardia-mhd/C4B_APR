string = [x for x in input()]
reverse = string[::-1]

if string == reverse and len(string) % 2 == 1:
    print("YES")
else:
    for i in range(len(string)):
        if string[i] == reverse[i]:
            reverse[i] = ''

    count = 0

    for letter in reverse:
        if letter != '':
            count += 1

    print(["NO", "YES"][count == 2])