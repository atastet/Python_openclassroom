#!/usr/bin/python3.4
# -*-coding:Utf-8 -

string = "Hello World !"
voyelle = "AEIOUYaeiouy"

for letter in string : 
	if letter in voyelle:
		print(letter)
	else :
		print("*")

