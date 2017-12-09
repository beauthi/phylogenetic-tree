from ete3 import Tree
from sys import stderr
from gmpy import is_square
from math import sqrt

import sys

PARAMETERS = {
        '-u' : False, # wpgma
        '-w' : False, # upgma
        }

matrix = []

trans = []

def make_matrix(l):
    width = int(sqrt(len(l)))
    global matrix, trans
    matrix = []
    for i in range(0, len(l), width):
        try:
            sublist = list(map(int, l[i:i + width]))
        except:
            error("Values must be integers", 10)
        matrix.append(sublist)
    trans = [c for c in [chr(x + ord('a')) for x in range(len(matrix))]]


def read_file(f):
    try:
        r = None
        with open(f, "r") as content:
            r = content.read()
        r = [c for c in r.replace('\n', ' ').split() if c != '']
        if not is_square(len(r)):
            error(str(f) + " input is not a square", 5)
        make_matrix(r)
        return r
    except Exception as e:
        error(e.strerror, 4)

def error(err, code):
    print("Error : " + str(err), file=stderr)
    exit(code)

def check_integrity(): 
    width = len(matrix)
    for l in matrix:
        if len(l) != width:
            error("Input is not a square matrix.", 1)
    for i, l in enumerate(matrix):
        if int(l[i]) != 0:
            error("Diagonal values must be zeros.", 2)
        i = i + 1

    for i, l in enumerate(matrix):
        for j, elt in enumerate(l):
            if matrix[j][i] != matrix[i][j]:
                error("Matrix must be symmetric.", 3)

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
    if PARAMETERS['-u']:
        line_length = len(trans[x])
        col_length = len(trans[y])
    else:
        line_length = 1
        col_length = 1

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
    global trans
    pair = trans[x], trans[y]
    del trans[x], trans[y - 1 if y > 0 else 0]
    trans.insert(0, pair)
    print("Nouvelle table de traduction : ", end='')
    print(trans, end='\n\n')


def parse_parameters(argv):
    args = argv[1:]
    for i in range(0, len(args)):
        try:
            PARAMETERS[args[i]]
            break
        except KeyError:
            error(args[i] + " argument doesn't exist. You must use :\n-u : UPGMA method\n-w : WPGMA method", 6)

    for parameter in PARAMETERS:
        if parameter in args:
            PARAMETERS[parameter] = True
            args.pop(args.index(parameter))

    if not any(x for x in PARAMETERS.values()):
        error("You must specify a method to use", 7)

    if all(PARAMETERS.values()):
        error("You must specify only one method :\n-u : UPGMA method\n-w: WPGMA method", 8)

    if len(args) == 0:
        error("You must specify at least one file", 9)

    return args


def print_tree(f):
    read_file(f)
    check_integrity()
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
    print('')
    print("###############")
    print("  Final tree")
    print("###############")
    print(t)


def main():
    files = parse_parameters(sys.argv)
    for f in files:
        print_tree(f)
 

main()
