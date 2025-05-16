import sqlite3
import os
from datetime import datetime, timedelta
import random

#ローカルテスト用DB作成
def create_table():
    database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    
    conn = sqlite3.connect(database_path)
    
    cursor = conn.cursor()
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS History (
                UserID TEXT,
                YearAndMonth TEXT,
                Day TEXT,
                EntryTime TEXT,
                LeavingTime TEXT
                )''')
        
    conn.commit()
    
    conn.close()
    

def insert_data():
    
    # database_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'database.db')
    
    conn = sqlite3.connect('DiligenceDB.db')
    
    cursor = conn.cursor()
    
    user_ids = [f"{i:04d}" for i in range(3, 11)]
    
    start_date = datetime(2024, 2, 25)
    end_date = datetime(2024, 3, 5)
    dates = [start_date + timedelta(days=x) for x in range((end_date - start_date).days + 1)]
    holidays = [datetime(2024, 2, 25), datetime(2024, 3, 2), datetime(2024, 3, 3)]
    
    for date in dates:
        if date in holidays:
            continue
        num_users = random.randint(5, 6)
        selected_user_ids = random.sample(user_ids, num_users)
        for user_id in selected_user_ids:
            year_and_month = '{}{:02d}'.format(date.year, date.month)
            day = format(date.day, '02d')
            entry_time = '{:02d}{:02d}'.format(random.randint(8, 12), random.randint(0, 59))
            leaving_time = '{:02d}{:02d}'.format(random.randint(17, 23), random.randint(0, 59))
            
            cursor.execute('INSERT INTO History (UserID, YearAndMonth, Day, EntryTime, LeavingTime) VALUES (?, ?, ?, ?, ?)',
                           (user_id, year_and_month, day, entry_time, leaving_time))
    
    conn.commit()
    
    conn.close()


if __name__ == '__main__':
    # create_table()
    insert_data()