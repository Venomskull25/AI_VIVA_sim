import os
import json
from groq import Groq
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Model name
MODEL = "llama-3.3-70b-versatile"


def generate_question(topic):
    prompt = f"""
You are a strict viva examiner.

Ask one clear conceptual question about: {topic}

Rules:
- Only ONE question
- No explanation
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content


def evaluate_answer(answer):
    prompt = f"""
You are a strict AI viva examiner.

Evaluate this answer:

"{answer}"

Return ONLY valid JSON:

{{
  "score": number (0-10),
  "feedback": "short feedback",
  "improvement": ["point1", "point2", "point3"]
}}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {
            "score": 6,
            "feedback": "Decent answer but needs clarity.",
            "improvement": [
                "Be more structured",
                "Add examples",
                "Explain clearly"
            ]
        }