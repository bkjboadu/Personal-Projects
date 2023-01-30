from pathlib import Path
import re
p = Path.cwd()
userRegex = re.compile(r'my exes ')
for file in p.glob('*.txt'):
    with open(file,'r') as new_file:
        for line in new_file.readlines():
            if userRegex.search(line):
                print(line,end='')



