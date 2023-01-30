import PyPDF2,os,re
from pathlib import Path
pdfWriter = PyPDF2.PdfFileWriter()


for files in Path.cwd().glob('*.pdf'):
    pdfFile = open(files,'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    if pdfReader.isEncrypted:
        pdfReader.decrypt('bright')

    for pageNum in range(1,pdfReader.numPages):
        pdfWriter.addPage(pdfReader.getPage(pageNum))

pdfOutputFile = open('combined.pdf','wb')
pdfWriter.write(pdfOutputFile)
pdfOutputFile.close()








