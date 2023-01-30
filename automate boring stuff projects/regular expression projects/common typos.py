import re

space_regex = re.compile(r'\s{2,}')
exclamation_regex = re.compile(r'!{2,}')
repeated_words_regex = re.compile(r'\b(\w+)\s+\1\b')
matches = []
text = '''Find common typos typos typos such as  multiple  spaces between  words,  accidentally
accidentally accidentally repeated words, or multiple exclamation marks at the
end of sentences. Those are annoying!!'''
for match in space_regex.findall(text):
    matches.append(match)

for match in exclamation_regex.findall(text):
    matches.append(match)

for match in repeated_words_regex.findall(text):
    matches.append(match)

print(matches)