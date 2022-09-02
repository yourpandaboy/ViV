import pickle
from re import M
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy
import gensim.models as models
import nltk

from ViV_backend.transformers import Transformer

from ViV_backend.utilities import download_blob

class Model:
    def __init__(self, dl_new = False) -> None:
        #if dl_new:
            #download_blob('viv-data69','ViV_latest.pkl','models/ViV_latest.pkl')
        #self.model = pickle.load(open('../models/ViV_latest.pkl','rb'))

        self.model = pickle.load(open('models/ViV_latest.pkl','rb'))

    def predict(self, text):
        self.transformer = Transformer([text])
        self.transformer.sent_to_words()
        self.transformer.remove_stopwords()
        self.transformer.lemmatization()
        temp_data = self.transformer.to_corpus()
        model_predictor = models.wrappers.ldamallet.malletmodel2ldamodel(self.model, gamma_threshold=0.001, iterations=50)
        return model_predictor[temp_data]


#if __name__ == '__main__':
    #model = Model(dl_new=True)
    #print(model.predict("hey looking for friends here. male or female preferably people who likes to travel and outdoor activities."))
