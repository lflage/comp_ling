# LDA Performance on Diacrhonic Corpora

This repository was created to contain code relevant to the final project in the Computational Linguistics programm WiSe 21/22 at the Universiät des Saarlandes

# Dependencies  

python                    3.9.7  
lxml                      4.6.3   
pandas                    1.3.4  
numpy                     1.20.3  
tqdm                      4.62.3  

# Tree Structure
```
.
├── corpus_man.py
├── Diachronic_LDA.ipynb
├── lda_cli.py
├── lda_out.zip
├── my_lda.py
├── periodos_tycho.csv
└── README.md
```

# How to Run

The main file is the Jupyter Notebook ```Diachronic_LDA.ipynb```. By running this file you are able to reproduce the results.  

The corpus is however not provided here, there is a cell in the notebook which will download the corpus (approximately 80MB) and create the folder structure for the next cells. It is necessary to run this cell in order to reproduce the results fully.  

The ```my_lda.py``` file us module which is imported in the main notebook and contains the code for the LDA with Gibbs Sampling. It is an improved version of the code provided in Assignment 6.  

The ```lda_cly.py``` file is a CLI for running the experiments, it was used to create multiple sessions on the university servers and run the experiments more efficiently. It is not necessary to run these experiments again, they are carefully placed in the notebook but not run.

```corpus_man.py``` is a python file contaning functions used inside the notebook, it was done in this way to improve readability.

```periodos_tycho.csv``` is a file containing a manual tagging performed by the author. It consists of two columns, one with the file name, and another with the corresponding time period according to Bechara's classification.

# Running Times

No relevant running times.
