# sentiment-spanish


[![PyPI version](https://badge.fury.io/py/sentiment_analysis_spanish.svg)](https://badge.fury.io/py/sentiment_analysis_spanish)

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
0
```