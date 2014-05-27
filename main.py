import sys
from PyQt4 import * #QtCore, QtGui
from Database import *
from ui.mainWindow import *
from ui.aboutPage import *
from ui.addPlayer import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionSair.triggered.connect(self.sair)
        self.actionSobre.triggered.connect(self.about)
        self.actionAbrir.triggered.connect(self.loadPlayer)
        self.actionNovo.triggered.connect(self.newPlayerSave)
        self.actionAdicionar.triggered.connect(self.insertPlayer)
        self.db = None

        self.tableWidgetPlayer.setColumnCount(6)
        self.tableWidgetPlayer.setRowCount(0)
        self.tableWidgetPlayer.verticalHeader().hide()
        self.tableWidgetPlayer.horizontalHeader().hide()
    
    def atualizar(self):
        print("Opening " + self.dbPath)
        try:
            self.db = DB(self.dbPath)
        except OpenDBError as e:
            msg = "Erro ao abrir o arquivo " + self.dbPath + "." 
            QtGui.QMessageBox.critical(self, "Erro!", msg, QtGui.QMessageBox.Ok)
        else:
            data = self.db.selectAllPlayers()
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

    def sair(self):
        self.close()

    def about(self):
        sobre=aboutPage()
        sobre.exec_()

    def loadPlayer(self):
        self.dbPath = QtGui.QFileDialog.getOpenFileName(self,'Open file', '.')
        self.atualizar()

    def insertPlayer(self):
        window=addPlayer(self.db)
        window.exec_()
        self.atualizar()

    def newPlayerSave(self):
        self.error=None
        try:
            self.dbPath=QtGui.QFileDialog.getOpenFileName(self,'Open file', '.')
            self.db = DB(self.dbPath)
            self.db.createTables()
        except sqlite3.OperationalError as e:
            error="Error:\n%s" % e
        if error:
            QtGui.QMessageBox.critical(self, "Error!",error, QtGui.QMessageBox.Ok)


class addPlayer(QtGui.QDialog, Ui_newPlayer):
    def __init__(self, db, parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.buttonOk.clicked.connect(self.confirm)
        self.buttonCancel.clicked.connect(self.cancel)
        self.txtBoxPlayerName.setPlaceholderText("Nome Completo")
        self.txtBoxPlayerRating.setPlaceholderText("1500")
        self.db = db

    def confirm(self):
        error = None
        player = []
        player.append(self.txtBoxPlayerName.displayText())
        player.append(self.txtBoxPlayerRating.displayText())
        player.append(str(self.comboBoxTitle.currentText()))
        player.append(str(self.comboBoxSex.currentText()))
        
        try:
            self.db.insertPlayer(player)
        except UnselectedDBError as e:
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

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

