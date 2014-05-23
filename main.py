import sys
import sqlite3
from PyQt4 import QtCore, QtGui

from mainWindow import *
from aboutPage import *
from addPlayer import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent =None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionSair.triggered.connect(self.sair)
        self.actionSobre.triggered.connect(self.about)
        self.actionAbrir.triggered.connect(self.loadPlayer)
        self.actionAdicionar.triggered.connect(self.insertPlayer)
        self.conn=None
        self.dbPath=None
    def sair(self):
        self.close()
    def about(self):
        sobre=aboutPage()
        sobre.exec_()
    def loadPlayer(self):
        self.dbPath=QtGui.QFileDialog.getOpenFileName(self,'Open file', '.')
        #print(filename)
        #self.conn=sqlite3.connect(filename)
    def insertPlayer(self):
        window=addPlayer(self.dbPath)
        window.exec_()
    def newPlayerSave(self):
        

class addPlayer(QtGui.QDialog, Ui_newPlayer):
    def __init__(self, dbPath, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.buttonOk.clicked.connect(self.confirm)
        self.buttonCancel.clicked.connect(self.cancel)
        self.dbPath=dbPath
    def confirm(self):
        self.setupUi(self)
        if self.dbPath!=None:
            self.conn=sqlite3.connect(self.dbPath)
        if self.dbPath!=None:
            self.conn.commit()
            self.conn.close()
        self.close()   
    def cancel(self):
        self.close()

class aboutPage(QtGui.QDialog, Ui_Sobre):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.labelLogo.setPixmap(QtGui.QPixmap('nextlogo.jpg'))
        self.labelLogo.setScaledContents(True)

def main():
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

main()
