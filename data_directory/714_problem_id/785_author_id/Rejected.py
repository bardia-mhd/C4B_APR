import sys
from collections import Counter
from math import factorial

input = sys.stdin
output = sys.stdout

# input = open('input.txt')


def read_int():
    return [int(x) for x in input.readline().rstrip().split()]

l1, r1, l2, r2, k = read_int()
l = max(l1, l2)
r = min(r1, r2)
answer = r - l + 1
if l <= k <= r:
    answer -= 1

output.write('%d\n' % answer)