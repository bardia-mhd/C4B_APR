a = (int)(raw_input())
if -128 <= a <= 127:
    print('byte')
elif -32768 <= a <= 32767:
    print('short')
elif -2147483648 <= a <= 2147483647:
    print('int')
elif -9223372036854775808 <= a <= 9223372036854775807:
    print ('long')
else: print('BigInteger')