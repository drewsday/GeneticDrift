#!/usr/bin/python -d

from pylab import *
from random import *
import sys
from PyQt4 import QtCore, QtGui
from newdriftgui import Ui_GeneticDrift
 
class MyForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self, parent)
    self.ui = Ui_GeneticDrift()
    self.ui.setupUi(self)
    QtCore.QObject.connect(self.ui.pushRun, QtCore.SIGNAL("clicked()"), self.run_sim )
 
  def run_sim(self):
    # The user will enter the population size and the number of generations in our GUI
    popsize = int(self.ui.linePopsize.text())
    numgen = int(self.ui.lineGenerations.text())
 
    # initialize some arrays
    allele = ['P' , 'Q']
    i = 0
    gen0 = []
    listP = []
    listQ = []

    # This next part randomly generates the initial population diversity. 
    # With a large population it is close to 50/50. With a small population it can be anything.
    while i < popsize:
         gen0 = gen0 + [allele[(randint(0,1))]]
##       print gen0
         i = i+1

    gen0.sort()
    print gen0
    listP.append(gen0.count('P'))
    listQ.append(gen0.count('Q'))

    # j is going to be the counter that steps through the generations
    j = 1
    prevgen = gen0

    while j < numgen+1:

	i = 0

	nextgen = []

        # This is where the magic happens.
        # Each time through the loop over the entire population we select a
        # random member of the previous generation to reproduce.
        # Effectively this means that some members will not reproduce and
        # that other members will produce multiple offspring.
	while i < popsize:
		nextgen = nextgen + [prevgen[(randint(0,popsize-1))]]
     		i = i+1

	# Clean up and count stats for each generation.
	prevgen = nextgen
	nextgen.sort()
	numP = nextgen.count('P')
##	print 'Generation', j, ':', nextgen, 'Number of P alleles: ', numP
	listP.append(nextgen.count('P'))
	listQ.append(nextgen.count('Q'))

	j = j+1
    # Output some info to the console. (This could be removed for the GUI version.)
    print 'P alleles in each generation:', listP
    print 'Q alleles in each generation:', listQ

    genlist = range(0,numgen+1)
    freqP = [float(i)/popsize for i in listP]
    freqQ = [float(i)/popsize for i in listQ]
    P = scatter(genlist,freqP,c='b',lw=1)
    Q = scatter(genlist,freqQ, c='r',lw=1)
    plot(genlist,freqP,c='b',lw=1)
    plot(genlist,freqQ, c='r',lw=1)
    ylabel('frequency')
    xlabel('generation')
    legend((P,Q),('P', 'Q'))
    ylim(ymin=0, ymax=1)
    show()

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  myapp = MyForm()
  myapp.show()
  sys.exit(app.exec_())

