import argparse
import re

parser = argparse.ArgumentParser(description='Creates a file that can be used as input for the fast aligner.')

parser.add_argument('--f_path', type=str, default='../hw2/data/hansards.f',
        help='Optional path for foreign sentences')
parser.add_argument('--e_path', type=str, default='../hw2/data/hansards.e',
        help='Optional path for source language')
parser.add_argument('--paralelized',type=str, default='./fast_paralelized',
        help='Optional path for fast_text input file')

args = parser.parse_args()
with open(args.e_path, 'r') as file:
    e_sents = file.readlines()
with open(args.f_path,'r') as file:
    f_sents = file.readlines()

with open(args.paralelized, 'w') as file:
    for f, e in zip(f_sents, e_sents):
        f = re.sub('\n','',f)
        e = re.sub('\n','',e)
        file.write(f + ' ||| ' + e)
        file.write('\n')

