import pyperclip, sys, shelve

# check system argument that runs with mcb.pyw
shelfile = shelve.open('myclipboard')
if len(sys.argv) == 1:
    print('no action taken yet')
elif sys.argv[1] == 'list':
    print(list(shelfile.keys()))
elif sys.argv[1] == 'save':
    try:
        shelfile[sys.argv[2]] = pyperclip.paste()
        print('keyword has been copied to shelfile')
    except IndexError:
        print('One more argument needed')
elif len(sys.argv) > 2 and sys.argv[1] == 'delete':
    try:
        del shelfile[sys.argv[2]]
        print('keyword has been deleted from shelfile')
    except IndexError:
        print('One more argument needed')
elif len(sys.argv) == 2 and sys.argv[1] == 'delete':
    try:
        for keyword in list(shelfile.keys()):
            del shelfile[keyword]
        print('keyword has been deleted from shelfile')
    except IndexError:
        print('One more argument needed')
elif sys.argv[1] in list(shelfile.keys()):
    pyperclip.copy(shelfile[sys.argv[1]])
    print('keyword copied to clipboard')
elif sys.argv[1] not in list(shelfile.keys()):
    print('Argument no found in shelfile list')

shelfile.close()



