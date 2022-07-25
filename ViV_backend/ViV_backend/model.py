import pickle
from re import M
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy
import gensim.models as models
import nltk

from transformers import Transformer

class Model:
    def __init__(self) -> None:
        self.model = pickle.load('ViV_backend/data/optimal_model_45score.pkl','rb')

    def predict(self, text):
        self.transformer = Transformer([text])
        self.transformer.sent_to_words()
        self.transformer.remove_stopwords()
        self.transformer.lemmatization()
        temp_data = self.transformer.to_corpus()
        model_predictor = models.wrappers.ldamallet.malletmodel2ldamodel(self.model, gamma_threshold=0.001, iterations=50)
        return model_predictor[temp_data]


if __name__ == '__main__':
    model = Model()
    model.predict('')
