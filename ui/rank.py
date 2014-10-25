# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rank.ui'
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

class Ui_rankDialog(object):
    def setupUi(self, rankDialog):
        rankDialog.setObjectName(_fromUtf8("rankDialog"))
        rankDialog.resize(412, 416)
        self.frame = QtGui.QFrame(rankDialog)
        self.frame.setGeometry(QtCore.QRect(0, 0, 411, 411))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tableRank = QtGui.QTableWidget(self.frame)
        self.tableRank.setGeometry(QtCore.QRect(0, 10, 411, 401))
        self.tableRank.setObjectName(_fromUtf8("tableRank"))
        self.tableRank.setColumnCount(0)
        self.tableRank.setRowCount(0)

        self.retranslateUi(rankDialog)
        QtCore.QMetaObject.connectSlotsByName(rankDialog)

    def retranslateUi(self, rankDialog):
        rankDialog.setWindowTitle(_translate("rankDialog", "Dialog", None))

