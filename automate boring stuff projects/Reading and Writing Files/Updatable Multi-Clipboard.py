import pprint,shelve
import sys,pyperclip

TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}


if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]
if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + ' copied to clipboard')
elif keyphrase.lower() == 'list':
    print(pprint.pprint(TEXT.keys()))
elif keyphrase.lower() == 'save' and len(sys.argv) == 3:
    TEXT[sys.argv[2]] = pyperclip.paste()
    print(TEXT)
else:
    print('There is no task for ' + keyphrase)





