import os,shutil,re
from pathlib import Path

euro = re.compile('''(
(\d{2}) #day
-
(\d{2}) #month
-
(\d{4}) #year
)''',re.VERBOSE)

for file in Path.cwd().glob('*'):
    ams = euro.findall(str(file))
    if not ams:
        continue

    for group in ams:
        america = group[2] + '-' + group[1] + '-' + group[3]
        new_filename = str(Path.cwd() / str(euro.sub(america,str(file))))
    os.rename(file,new_filename)

