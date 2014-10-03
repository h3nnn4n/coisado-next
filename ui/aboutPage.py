# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutPage.ui'
#
# Created: Thu Oct  2 21:34:38 2014
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

class Ui_Sobre(object):
    def setupUi(self, Sobre):
        Sobre.setObjectName(_fromUtf8("Sobre"))
        Sobre.resize(400, 300)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Sobre.sizePolicy().hasHeightForWidth())
        Sobre.setSizePolicy(sizePolicy)
        self.label = QtGui.QLabel(Sobre)
        self.label.setGeometry(QtCore.QRect(80, 30, 251, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.labelName = QtGui.QLabel(Sobre)
        self.labelName.setGeometry(QtCore.QRect(180, 10, 31, 31))
        self.labelName.setAlignment(QtCore.Qt.AlignCenter)
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.labelLogo = QtGui.QLabel(Sobre)
        self.labelLogo.setGeometry(QtCore.QRect(80, 60, 244, 188))
        self.labelLogo.setObjectName(_fromUtf8("labelLogo"))

        self.retranslateUi(Sobre)
        QtCore.QMetaObject.connectSlotsByName(Sobre)

    def retranslateUi(self, Sobre):
        Sobre.setWindowTitle(_translate("Sobre", "Dialog", None))
        self.label.setText(_translate("Sobre", "Núcleo de estudos em Xadrez e Tecnologias", None))
        self.labelName.setText(_translate("Sobre", "NexT", None))
        self.labelLogo.setText(_translate("Sobre", "TextLabel", None))

