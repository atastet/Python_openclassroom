#!/usr/bin/python3.4
# -*-coding:Utf-8

string = "Hello World !"
print(string[1])
print(string[0])
print(string[-2])
print(string[-1])
l = len(string)
print(l)
# PARCOURIR
i = 0
while i < l:
	print(string[i])
	i += 1
print(string)

#SELECTION

pre = "salut"
print(pre[1:3])
print(pre[1:len(pre)])
print(pre[1:])

# Replace
i = 0
while i < l:
	print(string[i])
	print(string.replace("a", "o", len(string)))
	i += 1
