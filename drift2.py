from random import *

phenotypes = ['R', 'O', 'Y', 'G', 'B']

i = 0

gen0 = []

while i < 100:
     gen0 = gen0 + [phenotypes[(randint(0,4))]]
     i = i+1

gen0.sort()
print gen0

j = 1
prevgen = gen0

while j < 100:

	i = 0

	nextgen = []

	while i < 100:
		nextgen = nextgen + [prevgen[(randint(0,99))]]
     		i = i+1
	
	prevgen = nextgen
	nextgen.sort()
	print 'Generation', j, ':', nextgen
	j = j+1
