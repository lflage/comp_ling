import argparse, pickle
from my_lda import LDA

parser = argparse.ArgumentParser(description=
        'uses')
parser.add_argument('-nTopics', type=int, default=20, help=
        'number of topics to assign to LDA' )
parser.add_argument('-path', type=str,
        help='Path to input txt file ')
parser.add_argument('-nIter', type=int, default=500,
        help='Number of GibbsSampling iterations')

args = parser.parse_args()

with open(args.path+'.out', 'wb') as file:
    lda = LDA(args.path,Ntopic=args.nIter)
    lda.readCorpus()
    lda.initMatrices()
    lda.runIter(args.nIter)
    pickle.dump(lda, file)





with open(args.path+'.out', 'wb') as file:
    pickle.dump(lda, file)