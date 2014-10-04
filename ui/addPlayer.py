# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addPlayer.ui'
#
# Created: Fri Oct  3 14:19:21 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_newPlayer(object):
    def setupUi(self, newPlayer):
        newPlayer.setObjectName(_fromUtf8("newPlayer"))
        newPlayer.resize(357, 117)
        self.buttonOk = QtGui.QPushButton(newPlayer)
        self.buttonOk.setGeometry(QtCore.QRect(90, 80, 85, 27))
        self.buttonOk.setObjectName(_fromUtf8("buttonOk"))
        self.buttonCancel = QtGui.QPushButton(newPlayer)
        self.buttonCancel.setGeometry(QtCore.QRect(190, 80, 85, 27))
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.txtBoxPlayerName = QtGui.QLineEdit(newPlayer)
        self.txtBoxPlayerName.setGeometry(QtCore.QRect(60, 10, 131, 20))
        self.txtBoxPlayerName.setObjectName(_fromUtf8("txtBoxPlayerName"))
        self.txtBoxPlayerRating = QtGui.QLineEdit(newPlayer)
        self.txtBoxPlayerRating.setGeometry(QtCore.QRect(60, 40, 131, 20))
        self.txtBoxPlayerRating.setObjectName(_fromUtf8("txtBoxPlayerRating"))
        self.label = QtGui.QLabel(newPlayer)
        self.label.setGeometry(QtCore.QRect(10, 10, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(newPlayer)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.comboBoxTitle = QtGui.QComboBox(newPlayer)
        self.comboBoxTitle.setGeometry(QtCore.QRect(280, 10, 73, 28))
        self.comboBoxTitle.setObjectName(_fromUtf8("comboBoxTitle"))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.comboBoxTitle.addItem(_fromUtf8(""))
        self.label_3 = QtGui.QLabel(newPlayer)
        self.label_3.setGeometry(QtCore.QRect(220, 10, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(newPlayer)
        self.label_4.setGeometry(QtCore.QRect(220, 40, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.comboBoxSex = QtGui.QComboBox(newPlayer)
        self.comboBoxSex.setGeometry(QtCore.QRect(280, 40, 73, 28))
        self.comboBoxSex.setEditable(False)
        self.comboBoxSex.setObjectName(_fromUtf8("comboBoxSex"))
        self.comboBoxSex.addItem(_fromUtf8(""))
        self.comboBoxSex.addItem(_fromUtf8(""))

        self.retranslateUi(newPlayer)
        QtCore.QMetaObject.connectSlotsByName(newPlayer)

    def retranslateUi(self, newPlayer):
        newPlayer.setWindowTitle(_translate("newPlayer", "Dialog", None))
        self.buttonOk.setText(_translate("newPlayer", "Ok", None))
        self.buttonCancel.setText(_translate("newPlayer", "Cancelar", None))
        self.label.setText(_translate("newPlayer", "Nome:", None))
        self.label_2.setText(_translate("newPlayer", "Rating:", None))
        self.comboBoxTitle.setItemText(0, _translate("newPlayer", "WM", None))
        self.comboBoxTitle.setItemText(1, _translate("newPlayer", "GWM", None))
        self.comboBoxTitle.setItemText(2, _translate("newPlayer", "IM", None))
        self.comboBoxTitle.setItemText(3, _translate("newPlayer", "GIM", None))
        self.comboBoxTitle.setItemText(4, _translate("newPlayer", "FM", None))
        self.comboBoxTitle.setItemText(5, _translate("newPlayer", "WFM", None))
        self.comboBoxTitle.setItemText(6, _translate("newPlayer", "Outro", None))
        self.label_3.setText(_translate("newPlayer", "Titulo", None))
        self.label_4.setText(_translate("newPlayer", "Sexo", None))
        self.comboBoxSex.setItemText(0, _translate("newPlayer", "Masc", None))
        self.comboBoxSex.setItemText(1, _translate("newPlayer", "Fem", None))

