import os
import sqlite3

data = [
    {'userid': '0003', 'username': 'Michael Jackson', 'companyname': 'ABC Corporation', 'pass': '3842','facephoto': os.urandom(10), 'authority': 'true', 'adminpass': 'Abcd1234', 'createdate': '202310312245'},
    {'userid': '0004','username': 'Jessica Williams', 'companyname': 'XYZ Company', 'pass': '5698','facephoto': os.urandom(10), 'authority': 'false'},
    {'userid': '0005','username': 'John Smith', 'companyname': 'Smith & Co', 'pass': '9012','facephoto': os.urandom(10), 'authority': 'true', 'adminpass': 'Lp9qF5Kc', 'createdate': '202406181130'},
    {'userid': '0006','username': 'Linda Davis', 'companyname': 'Davis Enterprises', 'pass': '0753','facephoto': os.urandom(10), 'authority': 'false'},
    {'userid': '0007','username': 'David Garcia', 'companyname': 'Garcia Group', 'pass': '1987','facephoto': os.urandom(10), 'authority': 'true', 'adminpass': 'dX3sG6Wv', 'createdate': '202411240805'},
    {'userid': '0008','username': 'Sarah Johnson', 'companyname': 'Johnson Ltd.', 'pass': '5012','facephoto': os.urandom(10), 'authority': 'false'},
    {'userid': '0009','username': 'Robert Miller', 'companyname': 'Miller Holdings', 'pass': '6254','facephoto': os.urandom(10), 'authority': 'false'},
    {'userid': '0010','username': 'William Brown', 'companyname': 'Brown Industries', 'pass': '4901','facephoto': os.urandom(10), 'authority': 'false'}
]


#ローカルテスト用DB作成
def create_table():
    database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    
    conn = sqlite3.connect(database_path)
    
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS UserMst (
                UserID TEXT,
                UserName TEXT,
                CompanyName TEXT,
                Pass TEXT,
                FacePhoto BLOB,
                Authority TEXT
                )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS Administrator (
                Editor TEXT,
                AdminPass TEXT,
                CreateDate INTEGER
                )''')
        
    conn.commit()
    
    conn.close()
    
    
def insert_data():
    # database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    
    conn = sqlite3.connect('DiligenceDB.db')
    
    cursor = conn.cursor()
    
    for user in data:
        cursor.execute('INSERT INTO UserMst (UserID, UserName, CompanyName, Pass, FacePhoto, Authority) VALUES (?, ?, ?, ?, ?, ?)',
                       (user['userid'], user['username'], user['companyname'], user['pass'], user['facephoto'], user['authority']))
        
        if user['authority'] == 'true':
            cursor.execute('INSERT INTO Administrator (Editor, AdminPass, CreateDate) VALUES (?, ?, ?)',
                           (user['userid'], user['adminpass'], user['createdate']))
    
        
    conn.commit()
    
    conn.close()

if __name__ == '__main__':
    # create_table()
    insert_data()