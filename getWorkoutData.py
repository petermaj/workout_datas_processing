# Program to extract a particular row value 
import xlrd

def getDatas(location, row):    
    wb = xlrd.open_workbook(location)
    sheet = wb.sheet_by_index(0)     
    sheet.cell_value(0, 0) 
    
    print(sheet.row_values(row)) 

#How to call function:
#getDatas("workoutdata/Move_2019_07_29_17_38_24_Cycling.xlsx",2)


#Result:
#['Cycling', '2019-07-29T05:38:24', 8613.9, 1229.0, 51372.0, 107.0, 47.664239, 17.634368, 21.470004, 3.0, 38.0, 559.0, 28.0, 411.0, 7643.9, 128.0, 108.0, 56.0, 179.0, 12.41111, 1.0, 'Suunto Ambit3 Sport', '2019-07-29T05:38:24', 0.0, '', 0.0, 'Unspecified sport', 0.0, 0.0, 0.0, 3.5, '2019-07-29T05:38:24', 8.0, '', 0.0, 'Unspecified sport', 0.0, 0.0, 0.0, 3.5, '2019-07-29T08:01:56.877', 2.0, '', 8612.878, 'Cycling', 96.0, 107.0, 5.96456, 96.0, 51372.0, 12.4, '2019-07-29T05:38:24', 0.0, 0.0, 76.0, 3.5, -0.4, 0.0, '', 1041.0]