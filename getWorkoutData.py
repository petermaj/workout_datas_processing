import xlrd
def openWorkbook(location):
    workbook = xlrd.open_workbook(location)
    return workbook
def getDatas(workbook, row):    
    sheet = workbook.sheet_by_index(0)     
    sheet.cell_value(0, 0) 
    return (sheet.row_values(row)) 

def getRowNumber(workbook, name):     
    worksheet=workbook.sheet_by_name(name)
    return worksheet.nrows


#How to call functions:
#workbook=openWorkbook("workoutdata/Move_2019_07_29_17_38_24_Cycling.xlsx")
#getDatas(workbook,2)
#getRowNumber(workbook,"29 Jul 2019 17_38_24")


#Result:
#['Cycling', '2019-07-29T05:38:24', 8613.9, 1229.0, 51372.0, 107.0, 47.664239, 17.634368, 21.470004, 3.0, 38.0, 559.0, 28.0, 411.0, 7643.9, 128.0, 108.0, 56.0, 179.0, 12.41111, 1.0, 'Suunto Ambit3 Sport', '2019-07-29T05:38:24', 0.0, '', 0.0, 'Unspecified sport', 0.0, 0.0, 0.0, 3.5, '2019-07-29T05:38:24', 8.0, '', 0.0, 'Unspecified sport', 0.0, 0.0, 0.0, 3.5, '2019-07-29T08:01:56.877', 2.0, '', 8612.878, 'Cycling', 96.0, 107.0, 5.96456, 96.0, 51372.0, 12.4, '2019-07-29T05:38:24', 0.0, 0.0, 76.0, 3.5, -0.4, 0.0, '', 1041.0]