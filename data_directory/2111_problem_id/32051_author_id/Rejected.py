#!/usr/bin/python3

a = int(input())
lst = 'Washington,Adams,Jefferson,Madison,Monroe,Adams,Jackson,Van Buren,Harrison,Tyler,Polk,Taylor,Fillmore,Pierce,Buchanan,Lincoln,Johnson,Grant,Hayes,Garfield,Arthur,Cleveland,Harrison,Cleveland,McKinley,Roosevelt,Taft,Wilson,Harding,Coolidge,Hoover,Roosevelt,Truman,Elsenhower,Kennedy,Johnson,Nixon,Ford,Carter,Reagan'.split(',')
print(lst[a - 1])