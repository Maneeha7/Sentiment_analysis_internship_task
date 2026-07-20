# Amazon Review Sentiment Analysis

## Project Overview

This project predicts the sentiment of Amazon product reviews using Machine Learning and Natural Language Processing (NLP).

The application was developed using Python, Scikit-learn, TF-IDF Vectorization, and Support Vector Machine (SVM). A Streamlit web application is provided for real-time sentiment prediction.

---

## Features

- Data Cleaning
- Text Preprocessing
- Data Analysis
- TF-IDF Vectorization
- Logistic Regression
- Naive Bayes
- Support Vector Machine (Best Model)
- Streamlit Web Application

---

## Dataset

Amazon Fine Food Reviews
# you can download here
https://www.kaggle.com/datasets/snap/amazon-fine-food-reviews
I analyzed the data with 15000 rows.

Labels:
- Positive
- Neutral
- Negative

---

## Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- Streamlit
- Joblib

---

## Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | 85.1% |
| Naive Bayes | 78.1% |
| Support Vector Machine | 86.6% |

---

## Project Structure

```
sentiment_analysis.ipynb
app.py
requirements.txt
README.md
svm_sentiment_analysis_model.pkl
tfidf_vectorizer.pkl
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run

```bash
streamlit run app.py
```

---

## Sample Predictions

Input:
```
This product is amazing.
```

Prediction:
```
Positive
```

Input:
```
Worst purchase ever.
```

Prediction:
```
Negative
```

Input:
```
The product is okay.
```

Prediction:
```
Neutral
```
