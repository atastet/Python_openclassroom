#!/usr/bin/python3.4
# -*-coding:Utf-8

France = {10 : "Zizou", 1 : "Barthez", 9 : "Henry"}
for cle in France.keys():
	print(cle)

for cle in France.values():
	print(cle)

for cle, values in France.items():
	print(cle, values)
