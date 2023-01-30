text = '''The ADJECTIVE panda walked to the NOUN and then VERB. A nearby NOUN was
unaffected by these events.'''

things_to_replace = ['ADJECTIVE','ADVERB','NOUN','VERB']
for word in text.split(' '):
    if word in things_to_replace:
        print(f'Enter an {word}')
        new_word = input()
        text = text.replace(word,new_word)
    elif word[:len(word)-1] in things_to_replace:
        print(f'Enter an {word[:len(word)-1]}')
        new_word = input()
        text = text.replace(word[:len(word)-1], new_word)

print(text)


