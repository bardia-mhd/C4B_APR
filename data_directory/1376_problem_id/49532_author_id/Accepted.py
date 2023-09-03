"""
Solution to the 706B problem on CodeForces.
"""
import sys
import math

def binary_search(k, target):
    beg, end = 1, target
    while beg + 1 < end:
        number = (beg + end) // 2
        if (lambda_function(target, k, number)):
            end = number
        else:
            beg = number
    if (lambda_function(target, k, number)):
        return number
    return int(number+1)

def lambda_function(target, k, num):
    sum = 0
    count = 0
    while True:
        exp = k ** count
        sum += math.floor(num / exp)
        if int(math.floor(num / exp)) == 0:
            return False
        if sum >= target:
            return True
        count += 1

def main():
    """
    The main method.
    """
    lines, k = (int(i) for i in str(sys.stdin.readline()).split(" "))
    if (int(lines/k) == 0):
        print(lines)
    else:
        print(binary_search(k, lines))

if __name__ == "__main__":
    main()