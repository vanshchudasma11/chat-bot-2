import nltk
from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import string

# Download necessary NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    # For newer NLTK versions, we might need punkt_tab which is distinct from punkt
    nltk.download('punkt_tab')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

app = Flask(__name__)

# 1. FAQ Dataset (Stored in a list for simplicity)
faqs = [
    {
        "question": "What is this internship program about?",
        "answer": "This internship program is designed to provide hands-on experience in software development, data science, and web technologies."
    },
    {
        "question": "How long is the internship?",
        "answer": "The internship duration is typically 4 weeks, but it can vary based on the specific track."
    },
    {
        "question": "Is this a paid internship?",
        "answer": "This is an unpaid, educational internship focused on skill development and project completion."
    },
    {
        "question": "What technologies will I learn?",
        "answer": "You will work with Python, Web Development (HTML/CSS/JS), and potentially Machine Learning libraries depending on your domain."
    },
    {
        "question": "How do I submit my tasks?",
        "answer": "Tasks are submitted via GitHub. You will need to create a repository and share the link in the submission form."
    },
    {
        "question": "Can I get a certificate after completion?",
        "answer": "Yes, upon successful completion of all assigned tasks, you will receive a certificate of completion."
    },
    {
        "question": "Who can I contact for help?",
        "answer": "You can reach out to the mentors via the dedicated Discord server or email the support team."
    },
    {
        "question": "What are the working hours?",
        "answer": "The internship is flexible. You can work at your own pace as long as you meet the weekly deadlines."
    },
    {
        "question": "Do I need prior experience?",
        "answer": "Basic knowledge is recommended, but the program is beginner-friendly and learning resources are provided."
    },
    {
        "question": "Where is the company located?",
        "answer": "We are a remote-first organization, so you can work from anywhere!"
    }
]

# extract questions for vectorization
questions = [faq['question'] for faq in faqs]

# 2. MATCHING LOGIC
# Initialize user_question global to be used for matching
# But simpler: we will just compute similarity on the fly.
# We need to preprocess questions first ? 
# Actually TfidfVectorizer handles a lot, but let's do custom implementation as requested.

def preprocess_text(text):
    # Lowercasing
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Tokenization
    tokens = word_tokenize(text)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return " ".join(filtered_tokens)

# Preprocess all FAQ questions
preprocessed_questions = [preprocess_text(q) for q in questions]

# Vectorize once at startup
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_questions)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    if not user_message:
        return jsonify({"answer": "Please say something!"})

    # Preprocess user message
    processed_user_message = preprocess_text(user_message)
    
    # Vectorize user message
    user_vector = vectorizer.transform([processed_user_message])
    
    # Calculate cosine similarity
    similarities = cosine_similarity(user_vector, tfidf_matrix)
    
    # Find best match
    best_match_index = similarities.argmax()
    best_match_score = similarities[0, best_match_index]
    
    # Threshold for "I don't understand"
    if best_match_score < 0.2: # Adjustable threshold
        return jsonify({"answer": "Sorry, I don't understand your question. Could you rephrase it?"})
    else:
        return jsonify({"answer": faqs[best_match_index]['answer']})

if __name__ == '__main__':
    app.run(debug=True)
