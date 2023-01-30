import re

ssregex = re.compile(r'''(
(\d{3}-) #firt 3
(\d{2}-) #second 2
(\d{4})  #third 4
)''',re.VERBOSE)

creregex = re.compile(r'''(
(\d{4}\s) #first 4
(\d{4}\s) #second 4
(\d{4}\s) #third 4
(\d{4})   #fourth 4
)''',re.VERBOSE)

text = 'there are and so much more'
for social in ssregex.findall(text):
    sisocial = re.compile(social[0])
    remove = sisocial.sub('',text)
    text = remove
for credit in creregex.findall(text):
    cred = re.compile(credit[0])
    remove = cred.sub('',text)
    text = remove
print(text)
