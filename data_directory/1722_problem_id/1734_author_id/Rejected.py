x = int(input())
numbers = [int(i) for i in str(x)]
count = 0
for i in range(1, x + 1):
    if x % i == 0:
        digits = [int(j) for j in str(i)]
        flag = 0
        for j in digits:
            if j in numbers:
                flag = 1
                break
        if flag:
            count += 1
print (count)