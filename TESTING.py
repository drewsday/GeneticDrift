# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driftgui.ui'
#
# Created: Tue Aug 14 11:17:29 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_GeneticDrift(object):
    def setupUi(self, GeneticDrift):
        GeneticDrift.setObjectName(_fromUtf8("GeneticDrift"))
        GeneticDrift.resize(224, 281)
        self.linePopsize = QtGui.QLineEdit(GeneticDrift)
        self.linePopsize.setGeometry(QtCore.QRect(40, 40, 113, 27))
        self.linePopsize.setObjectName(_fromUtf8("linePopsize"))
        self.pushRun = QtGui.QPushButton(GeneticDrift)
        self.pushRun.setGeometry(QtCore.QRect(40, 200, 121, 27))
        self.pushRun.setObjectName(_fromUtf8("pushRun"))
        self.lineGenerations = QtGui.QLineEdit(GeneticDrift)
        self.lineGenerations.setGeometry(QtCore.QRect(40, 120, 113, 27))
        self.lineGenerations.setObjectName(_fromUtf8("lineGenerations"))
        self.label_2 = QtGui.QLabel(GeneticDrift)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(GeneticDrift)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(GeneticDrift)
        QtCore.QMetaObject.connectSlotsByName(GeneticDrift)

    def retranslateUi(self, GeneticDrift):
        GeneticDrift.setWindowTitle(QtGui.QApplication.translate("GeneticDrift", "Genetic Drift", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRun.setText(QtGui.QApplication.translate("GeneticDrift", "Run Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("GeneticDrift", "Number of generations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("GeneticDrift", "Population size", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    GeneticDrift = QtGui.QWidget()
    ui = Ui_GeneticDrift()
    ui.setupUi(GeneticDrift)
    GeneticDrift.show()
    sys.exit(app.exec_())

