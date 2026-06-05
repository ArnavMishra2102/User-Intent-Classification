import pandas as pd
import pickle

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Load dataset
df = pd.read_csv("dataset.csv")

# Input and output
X = df["text"]
y = df["intent"]

# ML pipeline
model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("classifier", LogisticRegression())
])

# Train model
model.fit(X, y)

# Save model
with open("intent_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained and saved successfully!")