
import json

path_to_model = './p_f_e.dict'
path_to_foreign = './hw2/data/hansards.f'
path_to_english = './hw2/data/hansards.e'
with open(path_to_model) as file:
    p_f_e = json.loads(file.read())

with open (path_to_foreign, 'r') as file:
    f_sentences = file.readlines()

with open (path_to_english, 'r') as file:
    e_sentences = file.readlines()

aligns = []

for n_f, n_e in zip(f_sentences, e_sentences):

    align = []
    f = n_f.split()
    for f_word in f:
        best_prob = 0
        best_j = 0
        
        
        
        e = n_e.split()
        e.insert(0,'NULL')
        for e_word in e:
            key = f_word+'#'+ e_word
            current_prob = p_f_e[key]
            if current_prob > best_prob:
                best_prob = current_prob
                best_j = e.index(e_word)
            
        align.append(str(f.index(f_word))+str(best_j))
    aligns.append(align)

with open('./model1.a','w') as file:
    for align in aligns:
        file.write(' '.join(align))
        file.write('\n')


