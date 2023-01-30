#Filling in the Gaps
import os,re,shutil
from pathlib import Path

spam_regex = re.compile(r'(spam(\d{3})\.txt)')
match = []

for file in os.listdir(Path.cwd()):
    spam = spam_regex.findall(str(file))
    if not spam:
        continue
    for spam in spam:
        match.append(spam)

New_Name = [match[0]]
for i in range(len(match)):
    try:
        if int(match[i+1][1]) != int(New_Name[i][1]) + 1:
            New_Name.append((match[i+1][0],str(int(New_Name[i][1]) + 1).zfill(3)))
        else:
            New_Name.append(match[i + 1])
    except IndexError:
        continue


for names in New_Name:
    rename = 'spam' + names[1] + '.txt'
    shutil.move(Path.cwd() / names[0],Path.cwd() / rename)

print('Done')




