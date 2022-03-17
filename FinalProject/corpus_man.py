import re
#import spacy
import lxml
from unicodedata import normalize


#def spacy_loader():
#    nlp = spacy.load('pt_core_news_lg')
#    return nlp

def remove_acentos(text):
    '''Remove os acentos da string "text". Usada somente na função pre_process
    '''
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')


def pre_process(text):
    '''Pre process the input string 'text' by setting it to lowercase, removing
    excess whitestace, removes non word characters and removes accent marks
    '''
    text = re.sub(r'\W+|\d+',' ', text)
    text = re.sub(r'\s{2,}',' ',text).strip().lower()
    text = ' '.join([token for token in text.split() if len(token)>2])           
    return text

def get_meta(data, tree):
    """ Retrieves metadata from the parsed xml tree. Returns a string containing the corresponding
    metadata information.
    :data: string with the name of the metadata to be retrieved
    :tree: lxml parse tree object
    """
    parsed = tree

    n_list = parsed.xpath('//meta/n')
    n_text = [i.text for i in n_list]
    index_meta = n_text.index(data)

    v_list = parsed.xpath('//meta/v')
    meta = v_list[index_meta]
    return meta

