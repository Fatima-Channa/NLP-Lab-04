import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

#Define the sample input corpus
corpus = [
    "The product performance is amazing and fast",
    "The service was fast and performance was great",
    "Terrible customer service and bad performance"
]

#Create CountVectorizer with English stop words removed
vectorizer = CountVectorizer(stop_words='english')

#Fit and transform the corpus
X = vectorizer.fit_transform(corpus)

#Get vocabulary feature names
feature_names = vectorizer.get_feature_names_out()

#Convert to Pandas DataFrame
df_bow = pd.DataFrame(
    X.toarray(),
    columns=feature_names
)

#Display the result
print(df_bow)