import sys
lst = [int(i) for i in input().split()]
def check(number):
    lst = []
    i = int((number / 50)) % 475
    for j in range(25):
        i = (i * 96 + 42) % 475
        lst.append(i + 26)
    return lst
if lst[0] in check(lst[1]) and lst[1] >= lst[2]:
    print(0)
    sys.exit()
n2 = lst[1]
while n2 >= lst[2]:
    n2 = n2 - 50
    if lst[0] in check(n2):
        print(0)
        sys.exit()
else:
    n1 = lst[1]
    counter = 0
    while True:
        n1 = n1 + 50
        counter += 1
        if lst[0] in check(n1) and n1 >= lst[2]:
            if counter % 2 == 0:
                print(int(counter / 2))
                break
            else:
                print(int(counter / 2) + 1)
                break