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
echo "alias pypgt='python3 $PWD/src/phylo.py'" >> ~/.bashrc
```

## Using

```
pypgt <option> <files>
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

* 0  : no error
* 1  : input file doesn't contain a square matrix;
* 2  : matrix doesn't contain a diagonal of zeros;
* 3  : matrix isn't a distance matrix (check [the ref.](https://en.wikipedia.org/wiki/Distance_matrix))
* 4  : I/O error (input file doesn't exist)
* 5  : matrix is not square
* 6 : values in matrix are not integers

## Testing

Example :

```
pypgt -w examples/simple.phgen # examples folder contains testing files, here I use WPGMA method
```
