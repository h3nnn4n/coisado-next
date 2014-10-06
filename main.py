import sys
from PyQt4 import *
from Database import *
from ui.mainWindow import *
from ui.aboutPage import *
from ui.addPlayer import *
from ui.newTournament import *

class MainWindow(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent = None):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        self.actionSair.triggered.connect(self.sair)
        self.actionSobre.triggered.connect(self.about)
        self.actionAbrir.triggered.connect(self.loadPlayer)
        self.actionNovo.triggered.connect(self.newPlayerSave)
        self.actionAdicionar.triggered.connect(self.insertPlayer)
        self.buttonNovoTorneio.clicked.connect(self.novoTorneio)
        self.buttonRemover.clicked.connect(self.removerSelecionado)
        self.db = None

        self.tableWidgetPlayer.setColumnCount(6)
        self.tableWidgetPlayer.setRowCount(0)
        self.tableWidgetPlayer.verticalHeader().hide()
        self.tableWidgetPlayer.horizontalHeader().hide()
        self.tableWidgetPlayer.setSelectionBehavior(self.tableWidgetPlayer.SelectRows)

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
                btn.clicked.connect(self.removerSelecionado)
                self.tableWidgetPlayer.setCellWidget(i, 5, btn)

                btn = QtGui.QPushButton(self)
                btn.setText('Atualizar')
                # btn.clicked.connect(self.removerSelecionado)
                self.tableWidgetPlayer.setCellWidget(i, 4, btn)

    def removerSelecionado(self):
        rows=self.tableWidgetPlayer.selectionModel().selectedRows()
        for r in rows:
            print(r.item(0,0))
            # TODO
            # remover da db o item selecionado
            player=""
            self.db.deletePlayer(player)
            self.tableWidgetPlayer.removeRow(r.row())

    def novoTorneio(self):
        tournament=newTournament(self.db)
        tournament.exec_()

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

class newTournament(QtGui.QDialog, Ui_newTournament):
    def __init__(self,db,parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.buttonEmparcerar.clicked.connect(self.emparcerar)
        self.buttonPrev.clicked.connect(self.prevRound)
        self.buttonNext.clicked.connect(self.nextRound)
        self.buttonQuit.clicked.connect(self.sair)
        self.buttonWhiteWins.clicked.connect(self.whiteWins)
        self.buttonBlackWins.clicked.connect(self.blackWins)
        self.buttonDraws.clicked.connect(self.draws)

        self.tableWidgetPlayers.setColumnCount(5)
        self.tableWidgetPlayers.setRowCount(1)
        self.tableWidgetPlayers.setSelectionBehavior(self.tableWidgetPlayers.SelectRows)

        self.players=[]
        self.points=[]
        self.rounds=[]
        self.nrounds=-1
        self.db=db

        self.is_emparcered=0
        self.active_round=0

    def whiteWins(self):
        rows=self.tableWidgetPlayers.selectionModel().selectedRows()
        for r in rows:
            print(r.data())

        for i in range(0,len(self.players)-1):
            if r.data()==self.players[i]:
                self.points[i]+=1

        for i in range(0,len(self.players)-1):
            print(self.players[i]+" "+str(self.points[i]))

        self.showRound()

    def draws(self):
        rows=self.tableWidgetPlayers.selectedItems()

        for i in range(0,len(rows)):
            for j in range(0,len(self.players)-1):
                if str(rows[i].data(0))==self.players[j]:
                    self.points[j]+=0.5

        print("---")
        for i in range(0,len(self.players)-1):
            print(self.players[i]+" "+str(self.points[i]))

        self.showRound()

    def blackWins(self):
        rows=self.tableWidgetPlayers.selectedItems()

        for i in range(1,len(rows)):
            for j in range(0,len(self.players)-1):
                if str(rows[i].data(0))==self.players[j]:
                    self.points[j]+=1

        print("---")
        for i in range(0,len(self.players)-1):
            print(self.players[i]+" "+str(self.points[i]))

        self.showRound()

    def pointTo(self,name,p):
        for i,n in enumerate(self.players):
            if n==name:
                self.rounds[i]+=p

    def showRound(self):
        self.tableWidgetPlayers.setColumnCount(5)
        self.tableWidgetPlayers.setRowCount(0)
        self.tableWidgetPlayers.clear()

        rounds=self.rounds[self.active_round]

        l=len(rounds[0])

        print(self.players)

        for i in range(0,l):
            print(rounds[0][i]+" vs "+rounds[1][i])

            self.tableWidgetPlayers.insertRow(i)

            add=QtGui.QTableWidgetItem(rounds[0][i])
            self.tableWidgetPlayers.setItem(i,0,add)

            add=QtGui.QTableWidgetItem(rounds[1][i])
            self.tableWidgetPlayers.setItem(i,4,add)

            for j in range(0,len(self.players)-1):
                if rounds[1][i]==self.players[j]:
                    add=QtGui.QTableWidgetItem(str(self.points[j]))
                    self.tableWidgetPlayers.setItem(i,3,add)

            for j in range(0,len(self.players)-1):
                if rounds[0][i]==self.players[j]:
                    add=QtGui.QTableWidgetItem(str(self.points[j]))
                    self.tableWidgetPlayers.setItem(i,1,add)

            """btn = QtGui.QPushButton(self)
            btn.setText('1 - 0')
            btn.clicked.connect(self.showRound)
            self.tableWidgetPlayers.setCellWidget(i, 1, btn)

            btn = QtGui.QPushButton(self)
            btn.setText('.5 - .5')
            #btn.clicked.connect(self.removerSelecionado)
            self.tableWidgetPlayers.setCellWidget(i, 2, btn)

            btn = QtGui.QPushButton(self)
            btn.setText('0 - 1')
            #btn.clicked.connect(self.removerSelecionado)
            self.tableWidgetPlayers.setCellWidget(i, 3, btn)
            """

    def nextRound(self):
        if self.is_emparcered==1:
            if self.active_round<self.nrounds:
                self.active_round+=1
                self.labelRound.setText("Round: " + str(self.active_round+1))
                print("Round: " + str(self.active_round+1))
                self.showRound()

    def prevRound(self):
        if self.is_emparcered==1:
            if self.active_round>0:
                self.active_round-=1
                self.labelRound.setText("Round: " + str(self.active_round+1))
                print("Round: " + str(self.active_round+1))
                self.showRound()


    def deleteSelecionado(self):
        rows=self.tableWidgetPlayers.selectionModel().SelectRows()
        for r in rows:
            # TODO
            # Remove from database
            self.tableWidgetPlayers.removeRow(r.rows())

    def emparcerar(self):
        data=self.db.selectAllPlayers()
        for i in enumerate(data):
            self.players.append(i[1][0])

        print("The players are: ", end="")
        if len(self.players) % 2 == 1: self.players.append("BYE")
        for i in self.players:
            print(i,end=" + ")
        print("\n")

        self.rounds=[]
        self.nrounds=0

        for i in range(len(self.players)-1):
            self.nrounds+=1
            mid = len(self.players) / 2
            l1 = self.players[:int(mid)]
            l2 = self.players[int(mid):]
            l2.reverse()

            l3=[]

            if(i % 2 == 1):
                l3.append(l1)
                l3.append(l2)
                self.rounds.append(l3)
            else:
                l3.append(l2)
                l3.append(l1)
                self.rounds.append(l3)

            self.players.insert(1, self.players.pop())

        self.is_emparcered=1
        self.labelRound.setText("Round: " + str(self.active_round+1))

        for i in range(len(self.players)):
            self.points.append(0)

        self.showRound()

    def sair(self):
        self.close()

if __name__ == "__main__":
    app=QtGui.QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())
