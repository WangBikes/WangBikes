import sqlite3
# Database
class DatabaseLogic():
    # Constructor
    def __init__(self, database):
        # Database
        self.database = database
        
        # Connection and cursor
        self.con = sqlite3.connect(self.database)
        self.cursor = self.con.cursor()
    
    def checkUser(self, username):
      """this function checks that the username
      exists in the database"""
      
      
      #cur.execute("FROM ")

    def addUser(self, username, password):
        pass
        

    def deleteUser(self, username):
        pass

    def getPassword(self, username):
        pass
    
    def updateUsername(self, username, newUsername):
      pass
    
    def updatePassword(self, username, newPassword):
        pass
    
    def addProduct(self, productName, productID, productPrice):
      pass

    def deleteProduct(self, productID):
      pass
    
    def getProductFromName(self, productName):
      pass
    

    def createTables(self):
      """this function creates tables """
      with sqlite3.connect('database.db') as dbase:
        cur = dbase.cursor()    
         
        userQuery = '''CREATE TABLE IF NOT EXISTS users(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        isAdmin BOOl
        )'''

        bikeQuery = '''CREATE TABLE IF NOT EXISTS bikes(
        bikeID INTEGER PRIMARY KEY AUTOINCREMENT,
        bikeName TEXT NOT NULL,
        price INTEGER,
        model TEXT NOT NULL
        )'''
        
        cardQuery = '''CREATE TABLE IF NOT EXISTS cards(
        cardID INTEGER PRIMARY KEY AUTOINCREMENT,
        type TEXT,
        expireDate INTEGER
        )'''
        
        saleQuery = '''CREATE TABLE IF NOT EXISTS sales(
        saleID INTEGER PRIMARY KEY AUTOINCREMENT,
        userID INTEGER,
        FOREIGN KEY (userID)
        REFERENCES users (ID),
        bikeID INTEGER,
        FOREIGN KEY (bikeID)
        REFERENCES bikes (bikeID),
        cardID INTEGER,
        FOREIGN KEY (cardID)
        REFERENCES cards (cardID),

      
        )'''

      cur.execute()