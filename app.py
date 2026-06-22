import streamlit as st
import pickle
import re
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')

# Load Model and Vectorizer
with open("sentiment_model.pkl", "rb") as file:
    model = pickle.load(file)

with open("tfidf_vectorizer.pkl", "rb") as file:
    tfidf = pickle.load(file)

# Stopwords
stop_words = set(stopwords.words('english'))

# Text Cleaning Function
def clean_text(text):

    text = str(text).lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-zA-Z\s]", "", text)

    words = text.split()

    words = [word for word in words if word not in stop_words]

    return " ".join(words)

# Page Config
st.set_page_config(
    page_title="Sentiment Analysis System",
    page_icon="💬",
    layout="centered"
)

# Title
st.title("💬 Social Media Sentiment Analysis")
st.markdown("### NLP Project using TF-IDF and Logistic Regression")

st.markdown("---")

# Input
user_text = st.text_area(
    "Enter a comment or review:",
    height=150
)

# Predict Button
if st.button("Analyze Sentiment"):

    if user_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        cleaned_text = clean_text(user_text)

        vector = tfidf.transform([cleaned_text])

        prediction = model.predict(vector)[0]

        sentiment_labels = {
            0: "Negative 😞",
            1: "Neutral 😐",
            2: "Positive 😊"
        }

        result = sentiment_labels[prediction]

        st.success(f"Predicted Sentiment: {result}")

st.markdown("---")

st.markdown(
    """
    **Dataset:** Sentiment Analysis Dataset (241K+ Records)

    **Algorithm:** Logistic Regression

    **Feature Extraction:** TF-IDF Vectorization

    **Accuracy:** 79.5%

    **Developed By:** Bhupinder Sandhu
    """
)