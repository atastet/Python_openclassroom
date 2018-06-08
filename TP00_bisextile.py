#!/usr/bin/python3.4
# -*-coding:Utf-8 -*

year = input("Which year you want to check ...")
answer = False
int(year)

if year % 4 != 0 :
	answer = False
elif year % 100 == 0 :
	if year % 400 == 0 :
		answer = True
	else :
		answer = False
else : 
	answer = True

if answer == True : 
	print("Yes it is a bissextile year !")
else : 
	print("Nope is not a bissextile year !") 
