import numpy as np
import random as rd
from tqdm import tqdm

class LDA:
    def __init__(self, path,alpha=0.02, beta=0.1,Ntopic=20):
        self.path = path
        self.alpha = alpha
        self.beta = beta
        self.Ntopic = Ntopic
        
    def readCorpus(self):
        with open(self.path, 'r') as file:
            docs = file.readlines()
    
            word_to_id = {}
            id_to_word = {}
            docsList = []
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
                docsList.append(current_doc)
                
        self.vocabSize = len(id_to_word)
        self.docsList = docsList
        self.id2word = id_to_word
        self.word2id = word_to_id

    def initMatrices(self):
        # Initialing the matrices
        print("Initializing matrices")
        # Matrix with dimension W x T, contains the number of times the word w is assigned to topic t
        self.Cwt = np.zeros([self.vocabSize, self.Ntopic]) 

        # Matrix with dimentions D x T, contains the number times a topic t appears in document d
        self.Cdt = np.zeros([len(self.docsList), self.Ntopic])

        # column vector Nz contains the number of times a topic occurs
        self.Nz = np.zeros([self.Ntopic])

        # Z is the topic assignments for all tokens. Each key corresponds to a document, its value is 
        # a list of topic assignments for the document key.
        self.Z = {}

        # A dict with the documents length. It is initialized with values to be used in the sampling phase.
        # Its the denominator of the theta element of the Gibbs sampling formula
        self.docSize = {}
    
    
        # Random Topic Initialization
        print("Initializing topics for each word")
        
        for i_doc, doc in tqdm(enumerate(self.docsList)):
            current_doc = []
            for word in doc:
                # Generate a random topic
                k = rd.randrange(self.Ntopic)
            
                # Appending the topic to the current doc
                current_doc.append(k)
        
                # Incrementing the count of topic occurance
                self.Nz[k] += 1
        
                # Incrementing the count of word with topic
                self.Cwt[word, k] += 1
        
                # Incrementing the count of topic in document
                self.Cdt[i_doc, k] += 1
        
            # appending the doc to dict Z
            self.Z[i_doc] = current_doc
            # appending the theta denominator
            self.docSize[i_doc] = (len(current_doc)-1)+self.Ntopic*self.alpha

        
    def runIter(self,nIter=500):
        self.nIter = nIter
            
        # Summing the constants to the matrices
        self.Cwt = self.Cwt + self.beta
        self.Cdt = self.Cdt + self.alpha
        self.Nz = self.Nz + self.vocabSize * self.beta
        
        for i in tqdm(np.arange(self.nIter)):
            for i_doc, doc in tqdm(enumerate(self.docsList)):
                current_doc_size = self.docSize[i_doc]
            
                for i_word, word in enumerate(doc):
                    assigned_topic = self.Z[i_doc][i_word]
                    # Subtracting counts
                    self.Cwt[word, assigned_topic] -= 1
                    self.Cdt[i_doc, assigned_topic] -= 1
                    self.Nz[assigned_topic] -= 1
        
                    # Calculating probability distribution
                    top = self.Cwt[word,:]*self.Cdt[i_doc,:]
                    botton = self.Nz * current_doc_size
                    p = top/botton
                    # The new topic is sampled from an np.array with range Ntopic,
                    # which every position of this array receives a probability p to be sampled.
                    new_topic = np.random.choice(a=self.Ntopic,p=p/p.sum())
           
                    # updating the new counts
                    self.Z[i_doc][i_word] = new_topic
                    self.Cwt[word, new_topic] += 1
                    self.Cdt[i_doc,new_topic] += 1
                    self.Nz[new_topic] += 1
                    
        self.Cwt = self.Cwt - self.beta
        self.Cdt = self.Cdt - self.alpha
        self.Nz = self.Nz - self.vocabSize * self.beta
    
    def classifyDocuments(self):
        self.docsTopic = {}
        for i in range(len(self.docsList)):
            currRow = self.Cdt[i,:]
            self.docsTopic[i] = np.where(currRow == np.amax(currRow))[0]
    
    def getDocTopic(self,index):
        return self.docsTopic[index]
        
    def saveCwt(self,path='./Cwt.npy'):
        np.save(path, self.Cwt)
    
    def saveCdt(self,path='./Cdt.npy'):
        np.save(path,self.Cdt)
    
    def mostFreqWordsTopic(self,n):
        most_freq_words = []
        for topic in range(self.Ntopic):
                # argsort gives us the indexes of the sorted elements in ascending order.
                # To get the highest numbers we multiply the matrix by -1, this way the sm
            most_freq_ids = (-self.Cwt[:,topic]).argsort()[:n]
            c_most_freq_words = []
            for ix in most_freq_ids:
                c_most_freq_words.append(self.id2word[ix])
            most_freq_words.append(c_most_freq_words)
        return most_freq_words
    
