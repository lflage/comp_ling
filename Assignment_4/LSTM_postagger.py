import torch
import torch.nn as nn
from torch.nn import functional
from torch.nn import Module
import torch.optim as optim
from torch.utils.data import Dataset, DataLoader
import data

from tqdm import tqdm

##
# Loading the corpus into the following variables
#    train_dataloader        	DataLoader for iterating over the training data
#    dev_dataloader        	DataLoader for iterating over the development data
#    test_dataloader        	DataLoader for iterating over the test data
#    vocabulary            	Vocabulary of words in the sentences in the data
#    tagset                	Vocabulary of POS tags in the data
#    pretrained_embeddings    	Pretrained fasttext word embeddings 
##

train_dataloader,dev_dataloader,test_dataloader,vocabulary,tagset, pretrained_embeddings = data.load(
'corpus/de_gsd-ud-train.conllu',
'corpus/de_gsd-ud-dev.conllu',
'corpus/de_gsd-ud-test.conllu'
)

##
# Print the first sentence of the training data and its POS tags 
##


for minibatch in train_dataloader:
	print('Shape of the batch Tensor objects: {}\n'.format(minibatch.size()))
	print('\nFirst POS Tags:\n')
	print(' '.join(tagset.lookup_tokens(minibatch[0][1].flatten().tolist())))
	print('\nFirst Sentence:\n')
	print(' '.join(vocabulary.lookup_tokens(minibatch[0][0].flatten().tolist())))
	break


