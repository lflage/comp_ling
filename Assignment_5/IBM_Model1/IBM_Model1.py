from tqdm import tqdm
import json
import argparse

parser = argparse.ArgumentParser(description='Creates a dictionary maping the probability of a word on the target corpus occuring given a word on the source corpus using expectation maximization')

parser.add_argument('iter_n', type=int, help=
        'Number of iterations for Expectation Maximization')
parser.add_argument('--n_sents', type=int, default=100000, help=
        'Number of sentences to be used from the Hansards Corpus' )
parser.add_argument('--path_to_dict', type=str, default='./p_f_e.dict',
        help= 'Path to store probabilities dict. Defaults to ./p_f_e.dict')
parser.add_argument('--f_path', type=str, default='../hw2/data/hansards.f',
        help='Optional path for the foreign corpus')
parser.add_argument('--e_path', type=str,default='../hw2/data/hansards.e',
        help='Optional path for the source')

args = parser.parse_args()

# Number of sentences to be used
n_sents = args.n_sents
# Number of iterations to be done
iter_n = args.iter_n
# Path to sabe probabilities dictionaty
path_to_dict = args.path_to_dict
# path to foreign
f_path = args.f_path
# path to source
e_path = args.e_path

# Reading the main files and removing the unused lines 
with open(f_path,'r') as file:
    f_sentences = file.readlines()[:n_sents]

with open(e_path,'r') as file:
    e_sentences = file.readlines()[:n_sents]

# The initialization value of the probabilities dictionary is the lengh of the
# target language vocabulary

p_f_e = {}
zero_dict = {}
e_vocab = set()
for sent in e_sentences:
    e_vocab.update(sent.split())

e_vocab_len = len(e_vocab)

# Creating a dict of word pairs french-english as key and probability as value
# The zero_dict is defined with the same keys as the p_f_e dict but with zeroes
# for the values. It will be used later to define a dictionary for the count of
# word pais seem on the data.

print('Creating Dicts')
for n_f, n_e, in tqdm(zip(f_sentences, e_sentences)):
    for i in n_f.split():
        p_f_e[i+'ß'+'NULL'] = 1/e_vocab_len
        zero_dict[i+'ß'+'NULL'] = 0
        for j in n_e.split():
            key = i+'ß'+j
            p_f_e[key] = 1/e_vocab_len
            zero_dict[key] = 0

# We repeeat this process iter_n times to get the best probabilites
for step in tqdm(range(iter_n)):
    # counts is a dict containg the possible alignment as a key and a 0.
    # It is used to store the expected counts for an alignment
    counts = dict(zero_dict)
    # word_marg_cunt is used to store the expected count for the english word
    word_marg_count = {}
    # Normalization term
    Z = {}
    for n in tqdm(range(n_sents)):
        f = f_sentences[n].split()
        # E-Step: Compute expected counts
        for i in f:
            Z[i] = 0
            e = e_sentences[n].split()
            e.insert(0,'NULL')
            for j in e:
                Z[i] = Z[i] + p_f_e[i+'ß'+j]
            for j in e:
                # Expected counts
                c = p_f_e[i+'ß'+j]/Z[i]
                counts[i+'ß'+j] += c
                # 
                if j in word_marg_count:
                    word_marg_count[j] += c
                else:
                    word_marg_count[j] = c

        # M-Step: Normalize
    for key in p_f_e:
    	# The marginal count
        p_f_e[key] = counts[key]/word_marg_count[key.split('ß')[1]]

# The dictionary is save using the json format
with open(path_to_dict,'w') as file:
    file.write(json.dumps(p_f_e))
    
