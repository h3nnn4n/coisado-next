import sqlite3

#
# Classe que irá acessar o arquivo do sqlite e manipular o
# banco de dados.
#
# TODO
# Especificar as exceptions
#

class OpenDBError(Exception):
    pass

class UnselectedDBError(Exception):
    pass
    
class DB():
    def __init__(self, dbPath):
        error = None
        try:
            self.conn = sqlite3.connect(dbPath)
        except Exception as e:
            error = e
        else:
            self.dbPath = dbPath
            self.cursor = self.conn.cursor()
            if self.checkDBFile():
                self.createTables()
            else:
                error = "invalid db file."
        if error:
            self.dbPath = None
            self.cursor = None
            self.conn = None
            raise OpenDBError("Error opening file: " + str(error))
    
    def isSelected(self):
        return self.dbPath != None

    def checkDBFile(self):
        error = None
        query = "SELECT name FROM sqlite_master WHERE type='table'"
        try:
            self.cursor.execute(query)
        except Exception as e:
            return False
        else:
            return True

    def __del__(self): 
        try:
            self.conn.close()
        except Exception as e:
            print(e)
            exit(1)
    
    def createTables(self):
        if self.isSelected():
            query = "CREATE TABLE IF NOT EXISTS PLAYERS (player TEXT, rating INT, sex TEXT, title TEXT)"
            self.cursor.execute(query)
            self.conn.commit()
        else:
            raise UnselectedDBError("No database file selected.")

    def selectAllPlayers(self):
        if self.isSelected():
            query = "SELECT * FROM PLAYERS"
            try:
                self.cursor.execute(query)
            except Exception as e:
                print(e)
                exit(1)
            return self.cursor.fetchall()
        else:
            raise UnselectedDBError("No database file selected.")

    def insertPlayer(self, player):
        if self.isSelected():
            player = tuple(player)
            query = "INSERT INTO PLAYERS VALUES (\"%s\",\"%s\",\"%s\",\"%s\")" % player
            try:
                self.cursor.execute(query)
                self.conn.commit()
            except Exception as e:
                print(e)
                exit(1)
        else:
            raise UnselectedDBError("No database file selected.")

if __name__ == "__main__":
    # Testes
    d = DB("/var/teste.db")
    p = ["Teste2", 1911, "Outro", "Fem"]
    #d.insertPlayer(p)
    #print(d.selectAllPlayers())
    # print(d.selectAllPlayers())
