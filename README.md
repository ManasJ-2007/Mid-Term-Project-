# Mid-Term-Project-
Midterm Project submission of WIDS
# Midterm Chatbot Assignment – Analytics Club

This repository contains solutions for the **midterm checkpoint chatbot assignment** issued by the Analytics Club.  
The objective was to design simple chatbots that demonstrate state handling, time-based logic, and basic conversational behavior using Python.

---

## 📁 Repository Contents

midterm-chatbots/
├── counterbot.py
├── timebot.py
├── app.py
└── README.md

---

## 🧠 Problem Statements Covered

### 1. Counter-Based Quiz Chatbot (`counterbot.py`)
- Maintains a counter for the number of user queries.
- Once the counter reaches **5**, the bot initiates a quiz.
- The quiz question is chosen **randomly from the last 5 queries**.
- After the quiz, the counter and stored queries are reset.

### 2. Time-Based Quiz Chatbot (`timebot.py`)
- Stores each user query along with the time it was asked.
- After **10 minutes**, the bot quizzes the user about that specific query.
- Time tracking is done using Python’s `time` module.

### 3. Simple Chatbot (`app.py`)
- A basic rule-based chatbot inspired by the Week-2 tutorial.
- Uses conditional logic to generate responses.
- Demonstrates the fundamental input–response chatbot loop.

---

## 🛠 Technologies Used
- Python 3
- Standard libraries:
  - `random`
  - `time`

---

## ▶️ How to Run

Run each file independently using:

```bash
python counterbot.py
python timebot.py
python app.py
