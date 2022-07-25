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


class Transformer:
    def __init__(self, bio):
        nltk.download('stopwords')
        self.nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        self.bio = bio

    def sent_to_words(self):
        empty_list = []
        for sentence in self.bio:
            empty_list.append(gensim.utils.simple_preprocess(str(sentence), deacc=True))
        return empty_list

    def remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    def lemmatization(self, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = self.nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    def to_corpus(self, texts):
        id2word = corpora.Dictionary(texts)
        corpus =  id2word.doc2bow(self.bio['text'][0].split())
        return corpus


if __name__ == '__main__':
    transformer = Transformer(["looking for someone to scroll endlessly through netflix. Or to yell out songs at the nearest karaoke. I enjoy cooking, travelling, singing, karaoke, gaming."])
    print(transformer.sent_to_words())
