#!/usr/bin/env python
# -*- coding: utf-8 -*-
cur = input()

all_upper = True
if(len(cur) == 1):
	if(cur.islower()):
		cur = cur.upper()
else:
	for i in range(1, len(cur)):
		if(not cur[i].isupper()):
			all_upper = False
			break
	if(all_upper and cur[0].isupper()):
		cur = cur.lower()
	elif(all_upper and cur[0].islower()):	
		cur = cur[0].upper() + cur[1:].lower()
print(cur)