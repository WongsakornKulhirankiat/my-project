import sqlite3

class CheckDBtable():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("DiligenceDB.db")
        self.cursor = self.conn.cursor()
    
    def checkDiligenceDB(self):
        self.cursor.execute("select name from sqlite_master where type='table'")
        result = self.cursor.fetchall()
        print("checkDB", result)

    def checkDiligenceDB_UserMst(self):
        self.cursor.execute("select * from UserMst")
        result = self.cursor.fetchall()
        print("checktUserMsttable", result)

    def checkDiligenceDB_Administrator(self):
        self.cursor.execute("select * from Administrator")
        result = self.cursor.fetchall()
        print("checktAdministratortable", result)

    def checkDiligenceDB_History(self):
        self.cursor.execute("select * from History")
        result = self.cursor.fetchall()
        print("checktHistorytable", result)


createmodule = CheckDBtable()
#createmodule.checkDiligenceDB()
#createmodule.checkDiligenceDB_UserMst()
#createmodule.checkDiligenceDB_Administrator()
createmodule.checkDiligenceDB_History()