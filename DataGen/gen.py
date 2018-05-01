from openpyxl import Workbook
import data

'''
生成数据文件
:param num 数据个数
:para filename 文件名，默认data.xlsx
'''
def gendata(num, filename="data"):
    indata = []
    wb = Workbook()
    wb.create_sheet("Data", index=0)
    sheet = wb.get_sheet_by_name("Data")
    for i in range(num):
        indata.append(data.rowData(i))
    for i in indata:
        sheet.append(i.list_all())
    wb.save(filename + ".xlsx")
