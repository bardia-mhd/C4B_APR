n = int(input())
def banner(n):
    if n == 1:
        return ''
    elif n%2 == 0:
        return banner(n-1) + 'that I love '
    elif n%2 == 1:
        return banner(n-1) + 'that I hate '

string = 'I hate ' + banner(n) + 'it'
        
print(string)