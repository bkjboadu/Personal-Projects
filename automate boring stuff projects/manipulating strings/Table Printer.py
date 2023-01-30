tableData = [['apples', 'or', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'mose', 'goose']]

def printTable(x):
    max_length = []
    num_of_string = 0
    for y in x:
        num_of_string = len(y)
        max_row = []
        for z in y:
            max_row.append(len(z))
        max_length.append(max(max_row))
    print(max_length)
    for i in range(num_of_string):
        line = []
        for a in range(len(max_length)):
            word = ' ' * (max_length[a]-len(x[a][i])) + x[a][i]
            line.append(word)
        print(' '.join(line))

printTable(tableData)


