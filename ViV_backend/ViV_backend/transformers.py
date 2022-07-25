import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint

# nltk
import nltk

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess

# spacy for lemmatization
import spacy
from nltk.corpus import stopwords

class Transformer:
    def __init__(self, bio):
        self.nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        self.bio = bio
        self.stopwords = stopwords.words('english')


    def sent_to_words(self):
        temp_list = []
        for sentence in self.bio:
            temp_list.append( simple_preprocess(str(sentence), deacc=True))
        self.list = temp_list
        # return temp_list

    def remove_stopwords(self):
        self.updated_list = [[word for word in simple_preprocess(str(doc)) if word not in self.stopwords] for doc in self.list]

    def lemmatization(self, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in self.updated_list:
            doc = self.nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        self.texts_out= texts_out

    def to_corpus(self):
        id2word = corpora.Dictionary(self.texts_out)
        corpus =  id2word.doc2bow(self.bio[0].split())
        return corpus


if __name__ == '__main__':
    transformer = Transformer(["looking for someone to scroll endlessly through netflix. Or to yell out songs at the nearest karaoke. I enjoy cooking, travelling, singing, karaoke, gaming."])
    transformer.sent_to_words()
    transformer.remove_stopwords()
    transformer.lemmatization()
    print(transformer.to_corpus())
