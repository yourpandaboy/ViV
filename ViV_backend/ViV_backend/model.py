import pickle
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
import spacy
import gensim.models as models
import nltk

from transformers import Transformer
class Model:
    def __init__(self) -> None:
        self.model = pickle.load('ViV_backend/data/optimal_model_45score.pkl','rb')
        nltk.download('stopwords')

    def predict(self, text):
        model_predictor = models.wrappers.ldamallet.malletmodel2ldamodel(self.model, gamma_threshold=0.001, iterations=50)
