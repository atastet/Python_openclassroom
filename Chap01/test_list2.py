#!/usr/bin/python3.4
# -*-coding:Utf-8

maliste = ['a', 'b', 1, 2 , "Hello You"]

print(maliste[0])
print(maliste[2])
print(maliste[4])
maliste.append("Hello world")
print(maliste[5])
maliste.append("Anthony")
print(maliste[6])
maliste.insert(2, 'c')
print(maliste[2])

maliste2 = ["12", "Hello"]
maliste3 = maliste + maliste2
print(maliste3)
maliste.extend(maliste2)
print(maliste)
maliste += maliste2
print(maliste)
maliste.remove('a')
print(maliste)
del maliste[1]
print(maliste)
