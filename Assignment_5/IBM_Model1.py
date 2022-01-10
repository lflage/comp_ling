from tqdm import tqdm
import json

# Number of sentences to be used
n_sents = 1000
# Number of iterations to be done
iter_n = 5
# Path to sabe probabilities dictionaty
path_to_dict = './p_f_e.dict'

with open('./hw2/data/hansards.f','r') as file:
    f_sentences = file.readlines()[:n_sents]

with open('./hw2/data/hansards.e','r') as file:
    e_sentences = file.readlines()[:n_sents]

# Creating a dict of word pairs french-english as key and probability as value
# The zero_dict is defined with the same keys as the p_f_e dict but with zeroes
# for the values. It will be used later to define a dictionary for the count of
# word pais seem on the data.

p_f_e = {}
zero_dict = {}

for n_f, n_e, in zip(f_sentences, e_sentences):
    for i in n_f.split():
        p_f_e[i+'#'+'NULL'] = 1/n_sents
        zero_dict[i+'#'+'NULL'] = 1/n_sents
        for j in n_e.split():
            key = i+'#'+j
            p_f_e[key] = 1/n_sents
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
                Z[i] = Z[i] + p_f_e[i+'#'+j]
            for j in e:
                # Expected counts
                c = p_f_e[i+'#'+j]/Z[i]
                counts[i+'#'+j] += c
           
                if j in word_marg_count:
                    word_marg_count[j] += c
                else:
                    word_marg_count[j] = c

        # M-Step: Normalize
    for key in p_f_e:
    	# The marginal count
        v = word_marg_count[key.split('#')[1]]
        p_f_e[key] = counts[key]/v


with open(path_to_dict,'w') as file:
    file.write(json.dumps(p_f_e))
    
