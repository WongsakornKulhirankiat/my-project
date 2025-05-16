import sqlite3
from datetime import datetime

class SchoolbusDAO():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("SchoolbusDB.db")
        self.cursor = self.conn.cursor()
    
    def getAdminInfo_Pass(self):
        try:
            self.cursor.execute("select Password from AdminInfo")
            loginpass = self.cursor.fetchall()
            return loginpass
        except Exception as e:
            print(e)
    
    def updateAdminInfo_Pass(self,newpass,oldpass):
        try:
            self.cursor.execute("update AdminInfo set Password = '{}' where Password = '{}'".format(newpass,oldpass))
            self.conn.commit() 
        except Exception as e:
            print(e)

    def getStudentInfo_studentid(self):
        try:
            self.cursor.execute("select max(StudentID) from StudentInfo")
            maxstudentid = self.cursor.fetchone()
            maxstudentid_plus = maxstudentid +1
            return maxstudentid_plus
        except Exception as e:
            print(e)
    
    def createStudentInfo_studentinfo(self,name,school,photo):
        try:
            self.cursor.execute("insert into StudentInfo(Name, School, FacePhoto) values ('{}','{}','{}')".format(name,school,photo))
            self.conn.commit() 
        except Exception as e:
            print(e)

    def getStudentInfo_All(self):
        try:
            studentinfolist = []
            self.cursor.execute("select * from StudentInfo") ###group by
            studentinfolist = self.cursor.fetchall()
            return studentinfolist
        except Exception as e:
            print(e)  
    
    def getStudentInfo_searchinfo(self,name,school):
        try:
            searchstudentlist = []
            self.cursor.execute("select * from StudentInfo where Name = {} and School = {}".format(name,school)) ###group by
            searchstudentlist = self.cursor.fetchall()
            return searchstudentlist
        except Exception as e:
            print(e)

    def deleteStudentInfo_studentinfo(self):
        try:
            pass
        except Exception as e:
            print(e)

    def updateStudentInfo_studentinfo(self, newname,newschool,newphoto,oldname,oldschool,studentid):
        try:
            self.cursor.execute("update StudentInfo set Name = '{}'and  School = '{}' and FacePhoto = {} where Name = '{}'and  School = '{}' and StudentID = {}".format(newname,newschool,newphoto, oldname,oldschool,studentid))
            self.conn.commit() 
        except Exception as e:
            print(e)

    def getStudentInfo_ridecheck(self, school):
        try:
            studentinfolist = []
            self.cursor.execute("select * from StudentInfo where School = '{}") ###group by
            studentinfolist = self.cursor.fetchall()
            return studentinfolist
        except Exception as e:
            print(e)    
