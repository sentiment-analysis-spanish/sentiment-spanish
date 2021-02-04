


from sklearn.metrics import confusion_matrix, f1_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

import re
import bz2
import _pickle as cPickle
from pathlib import Path
REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^\w\s]')

def compressed_pickle(title, data):
    with bz2.BZ2File(title + '.pbz2', 'w') as f:
        cPickle.dump(data, f)

def decompress_pickle(file):
    data = bz2.BZ2File(file, 'rb')
    data = cPickle.load(data)
    return data

class SentimentAnalysisSpanish:
    def __init__(self):
        self.parent_path = Path(__file__).parent
        self.vectorizer = decompress_pickle(str(self.parent_path / 'saved_model/ngram_vectorized_compressed.pbz2'))
        self.classifier = decompress_pickle(str(self.parent_path / 'saved_model/classifier_naive_bayes_compressed.pbz2'))

    def clean_text(self, text):
        text = text.lower()
        text = self.REPLACE_BY_SPACE_RE.sub(' ',text)
        text = self.BAD_SYMBOLS_RE.sub('', text)
        return text

    #returns the sentiment of a text string
    def sentiment(self, text:str):
        vals = self.vectorizer.transform([text])
        return self.classifier.predict_proba(vals)[0][1]
