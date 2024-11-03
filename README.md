# Computational Linguistics Assignments Repository

Repository created to hold code developed at the Computational Linguistics Lecture at the Universität des Saarlandes. This repository contains a series of assignments and project files covering topics such as Zipf's Law, n-grams, pointwise mutual information (PMI), Markov models, part-of-speech tagging, syntactic parsing, word alignment, topic modeling, and more.

## Folder Structure

```
.
├── Assignment_1
│   ├── 1_zips_law
│   │   └── Zipf's Law.ipynb
│   ├── 2_n_grams
│   │   ├── n_gram.ipynb
│   │   └── ngram.py
│   ├── 3_pmi
│   │   └── PMI.ipynb
│   └── README.md
├── Assignment_2
│   └── Part-of-speech tagging with HMMs.ipynb
├── Assignment_3
│   └── CKY Parser.ipynb
├── Assignment_4
│   ├── LSTM_PosTagger.ipynb
│   └── README.md
├── Assignment_5
│   ├── IBM_Model1
│   │   ├── IBM_Model1_align.py
│   │   └── IBM_Model1.py
│   └── README.md
├── Assignment_6
│   └── my_lda_np.ipynb
├── Corpora
│   ├── de-utb
│   ├── junglebook.txt
│   ├── SETIMES.bg-tr.bg
│   └── SETIMES.bg-tr.tr
├── FinalProject
│   ├── Diachronic_LDA.ipynb
│   └── README.md
├── README.md
```

## Contents

### [Assignment 1](./Assignment_1)
- **Zipf's Law**: Empirical verification of Zipf's law using three different corpora:
    - King James Bible
    - The Jungle Book
    - SETIMES Turkish-Bulgarian Parallel Newspaper Text
- **N-grams Generation**: Reimplementation of the "Dissociated Press" with n-gram generation from a probability distribution.
- **PMI Score**: Calculation of Pointwise Mutual Information (PMI) Score to test the independence assumption, often applied to phenomena inaccurately modeled as independent.

### [Assignment 2](./Assignment_2)
- **Markov Chain POS Tagging**: Implementation of part-of-speech tagging using a Markov chain approach with Hidden Markov Models.

### [Assignment 3](./Assignment_3)
- **CKY Parser**: Implementation of the CKY algorithm for syntactic parsing of sentences.

### [Assignment 4](./Assignment_4)
- **POS Tagger with PyTorch**: Sequence labeling using an LSTM neural network for POS tagging, implemented with PyTorch.

### [Assignment 5](./Assignment_5)
- **Word Alignments (IBM Model 1)**: Scripts implementing IBM Model 1 for word alignment in bilingual corpora.

### [Assignment 6](./Assignment_6)
- **Latent Dirichlet Allocation with Numpy**: Implementation of Latent Dirichlet Allocation (LDA) from scratch using NumPy.

### [Final Project](./FinalProject)
- **LDA Performance on Grouping Diachronic Data**: Analysis of LDA model performance in grouping topics over diachronic data.

### [Corpora](./Corpora)
Contains various text corpora used across assignments, including tokenized texts in multiple languages.

## License

This project is licensed under the MIT License.

## Acknowledgments

This repository was developed as part of a computational linguistics course at the Universität des Saarlandes, covering various techniques in natural language processing and statistical modeling.
