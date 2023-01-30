import os,shutil
from pathlib import Path

for file in Path.cwd().glob('*.txt'):
    filename = str(Path(file).name)
    new_filename =str( Path.cwd() / ('spam0042' + filename))
    os.rename(str(file),new_filename)
