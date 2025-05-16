import sqlite3
#import pymysql
import time
from datetime import datetime

class XFaceCreateDB():
    def DBconnect(self):
        try:
            conn = sqlite3.connect("DB/XFACEDB.db")
            return conn
        except Exception as e:
            print(e)
    
    def DBconnect_close(self,conn):
        try:
            conn.close()
        except Exception as e:
            print(e)
    
    def createUserInfo(self):
        try:
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("create table IF NOT EXISTS UserInfo (UserID INTEGER PRIMARY KEY AUTOINCREMENT, UserName TEXT NOT NULL, Password INTEGER NOT NULL, FacePhoto BLOB NOT NULL)")
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def createAttendanceRecord_userid(self,userid):
        try:
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("create table IF NOT EXISTS AttendanceRecord_{} (YearMonth INTEGER NOT NULL, Date INTEGER NOT NULL, StartingworkTime TEXT NOT NULL, EndingworkTime TEXT, WorkingTime REAL , Memo TEXT)".format(userid))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def createAccessRecord_userid(self,userid):
        try:
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("create table IF NOT EXISTS AccessRecord_{} (YearMonth INTEGER NOT NULL, Date INTEGER NOT NULL, EnteringTime TEXT, ExitingTime TEXT, AccessID INTEGER NOT NULL)".format(userid))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def createWorkingMaster(self):
        try:
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("create table IF NOT EXISTS WorkingMaster (StartingworkTimeMaster TEXT NOT NULL, EndingworkTimeMaster TEXT NOT NULL, RestTimeMaster INTEGER NOT NULL, OverTimeMaster INTEGER NOT NULL)")
            conn.commit()
            cursor.execute("insert into WorkingMaster (StartingworkTimeMaster, EndingworkTimeMaster, RestTimeMaster) values('8:00', '17:00', 1, 30)")
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)


class XFaceDAO():
    def DBconnect(self):
        try:
            conn = sqlite3.connect("DB/XFACEDB.db")
            return conn
        except Exception as e:
            print(e)
    
    def DBconnect_close(self,conn):
        try:
            conn.close()
        except Exception as e:
            print(e)

    def getWorkingMaster(self):
        try:
            masterlist = []
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select StartingworkTimeMaster, EndingworkTimeMaster, RestTimeMaster from WorkingMaster")
            masterlist = cursor.fetchall()
            self.DBconnect_close(conn)
            return masterlist
        except Exception as e:
            print(e)

    def getUserInfo(self):
        try:
            userinfolist = []
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select UserID, UserName, Password from UserInfo order by UserID")
            userinfolist = cursor.fetchall()
            self.DBconnect_close(conn)
            return userinfolist
        except Exception as e:
            print(e)
    
    def getUserInfo_userlist(self):
        try:
            userlist = []
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select UserID, UserName from UserInfo order by UserID")
            userlist = cursor.fetchall()
            self.DBconnect_close(conn)
            return userlist
        except Exception as e:
            print(e)

    def getAttendanceRecord_recordlist(self,userid,yearmonth):
        try:
            recordlist = []
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select Date, StartingworkTime, EndingworkTime, WorkingTime, Memo from AttendanceRecord_{} where YearMonth = {} order by Date".format(userid,yearmonth))
            recordlist = cursor.fetchall()
            self.DBconnect_close(conn)
            return recordlist
        except Exception as e:
            print(e)

    def updateWorkingMaster(self,startingtime,endingtime,resttime):
        try:
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("update WorkingMaster set StartingworkTimeMaster = '{}' , EndingworkTimeMaster = '{}' , RestTimeMaster = {}".format(startingtime,endingtime,resttime))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def getAccessRecord_accessid(self,userid):
        try:
            accessid = ""
            date = int(time.strftime("%d"))
            yearmonth = str(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select COUNT(AccessID) from AccessRecord_{} where YearMonth = {} and Date = {}".format(userid,yearmonth,date))
            accessid = cursor.fetchone()
            self.DBconnect_close(conn)
            return accessid[0]
        except Exception as e:
            print(e)

    def insertAttendanceRecord_StartingworkTime(self,userid,starttime):
        try:
            date = int(time.strftime("%d"))
            yearmonth = int(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("insert into AttendanceRecord_{} (YearMonth, Date, StartingworkTime) values({}, {}, '{}')".format(userid,yearmonth,date,starttime))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)
        
    def insertAccessRecord_Enter(self,userid,recognitiontime,accessid_plus1):
        try:
            date = int(time.strftime("%d"))
            yearmonth = int(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("insert into AccessRecord_{} (YearMonth, Date, EnteringTime, AccessID) values({}, {}, '{}', {})".format(userid,yearmonth,date,recognitiontime,accessid_plus1))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def insertAccessRecord_Exit(self,userid,recognitiontime,accessid_plus1):
        try:
            date = int(time.strftime("%d"))
            yearmonth = int(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("insert into AccessRecord_{} (YearMonth, Date, ExitingTime, AccessID) values({}, {}, '{}', {})".format(userid,yearmonth,date,recognitiontime,accessid_plus1))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)

    def getAttendanceRecord_StartingworkTime(self,userid):
        try:
            startingworktime = ""
            date = int(time.strftime("%d"))
            yearmonth = str(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("select StartingworkTime from AttendanceRecord_{} where YearMonth = {} and Date = {}".format(userid,yearmonth,date))
            startingworktime = cursor.fetchone()
            self.DBconnect_close(conn)
            return startingworktime[0]
        except Exception as e:
            print(e)

    def updateAttendanceRecord_workingtime(self,userid,exittime,workingtime):
        try:
            date = int(time.strftime("%d"))
            yearmonth = str(time.strftime("%Y%m"))
            conn = self.DBconnect()
            cursor = conn.cursor()
            cursor.execute("update AttendanceRecord_{} set EndingworkTime = '{}' , WorkingTime = {} where YearMonth = {} and Date = {} ".format(userid,exittime,workingtime,yearmonth,date))
            conn.commit()
            self.DBconnect_close(conn)
        except Exception as e:
            print(e)
        
if __name__ == '__main__':
    createdb = XFaceCreateDB()
    userid_sample = 100000
    createdb.createUserInfo()   #04/25 complete
    createdb.createAttendanceRecord_userid(userid_sample)   #userid -> userid_sample = 100000   04/25 complete
    createdb.createAccessRecord_userid(userid_sample)   #userid -> userid_sample = 100000   4/25 complete
    createdb.createWorkingMaster()   #04/25 complete

