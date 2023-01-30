import os,shutil

os.makedirs('bright1',exist_ok=True)
for file in os.listdir(os.getcwd()):
    if file.endswith('.pdf') or file.endswith('.jpg') or file.endswith('.txt'):
        shutil.copy(file,'bright1')
    else:
        pass

