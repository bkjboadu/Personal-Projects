import zipfile,os

def backupToZip(folder):

    folder = os.path.abspath(folder)

    number = 1
    while True:
        zipfilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipfilename):
            break
        number += 1

    print(f'Creating {zipfilename}....')
    backupZip = zipfile.ZipFile(zipfilename,'w')
    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Adding the current folder to the ZIP file.')
        backupZip.write(foldername)

        for filename in filenames:
            newBase = os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()

    print('Done')


def create_zipfile(folder):
    name = 'AlsPythonBook_'
    number = 1
    while True:
        check_name = Path(folder) / Path(name + str(number) + '.zip')
        print(check_name)
        if not Path(check_name).exists():
            break
        number += 1

    zipfile_name = name + str(number) + '.zip'
    ExZip = zipfile.ZipFile(zipfile_name,'w')
    for file in os.listdir(folder):
        ExZip.write(file,compress_type=zipfile.ZIP_DEFLATED)
        print(file)
    ExZip.close()

create_zipfile(Path.cwd())

backupToZip(r'C:\delicious')
