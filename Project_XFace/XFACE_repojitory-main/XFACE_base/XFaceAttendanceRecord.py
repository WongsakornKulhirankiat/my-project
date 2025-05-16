import time
import xlsxwriter
import xlwt
import cv2
import os

ItemList = [["fujiwara","111111"],["yamaji","222222"],["oohasi","333333"]]

class AttendanceRecord():
    
    
    def ExcelOutput():
        filename = "log/employee_list_" + str(time.strftime("%Y-%m-%d")) + ".xlsx"
        # Create one if not exists.
        if not os.path.isfile(filename):
            w = xlwt.Workbook(filename)
            w.add_sheet('Sheet1')
            w.save(filename)
        workbook = xlsxwriter.Workbook(filename)
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'italic': True,'align':'center'})
        cell_format2 = workbook.add_format({'align':'vcenter'})
        worksheet.set_column('A:A',20)
        worksheet.set_column('B:B',10)
        worksheet.set_column('C:C',20)
        worksheet.write('A1','Name',cell_format)
        worksheet.write('B1','Password',cell_format)
        worksheet.write('C1','Profile',cell_format)
        row = 1
        col = 0
        for name, Password in ItemList:
            worksheet.write(row, col,     name,cell_format2)
            worksheet.write(row, col + 1, Password,cell_format2)
            worksheet.set_row(row,114)
            Image = cv2.imread('pic/{}/{}.png'.format(name, name))
            if Image is None:
                worksheet.write(row, col + 2, Image)
            else:
                # imgdata = base64.b64decode(Image)         #yamaji 11.10
                # image = io.BytesIO(imgdata)               #yamaji 11.10
                worksheet.insert_image(row,col+2, 'pic/{}/{}.png'.format(name, name), {'x_scale': 0.5, 'y_scale': 0.5})#yamaji 11.10 change    #'1.png', {'image_data': image,'x_scale': 0.1, 'y_scale': 0.1})
            row += 1
        workbook.close()

#ExcelOutput()
#print("Excel output close")
