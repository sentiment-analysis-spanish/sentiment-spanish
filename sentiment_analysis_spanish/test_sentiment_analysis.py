import unittest
from sentiment_analysis import SentimentAnalysisSpanish

class TestSentimentAnalysis(unittest.TestCase):
        
    def test_sum(self):
        sentiment = SentimentAnalysisSpanish()
        test_sentences_positive = ["prados bellos y alegres a mi alrededor, felicidad, viva la vida", "me encantan los gatos y cantar, disfruto mucho", "que buena noticia me alegro"]

        test_sentences_negative = ["estoy muy enfadado y molesto y no quiero hablar", "me parece terrible esto que me estás diciendo", "fuera de aquí no quiero verte"]

        for text in test_sentences_positive:
            print(text)
            sentiment_result = sentiment.sentiment(text)
            print(sentiment_result)
            print("--------")
            self.assertGreater(sentiment_result, 0.5, "Sentiment should be possitive")
        
        for text in test_sentences_negative:
            print(text)
            sentiment_result = sentiment.sentiment(text)
            print(sentiment_result)
            print("--------")
            self.assertLess(sentiment_result, 0.5, "Sentiment should be negative")



if __name__ == '__main__':
    unittest.main()