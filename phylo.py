from ete3 import Tree

matrix = [
            [0, 17, 21, 31, 23],
            [17, 0, 30, 34, 21],
            [21, 30, 0, 28, 39],
            [31, 34, 28, 0, 43],
            [23, 21, 39, 43, 0]
        ]    

trans = [c for c in [chr(x + ord('a')) for x in range(len(matrix))]]

def check_integrity(): 
    width = len(matrix)
    for elt in matrix:
        if len(elt) != width:
            exit(1)

def print_matrix(iteration):
    print('\n')
    print('######## Iteration ' + str(iteration) + ' ########')
    print('\n')
    for i, l in enumerate(matrix):
        print(i, end=' | ')
        for elt in l:
            print(elt, end=' | ')
        print('\n')

def select_min():
    pair = 0, 1
    for i, l in enumerate(matrix):
        mini = l.index(min(i for i in l if i > 0))
        if l[mini] < matrix[pair[0]][pair[1]]:
           pair = i, mini
    return pair


def reduce_matrix(x, y):
    line = matrix[x]
    col = [l[y] for l in matrix]
    # UPGMA
    line_length = len(trans[x])
    col_length = len(trans[y])

    new_line = []
    for i, l in enumerate(matrix[x]):
        if i != x and i != y:
            new_line.append((matrix[x][i] * line_length + matrix[y][i] * col_length) / (line_length + col_length))

    new_line.insert(0, 0)

    for i, l in enumerate(matrix):
        matrix[i] = [v for u, v in enumerate(matrix[i]) if u not in [x, y]]
    
    del matrix[x], matrix[y - 1 if y > 0 else 0]

    print("Ligne nouvellement créée : ", end='')
    print(new_line, end='\n\n')
    matrix.insert(0, new_line)
    for i, l in enumerate(matrix):
        if i != 0:
            matrix[i].insert(0, new_line[i])

def update_trans(x, y):
    pair = trans[x], trans[y]
    del trans[x], trans[y - 1 if y > 0 else 0]
    trans.insert(0, pair)
    print("Nouvelle table de traduction : ", end='')
    print(trans, end='\n\n')



def main():
    i = 0
    print('\n')
    print("Table de traduction : ", end='')
    print(trans)
    print_matrix(i)
    while len(matrix) != 1:
        x, y = select_min() 
        reduce_matrix(x, y)
        update_trans(x, y)
        i = i + 1
        print_matrix(i)
    tree = ''.join(c for c in str(trans) if c not in '[]') + ";"
    t=Tree(tree)
    print(t)
 

main()
