from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Define documents and query
documents = [
    "Machine learning algorithms analyze structured data effectively",
    "Deep learning and neural networks excel at processing unstructured data",
    "Natural language processing helps computers understand human language",
    "Python is widely used for machine learning and data science"
]

query = ["machine learning algorithms for data"]

#Fit CountVectorizer on documents and transform documents and query
vectorizer = CountVectorizer()

doc_vectors = vectorizer.fit_transform(documents)
query_vector = vectorizer.transform(query)

#Compute cosine similarity
similarity_scores = cosine_similarity(
    query_vector,
    doc_vectors
).flatten()

#Rank documents from highest similarity to lowest
ranked_docs = sorted(
    list(enumerate(similarity_scores)),
    key=lambda x: x[1],
    reverse=True
)

#Display ranked documents
print("Ranked Documents:")

for idx, score in ranked_docs:
    print(f"Score: {score:.4f} | Document: {documents[idx]}")