import unittest
from sentiment_analysis import SentimentAnalysisSpanish

class TestSentimentAnalysis(unittest.TestCase):
        
    def test_sum(self):
        sentiment = SentimentAnalysisSpanish()
        test_sentences_positive = ["me encanta la tombola",
                                   "me gusta la tombola es genial",
                         "la tombola es genial",
                         "esto es precioso, muy bonito",
                         "me encanta, bello"]

        test_sentences_negative = ["¡Jamás voy a usar esta maldita aplicación!  No funciona para nada.",
                                    "me desagrada profundamente",
                                    "no me gusta",
                                    "la tombola no me encanta",
                                    "la tombola no es genial, no me gusta",
                                    "esto no es precioso no es bonito",
                                    "todo muy feo y desagradable",
                                    "me perece muy triste lo que está ocurriendo"
                                    "que tristeza, qué pena",
                                    "estoy muy enfadado y molesto y no quiero hablar",
                                    "me parece terrible esto que me estás diciendo",
                                    "fuera de aquí no quiero verte"]

        for text in test_sentences_positive:
            print(text)
            sentiment_result = sentiment.sentiment(text)
            print(sentiment_result)
            print("--------")
            #self.assertGreater(sentiment_result, 0.5, "Sentiment should be possitive")
        
        for text in test_sentences_negative:
            print(text)
            sentiment_result = sentiment.sentiment(text)
            print(sentiment_result)
            print("--------")
            #self.assertLess(sentiment_result, 0.5, "Sentiment should be negative")



if __name__ == '__main__':
    unittest.main()