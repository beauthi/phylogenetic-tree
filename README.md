# PyPgt

Phylogenetic tree creation program in Python 3.6.3 using ete3.

## Description

This project is a command-line program to visualize phylogenetic trees creation.
For the moment, two building agorithms are available :
* [UPGMA](https://en.wikipedia.org/wiki/UPGMA)
* [WPGMA](https://en.wikipedia.org/wiki/WPGMA)

## Installation

Place the folder wherever you want in your filesystem, and from root folder launch the following commands:

```
pip3 install -r requirements.txt
echo "alias pypgt=$PWD/src/phylo.py >> ~/.bashrc"
```

## Using

```
pypgt option file
```

### Options available

* -u : UPGMA method
* -w : WPGMA method

## Miscellaneous

If you spot issues or suggestions, please write it in the issues or email me : thibaut.passilly@epita.fr
Thank you.
