import XFace_Database_Function
import xlsxwriter
import datetime
import os

# 共通部分
def initialize_workbook(filename, sheet_name):
    """excelの作成と設定"""
    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(sheet_name)
    # フォーマット設定
    formats = {
        'bold_italic_center': workbook.add_format({'bold': True, 'italic': True, 'align': 'center'}),
        'vcenter': workbook.add_format({'align': 'vcenter'}),
        'yellow': workbook.add_format({'bg_color': '#FFFF00'})
    }
    # 列の広さ
    worksheet.set_column('A:F', 20)
    return workbook, worksheet, formats

def calculate_time_deltas(endingtime, overtime_threshold, worksheet, row, format):
    """残業の確認"""
    datetime_obj = datetime.datetime.strptime(endingtime, "%H:%M")
    new_datetime_obj = datetime_obj + datetime.timedelta(minutes=overtime_threshold)
    max_time = new_datetime_obj.strftime("%H:%M")
    max_hour, max_minute = max_time.split(':')
    worksheet.conditional_format(0, 3, row - 1, 3, {
        'type': 'formula', 'criteria': f'=TIMEVALUE(INDIRECT("C"&ROW())) >= TIME({max_hour},{max_minute},0)',
        'format': format['yellow']
    })

def calculate_work_time(recordlist, datetime_obj, overtime_threshold, worksheet, format):
    """残業時間の計算(未確定)"""
    total_working_time, total_overtime, total_overtime_min = 0.0, 0.0, 0.0
    obj_datetime = datetime.datetime.strptime(datetime_obj, "%H:%M")
    row = 1  # 計算開始の行
    for _, _, endingtime, workingtime, memo in recordlist:
        if memo == "有給休暇取得":
            total_working_time += 8 # 有給休暇取得は8時間として
        else:
            try:
                ending_datetime = datetime.datetime.strptime(endingtime, "%H:%M")
                delta = (ending_datetime - obj_datetime).total_seconds() / 60
                working_hours = float(workingtime)
                if working_hours > 8:  # 仕事時間は8時間に超えるかの確認
                    if delta >= overtime_threshold: # 設定の時間を超えたら、残業を認める
                        total_working_time += 8 
                        total_overtime += working_hours - 8
                        total_overtime_min += delta
                    else:
                        total_working_time += 8
                else:
                    total_working_time += working_hours
            except ValueError:
                continue
        row += 1
    """    
    summary_data = [
        (f"合計{total_working_time + total_overtime}"),
        (f"残業時間(h): {total_overtime:.1f}"),
        (f"残業時間(min): {total_overtime_min}"),
        (f"直接作業時間: {total_working_time}")
    ]
    for i, value in enumerate(summary_data):
        worksheet.write(row + i, 3, value, format)
    """
    
def write_headers(worksheet, headers, format):
    """タイトルの入力"""
    for col, header in enumerate(headers):
        worksheet.write(0, col, header, format)

def write_data(worksheet, recordlist, format):
    """データの入力"""
    row = 1
    for record in recordlist:
        for col, value in enumerate(record):
            worksheet.write(row, col, value, format)
        row += 1
    return row

"""
    User情報の中に顔写真もあるので、写真画像も出力が必要（未実装）
    Image = cv2.imread('pic/{}/{}.png'.format(username, username))
    if Image is None:
        worksheet.write(row, col + 2, Image)
    else:
        # imgdata = base64.b64decode(Image)         #yamaji 11.10
        # image = io.BytesIO(imgdata)               #yamaji 11.10
        worksheet.insert_image(row,col+2, 'pic/{}/{}.png'.format(username, username), {'x_scale': 0.5, 'y_scale': 0.5})#yamaji 11.10 change    #'1.png', {'image_data': image,'x_scale': 0.1, 'y_scale': 0.1})
"""
# 主体部分
class EmployeeInfo:
    def __init__(self):
        self.userinfolist = XFace_Database_Function.fetch_user_info() # databaseからuserinfolistを取得

    def ExcelOutput(self,yearmonth):
        """User情報を出力"""
        filename = "UserInformation.xlsx"
        if not os.path.isfile(filename):
            self.workbook, self.worksheet, self.formats = initialize_workbook(filename, yearmonth)
            headers = ['UserID', 'UserName', 'Password', 'DepartmentName', 'AdiminFlag']
            write_headers(self.worksheet, headers, self.formats['bold_italic_center'])
            write_data(self.worksheet, self.userinfolist, self.formats['vcenter'])
            self.workbook.close()

class AttendanceRecord:
    def __init__(self):
        self.userinfolist = XFace_Database_Function.fetch_user_list() # databaseからuserinfolistを取得
        # 会社による、終了時間(xx:xx)と残業認め時間(int(分))が異なるので、設定できる

    def ExcelOutput_user(self, userid, username, yearmonth):
        """Userごとに勤怠情報をexcelに出力"""
        filename = f"AttendanceRecord_{userid}_{username}.xlsx"
        if not os.path.isfile(filename):
            self.workbook, self.worksheet, self.formats = initialize_workbook(filename, yearmonth)
            headers = ['Date', 'WorkStartTime', 'WorkEndTime', 'WorkingTime', 'Memo']
            write_headers(self.worksheet, headers, self.formats['bold_italic_center'])
            recordlist = XFace_Database_Function.fetch_user_attendance(userid)
            result = XFace_Database_Function.load_department_settings(userid)
            overtime_threshold = int(result[0])
            endingtime = result[1]
            last_row = write_data(self.worksheet, recordlist, self.formats['vcenter'])
            calculate_time_deltas(endingtime, overtime_threshold, self.worksheet, last_row, self.formats)
            calculate_work_time(recordlist, endingtime, overtime_threshold, self.worksheet, self.formats['vcenter'])
            self.workbook.close()

    def ExcelOutput_list(self, yearmonth):
        """全員の勤怠情報をexcelに出力"""
        filename = f"AttendanceRecord_allUser_{yearmonth}.xlsx"
        if not os.path.isfile(filename):
            self.workbook, self.yearmonthsheet, self.formats = initialize_workbook(filename, yearmonth)
            userlist = self.userinfolist
            # excelの最初sheetはuser基本情報
            headers = ['UserID', 'UserName']
            write_headers(self.yearmonthsheet, headers, self.formats['bold_italic_center'])
            write_data(self.yearmonthsheet, userlist, self.formats['vcenter'])
            # userごとに詳細な勤怠情報を出力
            for userid, username in userlist:
                self.worksheet = self.workbook.add_worksheet(f"{userid}_{username}")
                self.worksheet.set_column('A:F', 20)
                headers = ['Date', 'WorkStartTime', 'WorkEndTime', 'WorkingTime', 'Memo']
                write_headers(self.worksheet, headers, self.formats['bold_italic_center'])
                recordlist = XFace_Database_Function.fetch_user_attendance(userid)
                result = XFace_Database_Function.load_department_settings(userid)
                overtime_threshold = int(result[0])
                endingtime = result[1]
                last_row = write_data(self.worksheet, recordlist, self.formats['vcenter'])
                calculate_time_deltas(endingtime, overtime_threshold, self.worksheet, last_row, self.formats)
                calculate_work_time(recordlist, endingtime, overtime_threshold, self.worksheet, self.formats['vcenter'])
            self.workbook.close()
