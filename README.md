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


SVM outperformed among all the 3 models so we will use it further. 
---

## SVM Evaluation

### Classification Report

| Class | Precision | Recall | F1-Score | Support |
|--------|----------:|-------:|---------:|--------:|
| Negative | 0.79 | 0.63 | 0.70 | 430 |
| Neutral | 0.54 | 0.12 | 0.19 | 226 |
| Positive | 0.88 | 0.98 | 0.93 | 2344 |

**Overall Accuracy:** **86.60%**

---

### Confusion Matrix

| Actual \ Predicted | Negative | Neutral | Positive |
|-------------------|---------:|--------:|---------:|
| **Negative** | 271 | 14 | 145 |
| **Neutral** | 37 | 26 | 163 |
| **Positive** | 35 | 8 | 2301 |

---

### Key Observations

- **Linear SVM** achieved an overall **accuracy of 86.60%**, outperforming Logistic Regression (85.13%) and Naive Bayes (78.13%).
- The model classified **Positive** reviews very effectively, achieving an **F1-score of 0.93** and **98% recall**.
- Performance on the **Neutral** class was comparatively lower because neutral reviews often contain language that overlaps with positive or negative sentiments.

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
streamlit run sentiment_analysis_app.py
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
