# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(776, 543)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 771, 501))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.tableWidgetPlayer = QtGui.QTableWidget(self.frame)
        self.tableWidgetPlayer.setGeometry(QtCore.QRect(0, 30, 771, 471))
        self.tableWidgetPlayer.setMaximumSize(QtCore.QSize(771, 471))
        self.tableWidgetPlayer.setObjectName(_fromUtf8("tableWidgetPlayer"))
        self.tableWidgetPlayer.setColumnCount(0)
        self.tableWidgetPlayer.setRowCount(0)
        self.buttonRemover = QtGui.QPushButton(self.frame)
        self.buttonRemover.setGeometry(QtCore.QRect(2, 2, 85, 27))
        self.buttonRemover.setObjectName(_fromUtf8("buttonRemover"))
        self.buttonAtualizar = QtGui.QPushButton(self.frame)
        self.buttonAtualizar.setGeometry(QtCore.QRect(90, 2, 85, 27))
        self.buttonAtualizar.setObjectName(_fromUtf8("buttonAtualizar"))
        self.buttonNovoTorneio = QtGui.QPushButton(self.frame)
        self.buttonNovoTorneio.setGeometry(QtCore.QRect(178, 3, 89, 25))
        self.buttonNovoTorneio.setObjectName(_fromUtf8("buttonNovoTorneio"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuArquivo = QtGui.QMenu(self.menubar)
        self.menuArquivo.setObjectName(_fromUtf8("menuArquivo"))
        self.menuSobre = QtGui.QMenu(self.menubar)
        self.menuSobre.setObjectName(_fromUtf8("menuSobre"))
        self.menuJogadores = QtGui.QMenu(self.menubar)
        self.menuJogadores.setObjectName(_fromUtf8("menuJogadores"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionSair = QtGui.QAction(MainWindow)
        self.actionSair.setObjectName(_fromUtf8("actionSair"))
        self.actionSobre = QtGui.QAction(MainWindow)
        self.actionSobre.setObjectName(_fromUtf8("actionSobre"))
        self.actionAdicionar = QtGui.QAction(MainWindow)
        self.actionAdicionar.setObjectName(_fromUtf8("actionAdicionar"))
        self.actionAbrir = QtGui.QAction(MainWindow)
        self.actionAbrir.setObjectName(_fromUtf8("actionAbrir"))
        self.actionNovo = QtGui.QAction(MainWindow)
        self.actionNovo.setObjectName(_fromUtf8("actionNovo"))
        self.menuArquivo.addAction(self.actionSair)
        self.menuSobre.addAction(self.actionSobre)
        self.menuJogadores.addAction(self.actionAbrir)
        self.menuJogadores.addAction(self.actionNovo)
        self.menuJogadores.addAction(self.actionAdicionar)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuJogadores.menuAction())
        self.menubar.addAction(self.menuSobre.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.buttonRemover.setText(_translate("MainWindow", "Remover", None))
        self.buttonAtualizar.setText(_translate("MainWindow", "Atualizar", None))
        self.buttonNovoTorneio.setText(_translate("MainWindow", "Criar torneio", None))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo", None))
        self.menuSobre.setTitle(_translate("MainWindow", "Ajuda", None))
        self.menuJogadores.setTitle(_translate("MainWindow", "Jogadores", None))
        self.actionSair.setText(_translate("MainWindow", "Sair", None))
        self.actionSobre.setText(_translate("MainWindow", "Sobre", None))
        self.actionAdicionar.setText(_translate("MainWindow", "Adicionar", None))
        self.actionAbrir.setText(_translate("MainWindow", "Abrir", None))
        self.actionNovo.setText(_translate("MainWindow", "Novo", None))

