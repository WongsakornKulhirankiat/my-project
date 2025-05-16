import sqlite3
from tkinter import messagebox
import datetime

db_path = 'database.db'

def check_user(user_id, password):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userinfo WHERE UserID=? AND Password=?", (user_id, password))
    user = cursor.fetchone()
    conn.close()
    return user

def check_admin(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userinfo WHERE UserID=?", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

def fetch_usernames():
        connection = sqlite3.connect(db_path)
        cursor = connection.cursor()
        cursor.execute("SELECT username FROM userinfo")  
        usernames = [row[0] for row in cursor.fetchall()]
        connection.close()
        return usernames

def fetch_username(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT UserName FROM userinfo WHERE UserID=?", (user_id,))
    username = cursor.fetchone()
    conn.close()
    return username

def fetch_user_info():
    """データベースからusers情報を取得"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT userinfo.UserID, userinfo.UserName, userinfo.Password, DepartmentMaster.DepartmentName, userinfo.AdminFlag FROM userinfo INNER JOIN DepartmentMaster ON userinfo.DepartmentID = DepartmentMaster.DepartmentID")
    user_info = cursor.fetchall()
    conn.close()
    return user_info

def fetch_userinfo_departmentname_by_username(user_name):
    """データベースからusers情報を取得"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT userinfo.UserName, userinfo.Password, DepartmentMaster.DepartmentName FROM userinfo INNER JOIN DepartmentMaster ON userinfo.DepartmentID = DepartmentMaster.DepartmentID WHERE userinfo.UserName=?",(user_name,))
    userinfo = cursor.fetchall()
    conn.close()
    return userinfo

def fetch_user_list():
    """データベースからusers情報を取得"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT UserID, UserName FROM userinfo")
    user_info = cursor.fetchall()
    conn.close()
    return user_info

def fetch_user_attendance(user_id):
    """(user)データベースから指定したusers勤怠情報を取得"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT Date, WorkStartTime, WorkEndTime, WorkingTime, Memo FROM AttendanceRecord WHERE UserID =?", (user_id,))
    recordlist = cursor.fetchall()
    conn.close()
    return recordlist

def fetch_user_attendance1(user_id, yearmonth):
    """(年月)データベースから指定したusers勤怠情報を取得"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(f"SELECT Date, WorkStartTime, WorkEndTime, WorkingTime, Memo FROM AttendanceRecord WHERE UserID=? AND YearMonth=?", (user_id, yearmonth))
    recordlist = cursor.fetchall()
    conn.close()
    return recordlist

def update_user_attendance(user_id, yearmonth, day, starting_time, ending_time, working_time, memo):
    """データベースから指定したusers勤怠情報を更新"""
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """UPDATE AttendanceRecord
               SET WorkStartTime=?, WorkEndTime=?, WorkingTime=?, Memo=?
               WHERE UserID=? AND YearMonth=? AND Date=?"""
    cursor.execute(query, (starting_time, ending_time, working_time, memo, user_id, yearmonth, day))
    conn.commit()
    conn.close()

def insert_department(department_name, start_time, end_time, rest_time, over_time):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(DepartmentID) FROM DepartmentMaster")
    last_department_id = cursor.fetchone()[0]
    if last_department_id is not None and int(last_department_id) >= 100:
            messagebox.showerror("Error", "The maximum number of divisions is 100. To add a new division,delete the current division")
            conn.close()
            return
    cursor.execute('''INSERT INTO DepartmentMaster (DepartmentName, WorkStartTime, WorkEndTime, RestTime, OverTime)
              VALUES (?, ?, ?, ?, ?)''',
              (department_name, start_time, end_time, rest_time, over_time))
    conn.commit()
    conn.close()

def fetch_departmentname():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentName FROM DepartmentMaster")
    departmentlist = [row[0] for row in cursor.fetchall()]
    conn.close()
    return departmentlist

def fetch_departmentname_by_departmentname(department_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentName FROM DepartmentMaster WHERE DepartmentName=?",(department_name,))
    departmentlist = [row[0] for row in cursor.fetchall()]
    conn.close()
    return departmentlist

def fetch_department(department_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentName, WorkStartTime, WorkEndTime, RestTime, OverTime FROM DepartmentMaster WHERE DepartmentName=?",(department_name,))
    department = cursor.fetchone()
    conn.close()
    return department

def delete_department(department_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM DepartmentMaster WHERE DepartmentName=?",(department_name,))
    conn.commit()
    conn.close()

def insert_userinfo(UserName, Password, DepartmentName, AdminFlag, FacePhoto):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentID FROM DepartmentMaster WHERE DepartmentName = ?", (DepartmentName,))
    result = cursor.fetchone()
    if result:
        DepartmentID = result[0]
        cursor.execute('''INSERT INTO userinfo (UserName, Password, DepartmentID, AdminFlag, FacePhoto)
                          VALUES (?, ?, ?, ?, ?)''', (UserName, Password, DepartmentID, AdminFlag, FacePhoto))
        conn.commit()
    conn.close()

def update_department(department_name, start_time, end_time, rest_time, over_time):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("UPDATE DepartmentMaster SET DepartmentName = ?, WorkStartTime = ?, WorkEndTime = ?, RestTime = ?, OverTime = ? WHERE DepartmentName = ?", (department_name, start_time, end_time, rest_time, over_time, department_name))
    conn.commit()
    conn.close()

def update_userinfo(user_id, UserName, Password, DepartmentName, AdminFlag, FacePhoto):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentID FROM DepartmentMaster WHERE DepartmentName = ?", (DepartmentName,))
    result = cursor.fetchone()
    if result:
        DepartmentID = result[0]
        query = """UPDATE userinfo
                   SET UserName=?, Password=?, DepartmentID=?, AdminFlag=?, FacePhoto=?
                   WHERE UserID=?"""
        cursor.execute(query, (UserName, Password, DepartmentID, AdminFlag, FacePhoto, user_id))
        conn.commit()
    conn.close()

import sqlite3

def fetch_userinfo_by_username(username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM userinfo WHERE UserName = ?", (username,))
    userinfo = cursor.fetchall()
    conn.close()
    return userinfo

def delete_user_by_username(username):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM userinfo WHERE UserName = ?", (username,))
    conn.commit()
    rows_deleted = cursor.rowcount
    conn.close()
    return rows_deleted 

def fetch_next_user_id():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(UserID) FROM userinfo")
    max_id = cursor.fetchone()[0] 
    conn.close()
    if max_id is None:
        return 1
    else:
        return max_id + 1

def load_department_settings(user_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentID FROM userinfo WHERE UserID=?", (user_id,))
    department_id = cursor.fetchone()[0]
    cursor.execute("SELECT OverTime, WorkEndTime FROM DepartmentMaster WHERE DepartmentID = ?", (department_id,))
    result = cursor.fetchone()
    return result

def fetch_usernames_by_departmentname(department_name):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    query = """
    SELECT userinfo.UserName
    FROM userinfo
    INNER JOIN DepartmentMaster ON userinfo.DepartmentID = DepartmentMaster.DepartmentID
    WHERE DepartmentMaster.DepartmentName = ?
    """
    cursor.execute(query, (department_name,))
    usernames = cursor.fetchall()
    conn.close()
    return [username[0] for username in usernames]

def save_work_start_time(userid):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT DepartmentID FROM userinfo WHERE UserID = ?", (userid,))
    department_id_result = cursor.fetchone()
    department_id = department_id_result[0]
    cursor.execute("SELECT WorkStartTime FROM DepartmentMaster WHERE DepartmentID = ?", (department_id,))
    work_start_time_str = cursor.fetchone()
    work_start_time_str = work_start_time_str[0]

    today_date = datetime.datetime.now().date()
    work_start_time = datetime.datetime.strptime(f"{today_date} {work_start_time_str}", '%Y-%m-%d %H:%M')
    current_time = datetime.datetime.now()

    later_time = max(work_start_time, current_time)
    today_year_month = current_time.strftime('%Y%m')
    today_date = current_time.strftime('%d')
    cursor.execute("""
        INSERT INTO AttendanceRecord (UserID, YearMonth, Date, WorkStartTime, WorkEndTime, WorkingTime, Memo)
        VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (userid, today_year_month, today_date, later_time.strftime('%H:%M'), 0, 0, ''))
    conn.commit()
    conn.close()

def save_work_end_time(userid):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("SELECT DepartmentID FROM userinfo WHERE UserID = ?", (userid,))
    department_id = cursor.fetchone()[0]

    cursor.execute("SELECT RestTime FROM DepartmentMaster WHERE DepartmentID = ?", (department_id,))
    rest_time = cursor.fetchone()[0]

    current_time = datetime.datetime.now()
    formatted_current_time_str = current_time.strftime('%d %H:%M')
    formatted_current_time = datetime.datetime.strptime(formatted_current_time_str, '%d %H:%M')

    cursor.execute("""
            SELECT WorkStartTime, Date FROM AttendanceRecord
            WHERE UserID = ? AND YearMonth = ? AND Date = ?""",
            (userid, current_time.strftime('%Y%m'), current_time.strftime('%d')))
    start_time_result = cursor.fetchone()
 
    start_time_str, start_date = start_time_result
    start_time = datetime.datetime.strptime(f"{start_date} {start_time_str}", '%d %H:%M') 

    rest_time_seconds = rest_time * 3600  
    working_time_seconds = (formatted_current_time - start_time).total_seconds() - rest_time_seconds
    working_time_hours = max(0, working_time_seconds / 3600)
    working_time_hours = round(working_time_hours, 1)
    cursor.execute("""
                UPDATE AttendanceRecord
                SET WorkEndTime = ?, WorkingTime = ?
                WHERE UserID = ? AND YearMonth = ? AND Date = ?""",
                (current_time.strftime('%H:%M'), working_time_hours, userid, current_time.strftime('%Y%m'), current_time.strftime('%d')))
    conn.commit()
    conn.close()