from random import *

phenotypes = ['R', 'O', 'Y', 'G', 'B']

i = 0

gen0 = []

while i < 10:
     gen0 = gen0 + [phenotypes[(randint(0,4))]]
     i = i+1

gen0.sort()
print gen0


i = 0

gen1 = []

while i < 10:
     gen1 = gen1 + [gen0[(randint(0,9))]]
     i = i+1

gen1.sort()
print gen1

i = 0

gen2 = []

while i < 10:
     gen2 = gen2 + [gen1[(randint(0,9))]]
     i = i+1

gen2.sort()
print gen2






