import argparse

parser = argparse.ArgumentParser(description=
        'Creates human readable alignments for word alignments generated for the hansards corpus')

parser.add_argument('-idx', type=int, default=0, help=
        'Index of the sentence in the Hansards Corpus' )
parser.add_argument('-a_path', type=str,
        help='Path to Alignments file ')
parser.add_argument('--f_path', type=str, default='./hw2/data/hansards.f',
        help='Optional path for the foreign corpus')
parser.add_argument('--e_path', type=str, default='./hw2/data/hansards.e',
        help='Optional path for the source corpus')

args = parser.parse_args()

# Reaind the 
with open(args.f_path, 'r') as file:
    f_sent = file.readlines()[args.idx]

with open(args.e_path, 'r') as file:
    e_sent = file.readlines()[args.idx]

with open(args.a_path, 'r') as file:
    a_sent = file.readlines()[args.idx]

# Printing the selected sentences
print('Foreign sentence:')
print(f_sent)
print('Source sentence:')
print(e_sent)
print('Alignments:')
print(a_sent)

# Spliting the sentences into lists
f_sent = f_sent.split()
e_sent = e_sent.split()
a_sent = a_sent.split()

# Iterates over the alignments file and translates the indexes into words
# from the original files
hr_aligns = []
for aligns in a_sent:
    i_idx, j_idx = aligns.split('-')
    hr_aligns.append(f_sent[int(i_idx)]+'-'+e_sent[int(j_idx)])
print('Human Readable Alignments:')
print(' '.join(hr_aligns))

