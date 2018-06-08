#!/usr/bin/python3.4
# -*-coding:Utf-8 -

i = 1
while i < 20 :
	if i % 3 == 0:
		i += 4
		print("On incremente de 4 donc i =", i)
		continue
	print("i =", i)
	i += 1
