import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pprint import pprint

# nltk
import nltk
nltk.download('stopwords')

# Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess

# spacy for lemmatization
import spacy


class Transformer:
    def __init__(self, bio):
        self.nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
        self.bio = bio

    def sent_to_words(self):
        for sentence in self.bio:
            yield(gensim.utils.simple_preprocess(str(sentence), deacc=True))

    def lemmatization(self, texts, allowed_postags=['NOUN', 'ADJ', 'VERB', 'ADV']):
        """https://spacy.io/api/annotation"""
        texts_out = []
        for sent in texts:
            doc = self.nlp(" ".join(sent))
            texts_out.append([token.lemma_ for token in doc if token.pos_ in allowed_postags])
        return texts_out

    def remove_stopwords(self, texts):
        return [[word for word in simple_preprocess(str(doc)) if word not in stop_words] for doc in texts]

    def to_corpus(self, texts):
        id2word = corpora.Dictionary(texts)
        corpus =  id2word.doc2bow(self.bio['text'][0].split())
        return corpus


if __name__ == 'main':
    transformer = Transformer(pd.DataFrame({'text':["lets see here i have a lot of things going on in my life so i guess there is just too much to really say.  i'm just a fun loving person who works and works and studies and works a lot so yea i do need a little bit of time to have fun with new people once and a while and all lol"]})
)
    print(transformer.sent_to_words())
