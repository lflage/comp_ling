#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random as rd
from tqdm import tqdm


# ## Reading the corpus

# In[2]:


# While reading the corpus we assign a unique id to each word and append it to a list, this list
# corresponds to the document, and we append it to another list which corresponds to our corpus.

with open('../Corpora/movies-pp.txt', 'r') as file:
    docs = file.readlines()[1:]
    
    word_to_id = {}
    id_to_word = {}
    n_docs = []
    id_word = 0
    
    for doc in docs:
        current_doc = []
        
        for word in doc.split():
            #print(word)
            if word in word_to_id:
                current_doc.append(word_to_id[word])
            else:
                current_doc.append(id_word)
                word_to_id[word] = id_word
                id_to_word[id_word] = word
                id_word +=1
        n_docs.append(current_doc)

# Transforming the documents into a list of word ids will make it easier to access the word
# and it's topic assignment in Z
    
vocab = set([word for doc in docs for word in doc.split()])
l_vocab = len(vocab)
doc_n = len(docs)


# In[3]:


# Initial Parameters

alpha = 0.02
beta = 0.1
iter_n = 500
topic_n = 20


# In[4]:


# Matrix with dimension W x T, contains the number of times the word w is assigned to topic t
C_wt = np.zeros([l_vocab, topic_n]) 

# Matrix with dimentions D x T, contains the number times a topic t appears in document d
C_dt = np.zeros([doc_n, topic_n])

# column vector N_z contains the number of times a topic occurs
N_z = np.zeros([topic_n])

# Z is the topic assignments for all tokens. Each key corresponds to a document, its value is 
# a list of topic assignments for the document key.
Z = {}

# A dict with the documents length. It is initialized with values to be used in the sampling phase.
# Its the denominator of the theta element of the Gibbs sampling formula
doc_size = {}


# In[5]:


# Random initialization of topics

for i_doc, doc in tqdm(enumerate(n_docs)):
    current_doc = []
    for word in doc:
        # Generate a random topic
        k = rd.randrange(topic_n)
        
        # Appending the topic to the current doc
        current_doc.append(k)
        
        # Incrementing the count of topic occurance
        N_z[k] += 1
        
        # Incrementing the count of word with topic
        C_wt[word, k] += 1
        
        # Incrementing the count of topic in document
        C_dt[i_doc, k] += 1
        
    # appending the doc to dict Z
    Z[i_doc] = current_doc
    # appending the theta denominator
    doc_size[i_doc] = (len(current_doc)-1)+topic_n*alpha


# In[6]:


# Summing the constants to the matrices

C_wt = C_wt + beta
C_dt = C_dt + alpha
N_z = N_z + l_vocab * beta


# In[ ]:


for i in tqdm(np.arange(iter_n)):
    for i_doc, doc in tqdm(enumerate(n_docs)):
        current_doc_size = doc_size[i_doc]
        
        for i_word, word in enumerate(doc):
            assigned_topic = Z[i_doc][i_word]
            # Subtracting counts
            C_wt[word, assigned_topic] -= 1
            C_dt[i_doc, assigned_topic] -= 1
            N_z[assigned_topic] -= 1
        
            # Calculating probability distribution
            top = C_wt[word,:]*C_dt[i_doc,:]
            botton = N_z * current_doc_size
            p = top/botton
            # The new topic is sampled from an np.array with range topic_n,
            # which every position of this array receives a probability p to be sampled.
            new_topic = np.random.choice(a=topic_n,p=p/p.sum())
           
            # updating the new counts
            Z[i_doc][i_word] = new_topic
            C_wt[word, new_topic] += 1
            C_dt[i_doc,new_topic] += 1
            N_z[new_topic] += 1                                            


# In[ ]:


# Saving the resulting matrix
np.save('./C_wt.npy', C_wt)


# In[ ]:


# Importing saved result

with open('./C_wt.npy','rb') as file:
    temp_wt = np.load(file)


# In[ ]:


# Finding the most frequent words

most_freq_words = []
for topic in range(topic_n):
    # argsort gives us the indexes of the sorted elements in ascending order.
    # To get the highest numbers we multiply the matrix by -1, this way the sm
    most_freq_ids = (-temp_wt[:,topic]).argsort()[:15]
    # print(most_freq_ids)
    c_most_freq_words = []
    for ix in most_freq_ids:
        c_most_freq_words.append(id_to_word[ix])
    most_freq_words.append(c_most_freq_words)


# In[ ]:


import pandas as pd

df = pd.DataFrame(most_freq_words).T
print(df.head(30))

df.to_csv('./most_freq_words.csv')


