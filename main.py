import sys
import sqlite3
from PyQt4 import * #QtCore, QtGui

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
        self.actionNovo.triggered.connect(self.newPlayerSave)
        self.actionAdicionar.triggered.connect(self.insertPlayer)
        self.conn=None
        self.dbPath=None

        self.tableWidgetPlayer.setColumnCount(6)
        self.tableWidgetPlayer.setRowCount(0)

    def atualizar(self):
        print("Opening " + self.dbPath)
        self.conn=sqlite3.connect(self.dbPath)
        c=self.conn.cursor()
        c.execute('select * from players')
        data=c.fetchall()
        self.tableWidgetPlayer.clear()
        for i, item in enumerate(data):
            self.tableWidgetPlayer.insertRow(i)
            for j in range(0,4):
                add=newitem = QtGui.QTableWidgetItem(data[i][j])
                self.tableWidgetPlayer.setItem(i,j,add)                
            btn = QtGui.QPushButton(self)
            btn.setText('Remover')
            self.tableWidgetPlayer.setCellWidget(i, 5, btn)
            btn = QtGui.QPushButton(self)
            btn.setText('Atualizar')
            self.tableWidgetPlayer.setCellWidget(i, 4, btn)
        self.conn.close()

    def sair(self):
        self.close()

    def about(self):
        sobre=aboutPage()
        sobre.exec_()

    def loadPlayer(self):
        self.dbPath=QtGui.QFileDialog.getOpenFileName(self,'Open file', '.')
        self.atualizar()

    def insertPlayer(self):
        window=addPlayer(self.dbPath)
        window.exec_()
        self.atualizar()

    def newPlayerSave(self):
        self.error=None
        try:
            self.dbPath=QtGui.QFileDialog.getOpenFileName(self,'Open file', '.')
            self.conn=sqlite3.connect(self.dbPath)
            self.conn.execute("create table players (Player text, Rating text, Sex text, Title text)")
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError as e:
            error="Error:\n%s" % e

        if error:
            QtGui.QMessageBox.critical(self, "Error!",error, QtGui.QMessageBox.Ok)


class addPlayer(QtGui.QDialog, Ui_newPlayer):
    def __init__(self, dbPath, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.buttonOk.clicked.connect(self.confirm)
        self.buttonCancel.clicked.connect(self.cancel)
        self.txtBoxPlayerName.setPlaceholderText("Nome Completo")
        self.txtBoxPlayerRating.setPlaceholderText("1500")
        self.dbPath=dbPath

    def confirm(self):
        error=None
        print(self.txtBoxPlayerName.displayText())
        commit="insert into players values(\"%s\",\"%s\",\"%s\",\"%s\")" % (\
        self.txtBoxPlayerName.displayText(),\
        self.txtBoxPlayerRating.displayText(),\
        str(self.comboBoxTitle.currentText()),\
        str(self.comboBoxSex.currentText()))
        print(commit)
        try:
            self.conn=sqlite3.connect(self.dbPath)
            self.conn.execute(commit)
            self.conn.commit()
            self.conn.close()
        except sqlite3.OperationalError as e:
            error="Error:\n%s" % e

        if error:
            QtGui.QMessageBox.critical(self, "Error!", error, QtGui.QMessageBox.Ok)

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
