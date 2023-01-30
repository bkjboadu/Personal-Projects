import openpyxl,sys

if len(sys.argv) > 2:
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    filename = sys.argv[3]
else:
    pass

wb = openpyxl.load_workbook(filename)
wba = wb.active
wba.insert_rows(a,b)
wb.save('new_save.xlsx')
