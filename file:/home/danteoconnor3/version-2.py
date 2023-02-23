from google.cloud import language
from google.cloud import language_v1
import six
import pandas as pd

data = pd.read_excel("solar-city.xlsx")

data.columns = ['text']

def analyze_sentiment(content):

    client = language_v1.LanguageServiceClient()

    if isinstance(content, six.binary_type):
        content = content.decode("utf-8")

    type_ = language_v1.Document.Type.PLAIN_TEXT
    document = {"type_": type_, "content": content}

    response = client.analyze_sentiment(request={"document": document})
    sentiment = response.document_sentiment
    print("Score: {}".format(sentiment.score))
    print("Magnitude: {}".format(sentiment.magnitude))

for x in range(20):
    val = data.loc[x].at['text']  #stores the data at that point in val
    print(val)
    analyze_sentiment(val)
    print('\n')   