import sys
import math

st = list("111111101010101111100101001111111100000100000000001010110001000001101110100110110000011010001011101101110101011001001111101001011101101110101100011000111100101011101100000101010101011010000101000001111111101010101010101010101111111000000001111101111100111100000000100010111100100001011110111111001110111001111111100100001000101100011100111010000101000111010001010011110000110001111110101100000011111111111111111000111001001011000111000010111010011010011010100100101010100010110010110101010000010101100000101010001111101000000000000010100011001101000111101011010101001001111101111000101010001110101101111111000100100001110001000000010011000100110000011010000010001101101001101110010010011011000011101011010001000111101010100110111010100110011101001101000001110110001010010101111000101111111000001000111011100001010110111110000000000001110010110100010100010110111111101000101111000110101011010100000100111010101111100100011011101110101001010000101000111111000101110100011010010010111111011010101110100100011011110110101110000100000100110011001111100111100000111111101101000101001101110010001")

k = []
i = 0
while(i < 32 * 32 + 33):
    k.append(st[i: i + 33])
    print(i)
    i += 33

a1, a2 = list(map(int, input().split()))
print(k[a1][a2])