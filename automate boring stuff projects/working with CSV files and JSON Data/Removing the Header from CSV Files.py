import csv
from pathlib import Path


for file in Path.cwd().glob('*.csv'):
    print(file)
    old = open(file)
    reader = csv.reader(old)
    csvrow = []
    for row in reader:
        if reader.line_num == 1:
            continue
        csvrow.append(row)
    old.close()
    new = open(file,'w',newline='')
    csvwriter = csv.writer(new)
    for row in csvrow:
        csvwriter.writerow(row)
    new.close()


