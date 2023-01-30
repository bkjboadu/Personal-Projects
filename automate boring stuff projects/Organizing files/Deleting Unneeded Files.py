import os
from pathlib import Path

path = Path(r'C:\Users\104535brbo\Desktop')

for folder,subfolder,file in os.walk(path):
    if os.path.getsize(folder) > 100000:
        print(folder + '-->' +  str(os.path.getsize(folder)))
    for file in file:
        try:
            if os.path.getsize(file) > 100000:
                print(file + '-->' +   str(os.path.getsize(file)))
        except FileNotFoundError:
            pass