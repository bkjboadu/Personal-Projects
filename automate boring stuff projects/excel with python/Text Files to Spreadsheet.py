import openpyxl
from pathlib import Path

text_files = []
for file in Path.cwd().glob('*.txt'):
    text_files.append(file)

new = openpyxl.Workbook()
newa = new.active
for i in range(len(text_files)):
    with open(text_files[i],'r') as f:
        lines = f.readlines()
        print(len(lines))
        for x in range(len(lines)):
            newa.cell(row=x+1,column=i+1).value = lines[x]

new.save('done.xlsx')