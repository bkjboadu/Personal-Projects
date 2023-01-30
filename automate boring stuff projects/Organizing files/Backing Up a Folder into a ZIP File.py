import os
import zipfile,re
from pathlib import Path

fileregex = re.compile(r'((Bproj).*)')
match = []
for file in Path.cwd().glob('*.zip'):
    if fileregex.findall(str(file)):
        match.append(fileregex.findall(str(file)))

zipfname = f'Bproj_{len(match) + 1}.zip'


new_zip = zipfile.ZipFile(str(zipfname),'w')
for folder,subfolder,filenames in os.walk(os.getcwd()):
    new_zip.write(folder)
    try:
        for filename in filenames:
            if filename.endswith('.zip'):
                continue
            new_zip.write(filename)
    except FileNotFoundError:
        pass

new_zip.close()