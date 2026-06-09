from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faqs = {
    "What is AI?": "AI is the simulation of human intelligence by machines.",
    "What is Machine Learning?": "Machine Learning is a subset of AI."
}

questions = list(faqs.keys())
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(questions)

while True:
    q = input("You: ")
    qv = vectorizer.transform([q])
    idx = cosine_similarity(qv, X).argmax()
    print("Bot:", faqs[questions[idx]])
