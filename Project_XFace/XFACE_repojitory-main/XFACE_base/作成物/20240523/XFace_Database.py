import sqlite3
from datetime import datetime, timedelta
import os

current_directory = os.getcwd()  # 現在のディレクトリを取得
db_path = 'DB/database.db'
userRegPhoto_directory = os.path.join(current_directory, db_path)# ユーザー登録で画像を一時保存するディレクトリ

def create_tables():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()

    c.execute('''CREATE TABLE userinfo
                 (UserID INTEGER PRIMARY KEY,
                  UserName TEXT NOT NULL,
                  Password TEXT NOT NULL,
                  DepartmentID INTEGER NOT NULL,
                  AdminFlag INTEGER NOT NULL,
                  FacePhoto BLOB)''')

    c.execute('''CREATE TABLE AttendanceRecord
                 (UserID INTEGER NOT NULL,
                  YearMonth INTEGER NOT NULL,
                  Date INTEGER NOT NULL,
                  WorkStartTime TEXT,
                  WorkEndTime TEXT,
                  WorkingTime REAL,
                  Memo TEXT,
                  FOREIGN KEY(UserID) REFERENCES userinfo(UserID))''')

    c.execute('''CREATE TABLE AccessRecord
                 (UserID INTEGER NOT NULL,
                  YearMonth INTEGER NOT NULL,
                  Date INTEGER NOT NULL,
                  EnteringTime TEXT,
                  FOREIGN KEY(UserID) REFERENCES userinfo(UserID))''')

    c.execute('''CREATE TABLE DepartmentMaster
                 (DepartmentID INTEGER PRIMARY KEY,
                  DepartmentName TEXT NOT NULL,
                  WorkStartTime TEXT NOT NULL,
                  WorkEndTime TEXT NOT NULL,
                  RestTime INTEGER NOT NULL,
                  OverTime INTEGER NOT NULL)''')

    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()


    users_data = [
        ('100000', 'aaaa', '111111', '1', 1, ''),
        ('100001', 'bbbb', '111111', '1', 0, ''),
        ('100002', 'cccc', '111111', '2', 0, ''),
        ('100003', 'dddd', '111111', '2', 0, ''),
        ('100004', 'eeee', '111111', '3', 0, ''),
        ('100005', 'ffff', '111111', '3', 0, ''),
        ('100006', 'gggg', '111111', '4', 0, ''),
        ('100007', 'hhhh', '111111', '4', 0, ''),
        ('100008', 'iiii', '111111', '5', 0, ''),
        ('100009', 'jjjj', '111111', '5', 0, '')
    ]


    c.executemany('INSERT INTO userinfo (UserID, UserName, Password, DepartmentID, AdminFlag, FacePhoto) VALUES (?, ?, ?, ?, ?, ?)', users_data)
    conn.commit()

   
    today = datetime.now()
    for user in users_data:
        user_id = user[0]
        data = [
            (user_id, today.strftime('%Y%m'), (today - timedelta(days=3)).strftime('%d'), '09:00', '18:00', '8', ''),
            (user_id, today.strftime('%Y%m'), (today - timedelta(days=2)).strftime('%d'), '09:00', '18:30', '8.5', ''),
            (user_id, today.strftime('%Y%m'), (today - timedelta(days=1)).strftime('%d'), '', '', '', '有給休暇取得')
        ]
        
        c.executemany('INSERT INTO AttendanceRecord (UserID, YearMonth, Date, WorkStartTime, WorkEndTime, WorkingTime, Memo) VALUES (?, ?, ?, ?, ?, ?, ?)', data)
    
    conn.commit()
    conn.close()

def insert_department_data():
    conn = sqlite3.connect(userRegPhoto_directory)
    c = conn.cursor()

    departments_data = [
        (1, 'IT', '09:00', '18:00', 1, 0),
        (2, 'HR', '09:00', '18:00', 1, 0),
        (3, 'Finance', '09:00', '18:00', 1, 0),
        (4, 'Marketing', '09:00', '18:00', 1, 0),
        (5, 'Operations', '09:00', '18:00', 1, 0),
        (6, 'Sales', '09:00', '18:00', 1, 0)
    ]

    c.executemany('INSERT INTO DepartmentMaster (DepartmentID, DepartmentName, WorkStartTime, WorkEndTime, RestTime, OverTime) VALUES (?, ?, ?, ?, ?, ?)', departments_data)
    conn.commit()
    conn.close()

create_tables()
insert_data()
insert_department_data()
