# sentiment-spanish


[![PyPI version](https://badge.fury.io/py/sentiment_analysis_spanish.svg)](https://badge.fury.io/py/sentiment_analysis_spanish)

# LAST VERSION CHANGES:
From version 0.0.25 we no longer use tensorflow. The model is now based on Naive Bayes classifier.

# How does it work?

sentiment-spanish is a python library that uses Naive Bayes classification to predict the sentiment of spanish sentences. The model was trained using over *800000* reviews of users of the pages *eltenedor, decathlon, tripadvisor, filmaffinity and ebay*.
This reviews were extracted using web scraping with the project [opinion-reviews-scraper](https://github.com/sentiment-analysis-spanish/opinion-reviews-scraper)

Using the rate in the user reviews we trained the model to learn from the language in them. We achieved a validation accuracy (accuracy over fresh data, no used for training) of 90%.
For more details regarding the training of the neural network model check the repo [sentiment-analysis-model-neural-network](https://github.com/sentiment-analysis-spanish/sentiment-analysis-model-neural-network) 

# Why?

I believe there are not many solutions to sentiment analysis **in spanish** based on neural networks.


# Install and use

First to install the package

```
pip install sentiment-analysis-spanish
```


Import the package

```
from sentiment_analysis_spanish import sentiment_analysis

```

run the sentiment analysis:

```
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("me gusta la tombola es genial"))

```

you will see that it outputs 

```
0.9304396176531412
```
For instance if you use the text 

```
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("me parece terrible esto que me estás diciendo"))

```

you will see that it outputs 

```
2.1830853580533075e-06
```

which as you see is very close to 0.

## Output and meaning
The function ``sentiment(text)`` returns a number between 0 and 1. This is the probability of string variable  ``text`` of being "positive". Low probabilities mean that the text is negative (numbers close to 0), high probabilities (numbers close to 1) mean that the text is positive. The space in between corespond to neutral texts.