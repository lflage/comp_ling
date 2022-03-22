import re
import lxml
import pandas as pd
from unicodedata import normalize



def remove_acentos(text):
    """Remove graphical accents from "text" string
    :text: string
    """
    return normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')


def pre_process(text):
    """Pre process the input string 'text' by setting it to lowercase, removing
    excess whitestace, removes non word characters and removes accent marks
    :text: string object to be processed
    """
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

def confusionMatrix(df):
    """ Function used to create a new dataframe where the indexes are the initial tags from the periodos_tycho.csv
    file and the colum is the predicted topic for the LDA model.
    :df: :Pandas Dataframe Object: dataframe containing the
    """
    confusion_matrix = pd.DataFrame(0,
                                    index=['arcmed','mod','cont'],
                                    columns=range(len(df['predicted_period'].unique())))
    for index in range(len(df)):
        initial = df['period'][index]
        predicted = df['predicted_period'][index]
        confusion_matrix[predicted][initial] += 1
    return confusion_matrix

def removeMime(to_slice):
    """Removes the last 4 characters of a string. Used to remove files extensions from file names.
    :to_slice: string - string to have its last characters removed
    """
    return to_slice[:-4]

