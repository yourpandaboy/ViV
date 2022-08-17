import nltk
from nltk.corpus import stopwords

class Stopwords:
    def __init__(self):
        nltk.download('stopwords')

    def activate_stopwords(self):
        self.stopwords = stopwords.words('english')
        return self.stopwords

if __name__ == '__main__':
    stopwords = Stopwords().activate_stopwords()
    print(stopwords)
