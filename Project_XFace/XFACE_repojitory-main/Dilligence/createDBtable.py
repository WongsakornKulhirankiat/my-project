import sqlite3

class CreateDBtable():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("DiligenceDB.db")
        self.cursor = self.conn.cursor()
    
    def createUserMst(self):
        self.cursor.execute("create table UserMst(UserID INTEGER PRIMARY KEY, UserName TEXT NOT NULL, CompanyName TEXT NOT NULL, Pass INTEGER NOT NULL, FacePhoto BLOB NOT NULL, Authority TEXT NOT NULL)")
        self.conn.commit()

    def createAdministrator(self):
        self.cursor.execute("create table Administrator(Editor TEXT, AdminPass TEXT NOT NULL, CreateDate INTEGER NOT NULL)")
        self.conn.commit()

    def createHistory(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS History (UserID TEXT, YearAndMonth TEXT, Day TEXT, EntryTime TEXT, LeavingTime TEXT)")              
        self.conn.commit()


createmodule = CreateDBtable()
#createmodule.createUserMst()    #2024/02/28 complete
#createmodule.createAdministrator()   #2024/02/28 complete
#createmodule.createHistory()   #2024/03/01 complete



"""class DropDBtable():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("DiligenceDB.db")
        self.cursor = self.conn.cursor()

    def dropDBTable(self, tablename):
        self.cursor.execute("DROP TABLE {}".format(tablename))
        self.conn.commit()

tablename = "UserMst"
dropemodule = DropDBtable()
dropemodule.dropDBTable()"""