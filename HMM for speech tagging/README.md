# Do "part of speech tagging'" with HMM 

This is a homework project, aiming to do part of speech of tagging with a python module called `pomegranate`.

Here **Part of speech tagging** is the process of determining the syntactic category of a word from the words in its surrounding context.  

## Prerequisite

- System: windows 10 or Linux
- Package: Python 3.6 with module `pomegranate`, `jupyter notebook`

##  How to use

`HMM warmup (optional).ipynb` is a prewritten file used to understand how to do baisc HMM inference with module  `pomegranate`.

`HMM Tagger.ipynb` is the main book for doing part of  speech tagging with HMM. In this notebook, a basic method called MFC is done first.  Then HMM is done afterwards.  

For more informaton, please take a look at the 2 books. 

Generally,  the output of HMM is better than MFC. Because HMM takes more correlations of words  into accounts than MFC does.

## Issue

- Under Windows 10, the testing result on the last cell of book `HMM Tagger.ipynb` is something wrong, due to some IT issue. I haven't figure it out yet.

