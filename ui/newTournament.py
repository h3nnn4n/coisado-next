# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newTournament.ui'
#
# Created: Tue Oct  7 23:36:42 2014
#      by: PyQt4 UI code generator 4.11.2
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
        self.buttonImport.setGeometry(QtCore.QRect(5, 6, 81, 27))
        self.buttonImport.setObjectName(_fromUtf8("buttonImport"))
        self.buttonEmparcerar = QtGui.QPushButton(self.frame_2)
        self.buttonEmparcerar.setGeometry(QtCore.QRect(90, 6, 81, 27))
        self.buttonEmparcerar.setObjectName(_fromUtf8("buttonEmparcerar"))
        self.buttonDelete = QtGui.QPushButton(self.frame_2)
        self.buttonDelete.setGeometry(QtCore.QRect(173, 6, 81, 27))
        self.buttonDelete.setObjectName(_fromUtf8("buttonDelete"))
        self.buttonPrev = QtGui.QPushButton(self.frame_2)
        self.buttonPrev.setGeometry(QtCore.QRect(260, 8, 26, 24))
        self.buttonPrev.setObjectName(_fromUtf8("buttonPrev"))
        self.buttonNext = QtGui.QPushButton(self.frame_2)
        self.buttonNext.setGeometry(QtCore.QRect(350, 8, 25, 25))
        self.buttonNext.setObjectName(_fromUtf8("buttonNext"))
        self.labelRound = QtGui.QLabel(self.frame_2)
        self.labelRound.setGeometry(QtCore.QRect(290, 14, 57, 14))
        self.labelRound.setObjectName(_fromUtf8("labelRound"))
        self.buttonQuit = QtGui.QPushButton(self.frame_2)
        self.buttonQuit.setGeometry(QtCore.QRect(550, 6, 96, 27))
        self.buttonQuit.setObjectName(_fromUtf8("buttonQuit"))
        self.buttonWhiteWins = QtGui.QPushButton(self.frame_2)
        self.buttonWhiteWins.setGeometry(QtCore.QRect(419, 8, 39, 25))
        self.buttonWhiteWins.setObjectName(_fromUtf8("buttonWhiteWins"))
        self.buttonDraws = QtGui.QPushButton(self.frame_2)
        self.buttonDraws.setGeometry(QtCore.QRect(460, 8, 48, 25))
        self.buttonDraws.setObjectName(_fromUtf8("buttonDraws"))
        self.buttonBlackWins = QtGui.QPushButton(self.frame_2)
        self.buttonBlackWins.setGeometry(QtCore.QRect(510, 8, 39, 25))
        self.buttonBlackWins.setObjectName(_fromUtf8("buttonBlackWins"))

        self.retranslateUi(newTournament)
        QtCore.QMetaObject.connectSlotsByName(newTournament)

    def retranslateUi(self, newTournament):
        newTournament.setWindowTitle(_translate("newTournament", "Dialog", None))
        self.buttonImport.setText(_translate("newTournament", "Importar", None))
        self.buttonEmparcerar.setText(_translate("newTournament", "Emparcerar", None))
        self.buttonDelete.setText(_translate("newTournament", "Remover", None))
        self.buttonPrev.setText(_translate("newTournament", "<", None))
        self.buttonNext.setText(_translate("newTournament", ">", None))
        self.labelRound.setText(_translate("newTournament", "Round:", None))
        self.buttonQuit.setText(_translate("newTournament", "Fechar", None))
        self.buttonWhiteWins.setText(_translate("newTournament", "1-0", None))
        self.buttonDraws.setText(_translate("newTournament", "½ - ½", None))
        self.buttonBlackWins.setText(_translate("newTournament", "0-1", None))

