# 💬 Social Media Sentiment Analysis

A Natural Language Processing (NLP) project that analyzes user comments and predicts whether the sentiment is **Positive**, **Neutral**, or **Negative** using **TF-IDF Vectorization** and **Logistic Regression**.

## 🚀 Live Demo

Add your Streamlit deployment link here:

https://sentimentanalysisproject-x.streamlit.app

---

## 📌 Project Overview

This project uses Natural Language Processing techniques to classify text sentiments from social media comments. The model is trained on a large sentiment analysis dataset containing over **241,000 records**.

The application allows users to enter any comment or review and instantly receive a sentiment prediction.

---

## 🎯 Features

- Predicts sentiment from text input
- Supports:
  - 😊 Positive
  - 😐 Neutral
  - 😞 Negative
- Text preprocessing and cleaning
- TF-IDF feature extraction
- Logistic Regression classifier
- Interactive Streamlit web interface

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- TF-IDF Vectorizer
- Logistic Regression
- Streamlit

---

## 📂 Dataset

**Dataset:** Sentiment Analysis Dataset

- 241,145+ Records
- 3 Sentiment Classes
  - 0 → Negative
  - 1 → Neutral
  - 2 → Positive

Dataset Source:

https://www.kaggle.com/datasets/abdelmalekeladjelet/sentiment-analysis-dataset

---

## ⚙️ Machine Learning Pipeline

1. Data Loading
2. Text Cleaning
3. Stopword Removal
4. TF-IDF Vectorization
5. Train-Test Split
6. Logistic Regression Training
7. Sentiment Prediction

---

## 📊 Model Performance

| Metric | Value |
|----------|----------|
| Algorithm | Logistic Regression |
| Feature Extraction | TF-IDF |
| Accuracy | 79.5% |

---

## 📁 Project Structure

```text
Sentiment_Analysis_Project/
│
├── app.py
├── sentiment_model.pkl
├── tfidf_vectorizer.pkl
├── requirements.txt
├── README.md
└── sentiment_data.csv
```

## ▶️ Run Locally

Clone the repository:

```bash
git clone https://github.com/bhupinder07-sandhu/Sentiment_Analysis_Project.git
```

Move into project directory:

```bash
cd Sentiment_Analysis_Project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 📸 Application Preview

<img width="1470" height="825" alt="Screenshot 2026-06-23 at 1 01 01 AM" src="https://github.com/user-attachments/assets/86f6cb53-40ce-40f6-976b-49221f705be3" />

---

## 👨‍💻 Developer

**Bhupinder Sandhu**

B.Tech AIML Student

---

## 🙏 Acknowledgements

Special thanks to:

- Ducat India
- Trainers and Mentors
- Batchmates and Friends
- Open Source Community

---

⭐ If you found this project useful, please consider giving it a star.
