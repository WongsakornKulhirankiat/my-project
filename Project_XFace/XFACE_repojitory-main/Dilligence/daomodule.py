import sqlite3
from datetime import datetime

class StartsettingDAO():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("DiligenceDB.db")
        self.cursor = self.conn.cursor()

    def setTimezone(self, timezone):
        try:
            #self.cursor.execute("insert into DB名(カラム名) values('{}')".format(timezone))
            pass
        except Exception as e:
            print(e)

    def setLanguage(self, language):
        try:
            #self.cursor.execute("insert into DB名(カラム名) values('{}')".format(language))
            pass
        except Exception as e:
            print(e)  
    
    def insertUserMst(self, userid, username, companyname, password, picture, admin):
        try:
            self.cursor.execute("insert into UserMst(UserID, UserName, CompanyName, Pass, FacePhoto, Authority) values('{}','{}','{}','{}','{}','{}')"\
                    .format(userid, username, companyname, password, picture, admin))
            self.conn.commit()

        except Exception as e:
            print(e)

    def insertAdministrator(self, editorid, adminpassword, createdate):
        try:
            self.cursor.execute("insert into Administrator(Editor, AdminPass, CreateDate) values('{}','{}','{}')"\
                    .format(editorid, adminpassword, createdate))
            self.conn.commit()

        except Exception as e:
            print(e)



class UseradminopDAO():
    def __init__(self) -> None:
        self.conn = sqlite3.connect("DiligenceDB.db")
        self.cursor = self.conn.cursor()

    def getUserIDLoginpassword(self):
        try:
            self.cursor.execute("select UserID, Pass from UserMst")
            result = self.cursor.fetchall()
            logindict = {}
            logindict = {record[0]:record[1] for record in result}
            return logindict
        except Exception as e:
            print(e)

    def getLoginUserinfo(self, userid, password):
        try:
            print(type(userid), type(password))
            userinfolist = []
            self.cursor.execute("select * from UserMst where UserID = '{}' and Pass = '{}'".format(userid, password))
            userinfolist = self.cursor.fetchone()
            return userinfolist
        except Exception as e:
            print(e)
        
    def getEntryLeavingtime(self, userid, yearmonth, day):
        try:
            print(self, yearmonth, day)
            self.cursor.execute("select EntryTime, LeavingTime from History where UserID = '{}' and YearAndMonth = '{}' and Day = '{}'".format(userid, yearmonth, day))
            entryleavingtime = self.cursor.fetchall()
            return entryleavingtime
        except Exception as e:
            print(e)

    def updateUserCompanyname(self, name_before, name_after, userid, flag):
        if flag == "user":
            self.cursor.execute("update UserMst set UserName = '{}' where UserID = '{}' and UserName = '{}'".format(name_after, userid, name_before))
            self.conn.commit()
        else:
            self.cursor.execute("update UserMst set CompanyName = '{}' where UserID = '{}' and CompanyName = '{}'".format(name_after, userid, name_before))
            self.conn.commit()

    
    def updateUserPassword(self, changepassword, userid, username, companyname):
        try:
            print(self, changepassword, userid)
            self.cursor.execute("update UserMst set Pass = '{}' where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(changepassword, userid, username, companyname))
            self.conn.commit()
        except Exception as e:
            print(e)

    def updateAdminPassword(self, changeadminpassword, editor):
        try:
            print(self, changeadminpassword, editor)
            self.cursor.execute("update Administrator set AdminPass = '{}' where Editor = '{}'".format(changeadminpassword, editor))
            self.conn.commit()
        except Exception as e:
            print(e)

    def updatePhoto(self, userid, username, password, picture):
        try:
            self.cursor.execute("update UserMst set FacePhoto = '{}' where UserID = '{}' and UserName = '{}' and Pass = '{}'".format(picture, userid, username, password))
            self.conn.commit()
        except Exception as e:
            print(e)

    def getAdminLoginpassword(self, editor):
        try:
            self.cursor.execute("select AdminPass from Administrator where Editor = '{}'".format(editor))
            adminpassword = self.cursor.fetchone()
            return adminpassword
        except Exception as e:
            print(e)

    def getAdminEntryLeavingtime(self, yearmonth, day):
        try:
            print(type(yearmonth), type(day))
            self.cursor.execute("select EntryTime, LeavingTime, UserMst.UserName, UserMst.CompanyName from History inner join UserMst on History.UserID = UserMst.UserID where YearAndMonth = '{}' and Day = '{}'".format(yearmonth, day))
            entryleavingtime = self.cursor.fetchall()
            return entryleavingtime
        except Exception as e:
            print(e)

    def getAllUserinfo(self):
        try:
            userinfolist = []
            self.cursor.execute("select * from UserMst order by UserID asc")
            userinfolist = self.cursor.fetchall()
            return userinfolist
        except Exception as e:
            print(e)

    def getAllUserName(self):
        try:
            usernamelist = []
            combo_usernamelist = []
            self.cursor.execute("select UserName from UserMst order by UserID asc")
            usernamelist = self.cursor.fetchall()
            print("check1:", usernamelist)
            for username in usernamelist:
                print(username)
                combo_usernamelist.append(username[0])
            print(combo_usernamelist)
            return combo_usernamelist
        except Exception as e:
            print(e)

    def getAllCompanyName(self):
        try:
            companynamelist = []
            combo_companynamelist = []
            self.cursor.execute("select CompanyName from UserMst order by UserID asc")
            companynamelist = self.cursor.fetchall()
            for companyname in companynamelist:
                combo_companynamelist.append(companyname[0])
            return combo_companynamelist
        except Exception as e:
            print(e)

    def getLeftoverAdminUser(self):
        try:
            self.cursor.execute("select count(*) from Administrator")
            leftoveradminuser = self.cursor.fetchone()
            return leftoveradminuser
        except Exception as e:
            print(e)

    def updateAdminAuthority(self, grantAdminAuthority_save, userid, username, companyname, authority):
        try:
            if grantAdminAuthority_save == "no":
                self.cursor.execute("update UserMst set Authority = '{}' where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(authority, userid, username, companyname))
                self.conn.commit()
            else:
                date = datetime.now()
                createdate = date.strftime('%Y%m%d%H%M')
                self.cursor.execute("update UserMst set Authority = '{}' where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(authority, userid, username, companyname))
                self.cursor.execute("update Administrator set AdminPass = '{}' , CreateDate = {} where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(grantAdminAuthority_save, createdate, username, companyname))
                self.conn.commit()            
        except Exception as e:
            print(e)

    def updateResetpassword(self, userid, username, companyname):
        try:
            print(userid, username, companyname)
            self.cursor.execute("update UserMst set Pass = '0000' where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(userid, username, companyname))
            self.conn.commit()       
        except Exception as e:
            print(e)

    def deleteUserinfo(self, userid, username, companyname):
        try:
            print(userid, username, companyname)
            #self.cursor.execute("update UserMst set Pass = '0000' where UserID = '{}' and UserName = '{}' and CompanyName = '{}'".format(userid, username, companyname))
            #self.conn.commit()       
        except Exception as e:
            print(e)

    def createUserinfo(self, createusername, createcompanyname, createpassword, picture):
        try:
            self.cursor.execute("insert into UserMst(UserName, Companyname, Pass, FacePhoto) values('{}','{}','{}','{}')".format(createusername, createcompanyname, createpassword, picture))
            self.conn.commit()
        except Exception as e:
            print(e)
 