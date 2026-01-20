# 🤖 FAQ Chatbot (CodeAlpha Task 2)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-lightgrey?style=for-the-badge&logo=flask&logoColor=black)
![NLTK](https://img.shields.io/badge/NLTK-NLP-green?style=for-the-badge&logo=python&logoColor=white)

A simple, intelligent **FAQ Chatbot** built for the **CodeAlpha Internship (Task 2)**. 
It uses Natural Language Processing (**NLP**) techniques like **TF-IDF** and **Cosine Similarity** to answer user queries based on a predefined dataset.

---

## 🚀 Features
- **Intelligent Matching**: Uses Cosine Similarity to find the most relevant answer.
- **NLP Pipeline**: Implements tokenization, stopword removal, and vectorization.
- **Clean UI**: A modern, responsive chat interface using HTML, CSS, and Vanilla JS.
- **No External APIs**: Runs 100% offline using `scikit-learn` and `nltk`.

## 🛠️ Tech Stack
- **Backend**: Python (Flask)
- **Machine Learning**: Scikit-learn (TF-IDF Vectorizer, Cosine Similarity)
- **NLP**: NLTK (Tokenization, Stopwords)
- **Frontend**: HTML5, CSS3, JavaScript

## 📂 Project Structure
```bash
chat_project/
├── static/
│   ├── style.css       # Chat UI Styling
│   └── script.js       # Frontend Logic (Fetch API)
├── templates/
│   └── index.html      # HTML Structure
├── app.py              # Flask Backend & NLP Logic
├── requirements.txt    # Dependencies
└── README.md           # Documentation
```

## ⚙️ How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/faq-chatbot.git
cd faq-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the App
```bash
python app.py
```
*Wait for a few seconds on the first run as it downloads NLTK data.*

### 4. Open in Browser
Visit: `http://127.0.0.1:5000`

## 🧠 How It Works
1. **Input**: User sends a specific question (e.g., "Is it paid?").
2. **Preprocessing**: Text is lowercased, punctuation removed, and tokenized.
3. **Vectorization**: The `TfidfVectorizer` converts the text into numbers.
4. **Similarity Check**: We compute the **Cosine Similarity** between the user input and known FAQs.
5. **Response**: If the similarity score > 0.2, the best answer is returned. Otherwise, it asks to rephrase.

## 📝 Sample Questions to Try
- "What is this internship?"
- "Is this a paid program?"
- "How do I submit my work?"
- "Where is the company located?"

---
**Developed by [Your Name] for CodeAlpha Internship.**
