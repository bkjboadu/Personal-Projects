import shutil,os
from pathlib import Path

destination = Path(r'C:\Users\104535brbo\Desktop\new1')
for files in Path.cwd().glob('*.txt'):
    shutil.copy(files,destination)

for files in Path.cwd().glob('*.pdf'):
    shutil.copy(files,destination)

for files in Path.cwd().glob('*.py'):
    shutil.copy(files,destination)
