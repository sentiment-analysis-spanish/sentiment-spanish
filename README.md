# sentiment-spanish


[![PyPI version](https://badge.fury.io/py/sentiment_analysis_spanish.svg)](https://badge.fury.io/py/sentiment_analysis_spanish)

# How does it work?

sentiment-spanish is a python library that uses convolutional neural networks to predict the sentiment of spanish sentences. The model was trained using over *800000* reviews of users of the pages *eltenedor, decathlon, tripadvisor, filmaffinity and ebay*.
This reviews were extracted using web scraping with the project [opinion-reviews-scraper](https://github.com/sentiment-analysis-spanish/opinion-reviews-scraper)

Using the rate in the user reviews we trained the model to learn from the language in them. For that we use the libraries Keras and Tensorflow. We achieved a validation accuracy (accuracy over fresh data, no used for training) of 88%.
For more details regarding the training of the neural network model check the repo [sentiment-analysis-model-neural-network](https://github.com/sentiment-analysis-spanish/sentiment-analysis-model-neural-network) 

# Why?

I believe there are not many solutions to sentiment analysis **in spanish** based on neural networks.


# Install and use

First to install the package

```
pip install sentiment-analysis-spanish
```

You will also need keras and tensorflow

```
pip install keras tensorflow
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
1
```
For instance if you use the text 

```
sentiment = sentiment_analysis.SentimentAnalysisSpanish()
print(sentiment.sentiment("me parece terrible esto que me estás diciendo"))

```

you will see that it outputs 

```
9.460418e-14s
```

which as you see is very close to 0.

## Output and meaning
The function ``sentiment(text)`` returns a number between 0 and 1. This is the probability of string variable  ``text`` of being "positive". Low probabilities mean that the text is negative (numbers close to 0), high probabilities (numbers close to 1) mean that the text is positive. The space in between corespond to neutral texts.