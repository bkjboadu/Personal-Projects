import PyPDF2

words = []
with open('dictionary.txt','r') as f:
    for line in f.readlines():
        words.append(line.strip('\n'))

pdfObj = open('encrypted.pdf','rb')
pdfreader = PyPDF2.PdfFileReader(pdfObj)
for password in words:
    if pdfreader.decrypt(password.lower()):
        print(1)
        print(password.lower())
        break
    elif pdfreader.decrypt(password.upper()):
        print(1)
        print(password.upper())
        break
    else:
        print(0)