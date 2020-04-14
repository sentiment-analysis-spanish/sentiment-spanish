
from cleaner import Cleaner
from keras.preprocessing.sequence import pad_sequences
from keras.models import model_from_json
import pickle
from pathlib import Path

class SentimentAnalysisSpanish:
    def __init__(self):
        self.cleaner = Cleaner()
        self.maxlen = 500
        self.tokenizer = None
        self.parent_path = Path(__file__).parent

        with open(self.parent_path / 'saved_model/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)

        # load json and create model
        json_model_keras = open(self.parent_path / 'saved_model/model.json', 'r')
        loaded_model_json = json_model_keras.read()
        json_model_keras.close()
        self.loaded_model = model_from_json(loaded_model_json)

        # load weights into new model
        self.loaded_model.load_weights(self.parent_path / "saved_model/model.h5")

        # evaluate loaded model on test data
        self.loaded_model.compile(optimizer='adam', loss='mean_squared_error',  metrics=['mae','accuracy'])

    #returns the sentiment of a text string
    def sentiment(self, text:str):
        x = self.tokenizer.texts_to_sequences([self.cleaner.clean_text(text)])
        x = pad_sequences(x, padding='post', maxlen=self.maxlen)

        y_new = self.loaded_model.predict(x)
        return y_new [0][0]