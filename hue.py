# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created: Fri May 23 12:19:36 2014
#      by: PyQt4 UI code generator 4.10.4
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(510, 150, 85, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.menuArquivo.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionSobre)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Sair", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Ajuda", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))

