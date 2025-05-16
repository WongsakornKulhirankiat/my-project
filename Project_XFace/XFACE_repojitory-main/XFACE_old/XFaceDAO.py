import sqlite3
import pymssql
#import pymysql
import os
import shutil
import time
import traceback
from datetime import datetime

SHAREDVARS = None

class XFaceServerDAO():
    def __init__(self, value):
        #self.conn = pymssql.connect(server = '1.10.174.85', user = 'sa', password = 'P@ssw0rd', database = 'XFACE')    #ExcellenceSiam External network connection
        #self.conn = pymssql.connect(server = '192.168.1.222', user = 'sa', password = 'P@ssw0rd', database = 'XFACE')  #ExcellenceSiam Internal network connection
        #self.conn = pymssql.connect(server = '192.168.1.36', user = 'admin', password = 'admin', database = 'XFACE')    #Gusts'Desktop Internal network connection
        self.conn = pymssql.connect(server = value[0], user = value[1], password = value[2], database = value[3])
        #conn = pymysql.connect(host="localhost" , user="root" , password="password" , database="database_name" ,)
        #self.conn = pymysql.connect(host=value[0] , user=value[1] , password=value[2] , db=value[3])
       # self.conn = pymysql.connect(host='192.168.1.222' , user='sa' , password='P@ssw0rd' , database='XFACE')
        self.cursor = self.conn.cursor()

    def deleteEmployee(self, name):
        try:
            self.cursor.execute("delete from EMPLOYEE where NAME = '{}'".format(name))
            SHAREDVARS['XFaceLogging'].s_employee('DELETE', name)
            self.cursor.execute("delete from FINGERPRINT where NAME = '{}'".format(name))
            SHAREDVARS['XFaceLogging'].s_fingerprint('DELETE', name)
            # keep image on server the way it was
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:S01', e)
            SHAREDVARS['XFaceLogging'].system('ERROR:S01', traceback.format_exc())

    def insertEmployee(self, name, password, department, role):
        try:
            # image to insert must be placed in pic/name/name.png in order to call this method.
            if imageExists(name):
                SHAREDVARS['XFaceAPI'].post(name)
                SHAREDVARS['XFaceLogging'].s_employee('INSERT', "API save image: {} on server".format(name))

            # fingerprint to insert must be in localDB in order to execute this method.
            localDAO.cursor.execute("select FINGERPRINT_ID, FINGERPRINT from FINGERPRINT where NAME = '{}'".format(name))
            fingerprints = localDAO.cursor.fetchall()
            try:
                for fingerprint in fingerprints:
                    # Do not overwrite existing ID on server
                    self.cursor.execute("select FINGERPRINT_ID from FINGERPRINT where FINGERPRINT_ID = '{}'".format(fingerprint[0]))
                    result = self.cursor.fetchone()
                    if result is None:
                        self.cursor.execute("insert into FINGERPRINT(FINGERPRINT_ID, NAME, FINGERPRINT, CREATE_TIME) values('{}','{}','{}','{}')"\
                                        .format(fingerprint[0], name, fingerprint[1], time.strftime('%Y-%m-%d %H:%M:%S')))
                        SHAREDVARS['XFaceLogging'].s_fingerprint('INSERT', 'fingerprint ID: {}'.format(fingerprint[0]))
            except Exception as e:
                SHAREDVARS['XFaceLogging'].system('ERROR:S02F', e)
                SHAREDVARS['XFaceLogging'].system('ERROR:S02F', traceback.format_exc())

            # lastly insert to EMPLOYEE
            self.cursor.execute("select NAME from EMPLOYEE where NAME = '{}'".format(name))
            result = self.cursor.fetchone()
            if result is None:
                self.cursor.execute("insert into EMPLOYEE(NAME, PASSWORD, DEPARTMENT, ROLE, CREATE_TIME) values('{}','{}','{}','{}','{}')"\
                            .format(name, password, department, role, time.strftime('%Y-%m-%d %H:%M:%S')))
                SHAREDVARS['XFaceLogging'].s_employee('INSERT', name)
                
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:S02', e)
            SHAREDVARS['XFaceLogging'].system('ERROR:S02', traceback.format_exc())

class XFaceLocalDAO():
    def __init__(self):
        self.conn = sqlite3.connect("XFaceDB.db")
        self.cursor = self.conn.cursor()

    def getServerDAO(self):
        return self.getSystemValue('SERVER_DB').split('|')

    def getSystemValue(self, code):
        self.cursor.execute("select VALUE from SYSTEM where CODE = '{}'".format(code))
        fetch = self.cursor.fetchone()
        if fetch is None: return None
        else: return fetch[0]

    def setSystemValue(self, code, value):
        try:
            sql = "update SYSTEM set VALUE = '{}' where CODE = '{}'".format(value, code)
            self.cursor.execute(sql)
            self.conn.commit()
            SHAREDVARS['XFaceLogging'].system('INFO', sql)
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:L00', 'unable to set system value with code {} {}'.format(code, e))
            SHAREDVARS['XFaceLogging'].system('ERROR:L00', traceback.format_exc())


    """def getSystemCamera(self):
        self.cursor.execute("select * from SYSTEM")
        fetch = self.cursor.fetchall()
        print(fetch,"fujiwaraCAMERAcheck11")
        if fetch is None: return None
        else: return fetch[0]


    def setSystemCamera(self):
        try:
            sql = "insert into SYSTEM(CODE, VALUE) values('FINGERPRINT', '0')"
            self.cursor.execute(sql)
            self.conn.commit()
            SHAREDVARS['XFaceLogging'].system('INFO', sql)
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:L00', 'unable to set system value with code fujiwaraerror')
            SHAREDVARS['XFaceLogging'].system('ERROR:L00', traceback.format_exc())"""                                #2023/11/10 fujiwara tuika

    def deleteEmployee(self, name):
        try:
            self.cursor.execute("delete from EMPLOYEE where NAME = '{}'".format(name))
            SHAREDVARS['XFaceLogging'].employee('DELETE', name)
            self.cursor.execute("delete from FINGERPRINT where NAME = '{}'".format(name))
            SHAREDVARS['XFaceLogging'].fingerprint('DELETE', name)
            pic_path = 'pic/'+name
            if os.path.exists(pic_path):
                shutil.rmtree(pic_path)
                SHAREDVARS['XFaceLogging'].employee('DELETE', "delete image {}".format(pic_path))
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:L01', e)
            SHAREDVARS['XFaceLogging'].system('ERROR:L01', traceback.format_exc())

    def insertEmployee(self, name, password, department, role):
        try:
            self.cursor.execute("insert into EMPLOYEE(NAME, PASSWORD, DEPARTMENT, ROLE,  CREATE_TIME) values('{}','{}','{}','{}','{}')"\
                    .format(name, password, department, role,  time.strftime('%Y-%m-%d %H:%M:%S')))
            self.conn.commit()                                                                                                              #2023/11/2 fujiwara tuika
            if os.path.exists('pic/{}/{}.png'.format(name, name)):
                SHAREDVARS['XFaceEncodingData'].PickleData.addFace(name)
            SHAREDVARS['XFaceLogging'].employee('INSERT', name)
        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:L02', e)
            SHAREDVARS['XFaceLogging'].system('ERROR:L02', traceback.format_exc())

    def insertFingerprint(self, name, eigens):
        # 1. get min id from localDB for inserting.
        # 2. insert(id, name, eigen) to localDB.
        # 3. insert(id, name, eigen) to Capacitive fingerprint.
        try:
            for i in range(len(eigens)):
                self.cursor.execute("SELECT min(FINGERPRINT_ID+1) R \
                                    FROM FINGERPRINT WHERE FINGERPRINT_ID+1 NOT IN \
                                    (SELECT FINGERPRINT_ID FROM FINGERPRINT)")
                id = self.cursor.fetchone()
                if id is None: id = 1
                else: id = id[0]

                SHAREDVARS['XFaceLogging'].system("FINGER id={} name={}".format(str(id), name), eigens[i])
                r = SHAREDVARS['XFaceCapacitiveFP'].SetEigenvalues(id, eigens[i])
                if r != SHAREDVARS['XFaceCapacitiveFP'].ACK_SUCCESS:
                    raise Exception("Failed SetEigenvalues id = "+str(id))

                self.cursor.execute("insert into FINGERPRINT(FINGERPRINT_ID, NAME, FINGERPRINT, CREATE_TIME) values('{}','{}','{}','{}')"\
                            .format(id, name, eigens[i], time.strftime('%Y-%m-%d %H:%M:%S')))
                #self.conn.commit()   #2024/01/09 fujiwara tuika
                SHAREDVARS['XFaceLogging'].fingerprint('INSERT', 'fingerprint id: {}'.format(str(id)))

        except Exception as e:
            SHAREDVARS['XFaceLogging'].system('ERROR:L03', e)
            SHAREDVARS['XFaceLogging'].system('ERROR:L03', traceback.format_exc())
            #SHAREDVARS['XFaceLogging'].system('ERROR:L03', e)

def copyFromServerToLocal(name):
    try:
        serverDAO.cursor.execute("select PASSWORD, DEPARTMENT, ROLE from EMPLOYEE where NAME = '{}'".format(name))
        employee = serverDAO.cursor.fetchone()
        localDAO.insertEmployee(name, employee[0], employee[1], employee[2])

        serverDAO.cursor.execute("select FINGERPRINT_ID, FINGERPRINT from FINGERPRINT where NAME = '{}'".format(name))
        fingerprints = serverDAO.cursor.fetchall()
        for fingerprint in fingerprints:
            # Server first (overwrite existing on local and fp)
            r = SHAREDVARS['XFaceCapacitiveFP'].SetEigenvalues(fingerprint[0], fingerprint[1])
            if r != SHAREDVARS['XFaceCapacitiveFP'].ACK_SUCCESS:
                raise Exception("Failed SetEigenvalues id = "+str(id))
                
        SHAREDVARS['XFaceLogging'].employee('SYNC', name)

    except Exception as e:
        SHAREDVARS['XFaceLogging'].system('ERROR:SYNC01', e)
        SHAREDVARS['XFaceLogging'].system('ERROR:SYNC01', traceback.format_exc())

def copyFromLocalToServer(name):
    try:
        localDAO.cursor.execute("select PASSWORD, DEPARTMENT, ROLE from EMPLOYEE where NAME = '{}'".format(name))
        employee = localDAO.cursor.fetchone()
        serverDAO.insertEmployee(name, employee[0], employee[1], employee[2])
        SHAREDVARS['XFaceLogging'].employee('SYNC', name)
    except Exception as e:
        SHAREDVARS['XFaceLogging'].system('ERROR:SYNC02', e)
        SHAREDVARS['XFaceLogging'].system('ERROR:SYNC02', traceback.format_exc())

def imageExists(name):
    return os.path.exists('pic/{}/{}.jpg'.format(name, name)) or os.path.exists('pic/{}/{}.png'.format(name, name))

def initServerDAO():
    try:
        global serverDAO
        print(11111111111111111)
        serverDAO = XFaceServerDAO(localDAO.getServerDAO())
        print(2222222222222222222)
        SHAREDVARS['SERVER'] = True
        print(3333333333333333)
    except Exception as e:
        print(e)
        serverDAO = None
        SHAREDVARS['SERVER'] = False
        SHAREDVARS['XFaceLogging'].system("[NANDE  ]", "Failed to connect XFaceServerDAO.")  #2023/11/10 fujiwara initialize XFaceCapacitiveFP -> connect XFaceServerDAO
        SHAREDVARS['XFaceLogging'].system('ERROR:DAO', e)
        SHAREDVARS['XFaceLogging'].system('ERROR:DAO', traceback.format_exc())

localDAO = XFaceLocalDAO()
serverDAO = None
