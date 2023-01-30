import webbrowser,sys,pyperclip
if len(sys.argv) > 1:
    locate = ' '.join(sys.argv[1:])
else:
    locate = pyperclip.paste()

print(locate)
map = 'https://www.google.com.gh/maps/place/' + str(locate)
webbrowser.open(map)