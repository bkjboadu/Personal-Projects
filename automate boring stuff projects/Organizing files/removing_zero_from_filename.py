import os,shutil
import re
from pathlib import Path

zeroregex = re.compile('''(
(0+) #find zeros
)''',re.VERBOSE)

for file in Path.cwd().glob('*.txt'):
    filename = str(Path(file).name)
    zerofile = zeroregex.findall(filename)
    if not zerofile:
        continue

    new_filename = Path.cwd() / zeroregex.sub('',filename)
    os.rename(file,new_filename)



