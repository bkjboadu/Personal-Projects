import os,re,shutil
from pathlib import Path
euro_date = re.compile(r'''
(.*)?  #before dates
((0|1)\d) #month 
-
((0|1|2|3)\d)
-
((19|20)\d\d) # year
(.*)? #extension''',re.VERBOSE)

for file in Path.cwd().glob('*'):
    euro_file = euro_date.search(str(file))
    if not euro_file:
        continue

    america_file = euro_file.group(1) + euro_file.group(4) + '-' + euro_file.group(2) + '-' + euro_file.group(6) + euro_file.group(8)
    os.rename(file,america_file)
    print(america_file)

