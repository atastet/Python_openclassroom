#!/usr/bin/python3.4
# -*-coding:Utf-8

quantity = 7
fruits = [10, 7, 8, 11]

fruits_2 = [nb - quantity for nb in fruits if nb - quantity > 0]
print(fruits_2)
