import time
import xlsxwriter
import cv2
import os

###DB Access###
import XFaceDAO 
dbaccess = XFaceDAO.XFaceDAO()

class EmployeeInfo():    
    def ExcelOutput(self,yearmonth):
        filename = "employeeinfo/employee_list_" + yearmonth + ".xlsx"
        # Create one if not exists.
        if not os.path.isfile(filename):
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet(yearmonth)
            cell_format = workbook.add_format({'bold': True, 'italic': True,'align':'center'})
            cell_format2 = workbook.add_format({'align':'vcenter'})
            worksheet.set_column('A:A',20)
            worksheet.set_column('B:B',20)
            worksheet.set_column('C:C',20)
            worksheet.set_column('D:D',20)
            worksheet.write('A1','UserId',cell_format)
            worksheet.write('B1','Name',cell_format)
            worksheet.write('C1','Password',cell_format)
            worksheet.write('D1','Profile',cell_format)
            row = 1
            col = 0
            #userinfolist = [["111112","fuji","111111"]]   ###
            userinfolist = dbaccess.getUserInfo()   #[UserID, UserName, Password]
            for userid, username, password in userinfolist:
                worksheet.write(row, col,     userid,cell_format2)
                worksheet.write(row, col + 1, username,cell_format2)
                worksheet.write(row, col + 2, password,cell_format2)
                worksheet.set_row(row,114)
                Image = cv2.imread('pic/{}/{}.png'.format(username, username))
                if Image is None:
                    worksheet.write(row, col + 2, Image)
                else:
                    # imgdata = base64.b64decode(Image)         #yamaji 11.10
                    # image = io.BytesIO(imgdata)               #yamaji 11.10
                    worksheet.insert_image(row,col+2, 'pic/{}/{}.png'.format(username, username), {'x_scale': 0.5, 'y_scale': 0.5})#yamaji 11.10 change    #'1.png', {'image_data': image,'x_scale': 0.1, 'y_scale': 0.1})
                row += 1
            workbook.close()

class AttendanceRecord():        
    def ExcelOutput_user(self,userid,username,yearmonth):   #このメソッドを実行する際に、userid,username,yearmonthを引数に指定する必要がある
        filename = "attendancerecord/AttendanceRecord_{}{}_".format(userid,username) + yearmonth + ".xlsx"
        # Create one if not exists.
        if not os.path.isfile(filename):
            workbook = xlsxwriter.Workbook(filename)
            worksheet = workbook.add_worksheet(yearmonth)
            cell_format = workbook.add_format({'bold': True, 'italic': True,'align':'center'})
            cell_format2 = workbook.add_format({'align':'vcenter'})
            worksheet.set_column('A:A',20)
            worksheet.set_column('B:B',20)
            worksheet.set_column('C:C',20)
            worksheet.set_column('D:D',20)
            worksheet.set_column('E:E',20)
            worksheet.write('A1','Date',cell_format)
            worksheet.write('B1','StartingTime',cell_format)
            worksheet.write('C1','EndingTime',cell_format)
            worksheet.write('D1','WorkingTime',cell_format)
            worksheet.write('E1','Memo',cell_format)
            row = 1
            col = 0
            #recordlist_user = [["01","10:00","19:00","8",""],]   ###
            recordlist_user = dbaccess.getAttendanceRecord_recordlist(userid,int(yearmonth)) #[Date,StartingTime,EndingTime,WorkingTime,Memo]
            for date, startingtime, endingtime, workingtime, memo in recordlist_user:
                worksheet.write(row, col,     date, cell_format2)
                worksheet.write(row, col + 1, startingtime, cell_format2)
                worksheet.write(row, col + 2, endingtime, cell_format2)
                worksheet.write(row, col + 3, workingtime, cell_format2)
                worksheet.write(row, col + 4, memo, cell_format2)
                row += 1
            workbook.close()

    def ExcelOutput_list(self,yearmonth):   #このメソッドを実行する際に、yearmonthを引数に指定する必要がある
        filename = "attendancerecord/AttendanceRecord_list_" + yearmonth + ".xlsx"
        # Create one if not exists.
        if not os.path.isfile(filename):
            workbook = xlsxwriter.Workbook(filename)
            cell_format = workbook.add_format({'bold': True, 'italic': True,'align':'center'})
            cell_format2 = workbook.add_format({'align':'vcenter'})
            userlist = []
            userlist = [["100000","fuji"],]   ###   ここでUserInfoにあるユーザーIDとユーザー名を取得する
            #userlist = dbaccess.getUserInfo_userlist() #[UserID, UserName]
            for userid, username in userlist:
                worksheet = ""               
                worksheet = workbook.add_worksheet("{}_{}".format(userid, username))                
                worksheet.set_column('A:A',20)
                worksheet.set_column('B:B',20)
                worksheet.set_column('C:C',20)
                worksheet.set_column('D:D',20)
                worksheet.set_column('E:E',20)
                worksheet.write('A1','Date',cell_format)
                worksheet.write('B1','StartingTime',cell_format)
                worksheet.write('C1','EndingTime',cell_format)
                worksheet.write('D1','WorkingTime',cell_format)
                worksheet.write('E1','Memo',cell_format)
                row = 1
                col = 0
                recordlist = []
                #recordlist = [["01","10:00","19:00","8",""],["02","10:00","19:30","8.5",""],["03","","","","有給休暇取得"]]
                recordlist = dbaccess.getAttendanceRecord_recordlist(userid,yearmonth)
                for date, startingtime, endingtime, workingtime, memo in recordlist:
                    worksheet.write(row, col,     date, cell_format2)
                    worksheet.write(row, col + 1, startingtime, cell_format2)
                    worksheet.write(row, col + 2, endingtime, cell_format2)
                    worksheet.write(row, col + 3, workingtime, cell_format2)
                    worksheet.write(row, col + 4, memo, cell_format2)
                    row += 1
            workbook.close()


#employeeinfo = EmployeeInfo()
#employeeinfo.ExcelOutput()

#userid = "000001"
#username = "fuji"
#yearmonth = str(time.strftime("%Y%m"))
#attendancerecord = AttendanceRecord()
#attendancerecord.ExcelOutput_user(userid,username,yearmonth)
#attendancerecord.ExcelOutput_list(yearmonth)
#print("Excel output close")