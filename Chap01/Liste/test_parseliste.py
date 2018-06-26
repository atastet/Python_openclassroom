#!/usr/bin/python3.4
# -*-coding:Utf-8

maliste = [1, 2, 3, 4, 5]
i = 0
maliste.extend("END")
maliste.insert(2, "2.5")
while i < len(maliste):
	print(maliste[i])
	i += 1

for elt in maliste:
	print(elt)

i = 0
for i, elt in enumerate(maliste):
	print("A l'indice {} se trouve {}".format(i, elt))
