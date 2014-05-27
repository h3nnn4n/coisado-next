import sqlite3

#
# Classe que irá acessar o arquivo do sqlite e manipular o
# banco de dados.
#
# TODO
# Especificar as exceptions
#

class DB():
    def __init__(self, dbPath):
        error = None
        try:
            self.conn = sqlite3.connect(dbPath)
        except Exception as e:
            print(e)
            exit(1)
        self.cursor = self.conn.cursor()
        self.createTables()
    
    def __del__(self):
        self.conn.close()
    
    def createTables(self):
        query = "CREATE TABLE IF NOT EXISTS PLAYERS (player TEXT, rating INT, sex TEXT, title TEXT)"
        self.cursor.execute(query)
        self.conn.commit()

    def selectAllPlayers(self):
        query = "SELECT * FROM PLAYERS"
        try:
            self.cursor.execute(query)
        except Exception as e:
            print(e)
            exit(1)
        return self.cursor.fetchall()

    def insertPlayer(self, player):
        player = tuple(player)
        query = "INSERT INTO PLAYERS VALUES (\"%s\",\"%s\",\"%s\",\"%s\")" % player
        try:
            self.cursor.execute(query)
            self.conn.commit()
        except Exception as e:
            print(e)
            exit(1)

if __name__ == "__main__":
    # Testes
    d = Database("teste.db")
    p = ["Teste2", 1911, "Outro", "Fem"]
    d.insertPlayer(p)
    print(d.selectAllPlayers())
    # print(d.selectAllPlayers())
