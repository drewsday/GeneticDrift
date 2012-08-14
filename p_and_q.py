from pylab import *
from random import *

allele = ['P' , 'Q']

i = 0

gen0 = []
listP = []
listQ = []

while i < 10000:
     gen0 = gen0 + [allele[(randint(0,1))]]
##     print gen0
     i = i+1

gen0.sort()
print gen0
listP.append(gen0.count('P'))
listQ.append(gen0.count('Q'))

j = 1
prevgen = gen0

while j < 101:

	i = 0

	nextgen = []

	while i < 10000:
		nextgen = nextgen + [prevgen[(randint(0,9999))]]
     		i = i+1
	
	prevgen = nextgen
	nextgen.sort()
	numP = nextgen.count('P')
##	print 'Generation', j, ':', nextgen, 'Number of P alleles: ', numP
	listP.append(nextgen.count('P'))
	listQ.append(nextgen.count('Q'))

	j = j+1

print 'P alleles in each generation:', listP
print 'Q alleles in each generation:', listQ

genlist = range(0,101)
freqP = [float(i)/10000 for i in listP]
freqQ = [float(i)/10000 for i in listQ]
P = scatter(genlist,freqP,c='b')
Q = scatter(genlist,freqQ, c='r')
ylabel('frequency')
legend((P,Q),('P', 'Q'))
ylim(ymin=0, ymax=1)
show()
