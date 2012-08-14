# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'driftgui.ui'
#
# Created: Tue Aug  7 09:59:32 2012
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(224, 281)
        self.linePopsize = QtGui.QLineEdit(Form)
        self.linePopsize.setGeometry(QtCore.QRect(40, 40, 113, 27))
        self.linePopsize.setObjectName(_fromUtf8("linePopsize"))
        self.pushRun = QtGui.QPushButton(Form)
        self.pushRun.setGeometry(QtCore.QRect(40, 200, 121, 27))
        self.pushRun.setObjectName(_fromUtf8("pushRun"))
        self.lineGenerations = QtGui.QLineEdit(Form)
        self.lineGenerations.setGeometry(QtCore.QRect(40, 120, 113, 27))
        self.lineGenerations.setObjectName(_fromUtf8("lineGenerations"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 20, 121, 17))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.pushRun.setText(QtGui.QApplication.translate("Form", "Run Simulation", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Number of generations", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Population size", None, QtGui.QApplication.UnicodeUTF8))

