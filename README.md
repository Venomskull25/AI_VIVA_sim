# AI_VIVA Simulater 

##  Overview

AI_VIVA Simulater is an AI-powered system designed to simulate viva (oral examination) environments. It generates topic-based questions, evaluates user answers, and provides real-time feedback with scores and improvement suggestions.

The system uses advanced AI techniques such as Natural Language Processing (NLP) and Large Language Models (LLMs) to create an intelligent and adaptive learning experience.

---

##  Features

* 🔹 Dynamic question generation based on topic
* 🔹 AI-based answer evaluation
* 🔹 Real-time scoring and feedback
* 🔹 Adaptive questioning (difficulty adjusts based on performance)
* 🔹 User-friendly web interface
* 🔹 Personalized learning experience

---

##  Tech Stack

**Frontend:**

* HTML
* CSS
* JavaScript

**Backend:**

* FastAPI (Python)

**AI Model:**

* Groq LLaMA 3.3 70B

**API Integration:**

* Groq API

---

##  Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-viva-simulater.git
cd ai-viva-simulater
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # for Linux/Mac.
venv\Scripts\activate      # for Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Add Environment Variables

Create a `.env` file and add:

```env
GROQ_API_KEY=your_api_key_here
```

### 5. Run Backend Server

```bash
uvicorn app.main:app --reload
```

### 6. Open Frontend

Open `index.html` in your browser.

---

##  How It Works.

1. User enters a topic
2. System generates a question using AI
3. User submits answer
4. System evaluates response using NLP + LLM
5. Score and feedback are displayed
6. Next question is generated adaptively

---

##  Output Example

**Input Topic:** Machine Learning

**Question:** What is supervised learning?

**User Answer:** It is a type of machine learning

**Output:**

* Score: 6/10
* Feedback: Basic definition provided
* Suggestion: Add examples and explanation

---

##  Applications

* Viva exam preparation
* Technical interview practice
* Self-learning and revision
* Educational platforms (LMS integration)

---

##  Limitations

* Depends on API availability
* May produce slightly inconsistent evaluations
* Requires internet connection

---

##  Future Scope

* Voice-based viva interaction
* Multi-language support
* Performance analytics dashboard
* Integration with LMS platforms

---

##  Author

* Sarvesh Dhanrale

---

##  License

This project is for academic purposes.

---
