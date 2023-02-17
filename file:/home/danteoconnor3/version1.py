from google.cloud import language
import pandas as pd

data = pd.read_csv("all-data.csv", encoding="ISO-8859-1")

data2 = data.columns[1]


def analyze_text_sentiment(text):
    client = language.LanguageServiceClient()
    document = language.Document(content=text, type_=language.Document.Type.PLAIN_TEXT)

    response = client.analyze_sentiment(document=document)

    sentiment = response.document_sentiment
    results = dict(
        text=text,
        score=f"{sentiment.score:.1%}",
        magnitude=f"{sentiment.magnitude:.1%}",
    )
    for k, v in results.items():
        print(f"{k:10}: {v}")

text = "Guido van Rossum is great!"
analyze_text_sentiment(text)
