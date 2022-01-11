import json
from tqdm import tqdm

path_to_model = './p_f_e.dict'
path_to_foreign = './hw2/data/hansards.f'
path_to_target = './hw2/data/hansards.e'
path_to_aligns_file = './model1.a'


# Loading the dictionary with the probabilities of a word in a foreign language
# given a word in English.
with open(path_to_model) as file:
    p_f_e = json.loads(file.read())

# Loads the sentences in the foreign language and treats it as a list of 
# sentences.
with open (path_to_foreign, 'r') as file:
    f_sentences = file.readlines()

# Loads the sentences in the target language and treats it as a list of
# sentences.
with open (path_to_target, 'r') as file:
    e_sentences = file.readlines()

# List to contain all alignments
aligns = []

# Iterating over two lists of sentences
# n_f, n_e: type List
print('Searching for best alignments')
for n_f, n_e in tqdm(zip(f_sentences, e_sentences)):

    align = []
    # Spliting the string of foreign words
    f = n_f.split()
    for f_word in f:
        best_prob = 0
        best_j = 0
        
        e = n_e.split()
        e.insert(0,'NULL')
        for e_word in e:
            key = f_word+'ß'+ e_word
            try:
                current_prob = p_f_e[key]
                if current_prob > best_prob:
                    best_prob = current_prob
                    best_j = e.index(e_word)
            
            except KeyError:
                print(key)
           # if current_prob > best_prob:
           #     best_prob = current_prob
           #     best_j = e.index(e_word)
            
        align.append(str(f.index(f_word))+str(best_j))
    aligns.append(align)

with open('./model1.a','w') as file:
    print('Writing alignments to file')
    for sentence in aligns:
        for align in sentence:
             file.write('-'.join(align))
             file.write(' ')
        file.write('\n')

print('Done')
