# 🚀 User Intent Classification System

A Machine Learning and NLP-based application that predicts a user's intent from text queries and automatically routes requests to the appropriate support department.

Inspired by real-world customer support systems used by companies to automate ticket classification and routing.

---

## 📖 Overview

Customer support teams often receive thousands of requests daily. Manually identifying and routing each request can be time-consuming and inefficient.

This project uses Natural Language Processing (NLP) and Machine Learning to classify user queries into predefined intents such as:

- Payment Failed
- Refund Request
- Cancel Subscription
- Billing Issue
- Account Verification
- Card Issue
- Fraud Issue
- Technical Issue
- General Support

The predicted intent is then automatically mapped to the appropriate support department.

---

## 🎯 Features

✅ Real-time intent prediction

✅ NLP-based text processing

✅ TF-IDF feature extraction

✅ Logistic Regression classifier

✅ Automatic department routing

✅ Interactive Streamlit interface

✅ Lightweight and easy to deploy

---

## 🛠️ Tech Stack

- Python
- Pandas
- Scikit-Learn
- Streamlit
- Pickle
- NLP (TF-IDF)

---

## 🧠 How It Works

### Step 1: User enters a query

Example:

```text
My payment failed during checkout
```

### Step 2: TF-IDF Vectorization

The text is converted into numerical features using TF-IDF.

### Step 3: Intent Classification

The Logistic Regression model predicts the most likely intent.

Output:

```text
Payment Failed
```

### Step 4: Department Routing

The system routes the query to:

```text
Payments Support Team
```

---

## 📂 Project Structure

```text
User-Intent-Classification/
│
├── app.py
├── train_model.py
├── dataset.csv
├── intent_model.pkl
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/your-username/User-Intent-Classification.git
```

### Move to Project Directory

```bash
cd User-Intent-Classification
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Train the Model

```bash
python train_model.py
```

This creates:

```text
intent_model.pkl
```

which stores the trained machine learning model.

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

Open:

```text
http://localhost:8501
```

in your browser.

---

## 📊 Machine Learning Pipeline

```text
User Query
    ↓
TF-IDF Vectorization
    ↓
Logistic Regression
    ↓
Intent Prediction
    ↓
Department Routing
```

---

## 📈 Example Predictions

| User Query | Predicted Intent |
|------------|------------------|
| My payment failed | Payment Failed |
| I want a refund | Refund Request |
| Cancel my subscription | Cancel Subscription |
| My card is not working | Card Issue |
| Website is showing an error | Technical Issue |

---

## 💡 Future Improvements

- BERT-based intent classification
- Confidence score prediction
- Live prediction while typing
- Support for multiple languages
- Integration with customer support platforms
- Support ticket priority prediction
- Dashboard for analytics and monitoring

---

## 🎓 Learning Outcomes

Through this project, I gained hands-on experience with:

- Natural Language Processing (NLP)
- Text Vectorization using TF-IDF
- Classification using Logistic Regression
- Streamlit application development
- Model serialization using Pickle
- End-to-end Machine Learning workflow

---

## 👨‍💻 Author

**Arnav**

Computer Science Engineering Student  
SRM Institute of Science and Technology

---

## ⭐ If you found this project useful, consider giving it a star!
