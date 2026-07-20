import streamlit as st
import joblib
import re
import string
import nltk

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# Download required NLTK resources (only needed the first time)
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")

# Load the saved model and vectorizer
load_model = joblib.load(r"C:\Users\TAHIR\Documents\Content_Arcade\svm_sentiment_analysis_model.pkl")
vectorizer = joblib.load(r"C:\Users\TAHIR\Documents\Content_Arcade\tfidf_vectorizer.pkl")

# Initialize NLP tools
stop_words = set(stopwords.words("english"))
stop_words.discard("not")
stop_words.discard("no")
stop_words.discard("nor")
stop_words.discard("never")
lemmatizer = WordNetLemmatizer()


# Text preprocessing function
def preprocess(review):

    # Remove HTML tags
    review = re.sub(r"<.*?>", "", review)

    # Remove URLs
    review = re.sub(r"http\\S+|www\\S+|https\\S+", "", review)

    # Remove punctuation
    review = review.translate(str.maketrans("", "", string.punctuation))

    # Lowercase
    review = review.lower()

    # Tokenize
    tokens = word_tokenize(review)

    # Remove stopwords
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatize
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    return " ".join(tokens)


# -----------------------------
# Streamlit App
# -----------------------------
def main():
    st.title("Amazon Review Sentiment Analysis")
    st.write("Enter a product review below and the model will predict its sentiment.") 
    review = st.text_area("Enter your review")

    if st.button("Predict Sentiment"):

        if review.strip() == "":
            st.warning("Please enter a review.")
        else:

            cleaned_review = preprocess(review)

            review_vector = vectorizer.transform([cleaned_review])

            prediction = load_model.predict(review_vector)[0]

            st.subheader("Prediction")

            if prediction == "Positive":
                st.success("😊 Positive Review")

            elif prediction == "Neutral":
                st.info("😐 Neutral Review")

            else:
                st.error("😞 Negative Review")


import joblib

#model = joblib.load("svm_sentiment_analysis_model.pkl")
#vectorizer = joblib.load("tfidf_vectorizer.pkl")



if __name__ == '__main__':
    main()
