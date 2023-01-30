grid = [['.', '.', '.', '.', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['O', 'O', 'O', 'O', 'O', '.'],
['.', 'O', 'O', 'O', 'O', 'O'],
['O', 'O', 'O', 'O', 'O', '.'],
['O', 'O', 'O', 'O', '.', '.'],
['.', 'O', 'O', '.', '.', '.'],
['.', '.', '.', '.', '.', '.',]]

def pictures(x):
    len_of_list = []
    for y in x:
        len_of_list.append(len(y))
    print(max(len_of_list))
    for i in range(max(len_of_list)):
        string_to_print = ''
        for j in range(len(x)):
            try:
                string_to_print += x[j][i]
            except IndexError:
                continue
        print(string_to_print)


pictures(grid)