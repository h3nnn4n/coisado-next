# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTournament.ui'
#
# Created: Thu Oct  2 21:34:39 2014
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

class Ui_newTournament(object):
    def setupUi(self, newTournament):
        newTournament.setObjectName(_fromUtf8("newTournament"))
        newTournament.resize(662, 455)
        self.frame = QtGui.QFrame(newTournament)
        self.frame.setGeometry(QtCore.QRect(0, 0, 661, 451))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tableWidgetPlayers = QtGui.QTableWidget(self.frame)
        self.tableWidgetPlayers.setGeometry(QtCore.QRect(4, 44, 651, 401))
        self.tableWidgetPlayers.setMaximumSize(QtCore.QSize(771, 471))
        self.tableWidgetPlayers.setObjectName(_fromUtf8("tableWidgetPlayers"))
        self.tableWidgetPlayers.setColumnCount(0)
        self.tableWidgetPlayers.setRowCount(0)
        self.frame_2 = QtGui.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(4, 1, 651, 41))
        self.frame_2.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName(_fromUtf8("frame_2"))
        self.buttonImport = QtGui.QPushButton(self.frame_2)
        self.buttonImport.setGeometry(QtCore.QRect(10, 10, 91, 23))
        self.buttonImport.setObjectName(_fromUtf8("buttonImport"))
        self.buttonEmparcerar = QtGui.QPushButton(self.frame_2)
        self.buttonEmparcerar.setGeometry(QtCore.QRect(110, 10, 89, 23))
        self.buttonEmparcerar.setObjectName(_fromUtf8("buttonEmparcerar"))
        self.buttonDelete = QtGui.QPushButton(self.frame_2)
        self.buttonDelete.setGeometry(QtCore.QRect(210, 10, 89, 23))
        self.buttonDelete.setObjectName(_fromUtf8("buttonDelete"))

        self.retranslateUi(newTournament)
        QtCore.QMetaObject.connectSlotsByName(newTournament)

    def retranslateUi(self, newTournament):
        newTournament.setWindowTitle(_translate("newTournament", "Dialog", None))
        self.buttonImport.setText(_translate("newTournament", "Importar", None))
        self.buttonEmparcerar.setText(_translate("newTournament", "Emparcerar", None))
        self.buttonDelete.setText(_translate("newTournament", "Remover", None))

