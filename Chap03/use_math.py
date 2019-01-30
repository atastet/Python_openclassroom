# -*-coding:Utf-8 -*

import math
import random
from fractions import Fraction

print(math.pow(2,5)) #2^5
print(2**5)

a = math.cos(30)
b = math.degrees(a)
print(b)
print(math.ceil(b), math.floor(b))
print(math.pi)

un_demi = Fraction(1,2)
print(un_demi)

a = 0.25
un_quart = Fraction.from_float(a)
print(un_quart)

#RANDOM
print(random.random())
print(random.randrange(1,30,2))
TEST = ["a", "b", "c"]
print(random.choice(TEST))
random.shuffle(TEST)
print (TEST)