#! python3
# mclip.py - A multi-clipboard program.
import sys,pyperclip
TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
'busy': """Sorry, can we do this later this week or next week?""",
'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: python mclip.py [keyphrase] - copy phrase text')
    sys.exit()

keyphrase = sys.argv[1]

if keyphrase in TEXT:
    print('Text for ' + keyphrase + ' copied to clipboard')
    pyperclip.copy(TEXT[keyphrase])
else:
    print('There is no text for ' + keyphrase)


