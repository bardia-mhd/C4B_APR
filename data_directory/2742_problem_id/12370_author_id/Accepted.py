a = int(input())
x = a % 2;

if x == 1:
    b = int((a / 2));
    b = b - 1;
    str = "7";
    for i in range(0,b):
        str += "1"
else :
    b = int(a / 2);
    str = "1";
    b = b - 1
    for i in range(0,b):
        str += "1"
print (str)