string = input()
if string.isupper() or string[0].islower() and string[1:].isupper():
	print(''.join(c.lower() if c.isupper() else c.upper() for c in string))
elif len(string) == 1 and string.islower():
	print(string.upper())
else:
	print(string)