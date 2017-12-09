# PyPgt

Phylogenetic tree creation program in Python 3.6.3 using ete3.

## Description

This project is a command-line program to visualize phylogenetic trees creation.

For the moment, two building agorithms are available :
* [UPGMA](https://en.wikipedia.org/wiki/UPGMA)
* [WPGMA](https://en.wikipedia.org/wiki/WPGMA)

## Installation

Place the folder wherever you want in your filesystem, and from the root of the project launch the following commands:

```
pip3 install -r requirements.txt
echo "alias pypgt=python3 $PWD/src/phylo.py" >> ~/.bashrc
```

## Using

```
pypgt option file
```

### Input format

Input files contain the distance matrix between species that are being analyzed.

These files may be of any extension, content must be formatted this way :
```
0 1 2
1 0 3
2 3 0
```

### Available options

* -u : UPGMA method
* -w : WPGMA method

### Error codes

* 0 : no error
* 1 : input file doesn't contain a square matrix;
* 2 : matrix doesn't contain a diagonal of zeros;
* 3 : matrix isn't a distance matrix (check [the ref.](https://en.wikipedia.org/wiki/Distance_matrix))
* 4 : I/O error (input file doesn't exist)
* 5 : matrix is not square
* 6 : invalid argument
* 7 : method not specified (UPGMA, WPGMA...)
* 8 : two or more methods specified
* 9 : no file specified
* 10 : values in matrix are not integers

## Miscellaneous

If you spot issues or suggestions, please write it in the issues or email me at thibaut.passilly@epita.fr

Thank you.
