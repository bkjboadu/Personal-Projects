import sys
from pathlib import Path
import PyPDF2,os

if len(sys.argv) > 1:
    password = sys.argv[1]
else:
    password = 'bright'

path = os.getcwd()
pdfs = []
for folders,subfolder,files in os.walk(path):
    for file in files:
        if not file.endswith('.pdf'):
            continue
        else:
            stem = Path(os.path.abspath(file)).stem
            new_name = stem + '_encrypted.pdf'
            newpdf = open(new_name,'wb')
            pdfObj = PyPDF2.PdfFileWriter()
            openfile = open(file,'rb')
            pdfreader = PyPDF2.PdfFileReader(openfile)
            if pdfreader.isEncrypted:
                pdfreader.decrypt('bright')

            for i in range(pdfreader.numPages):
                pdfObj.addPage(pdfreader.getPage(i))
            pdfObj.encrypt(password)
            pdfObj.write(newpdf)
            pdfs.append(new_name)



print(pdfs)



