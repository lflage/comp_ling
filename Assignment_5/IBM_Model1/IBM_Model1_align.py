
import json
import argparse
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Process inputs.')

parser.add_argument('--n_sents', type=int, default=100000, help=
        'Number of sentences to be read from the Hansards Corpus')
parser.add_argument('--path_to_model', default='./p_f_e.dict', type=str,
        help='Optional path to pre trained probabilities model')
parser.add_argument('--f_path', default='../data/hansards.f',type=str,
        help='Optional path for the foreign corpus')
parser.add_argument('--e_path', default='../data/hansards.e',type=str,
        help='Optional path for the source corpus')
parser.add_argument('--a_path', default='./model1.a',type=str,
        help='Optional path for the alignemnts file')

args = parser.parse_args()

n_sents = args.n_sents
path_to_model = args.path_to_model
f_path = args.f_path
e_path = args.e_path
a_path = args.a_path


# Loading the dictionary with the probabilities of a word in a foreign language
# given a word in English.
with open(path_to_model) as file:
    p_f_e = json.loads(file.read())

# Loads the sentences in the foreign language and treats it as a list of 
# sentences.
with open (f_path, 'r') as file:
    f_sentences = file.readlines()[:n_sents]

# Loads the sentences in the source language and treats it as a list of
# sentences.
with open (e_path, 'r') as file:
    e_sentences = file.readlines()[:n_sents]

aligns = []

print('Searching for best alignments')
for n_f, n_e in tqdm(zip(f_sentences, e_sentences)):

    align = []
    f = n_f.split()
    for f_word in f:
        best_prob = 0
        best_j = 0
        
        e = n_e.split()
        
        for e_word in e:
            key = f_word+'ß'+ e_word
            current_prob = p_f_e[key]
            if current_prob > best_prob:
                best_prob = current_prob
                best_j = e.index(e_word)
            
        align.append((str(f.index(f_word)),str(best_j)))
    aligns.append(align)

with open(a_path,'w') as file:
    print('Writing alignments to file')
    for sentence in aligns:
        for align in sentence:
            file.write(align[0]+'-'+align[1])
            file.write(' ')
        file.write('\n')


