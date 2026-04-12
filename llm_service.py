import os
import json
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "llama-3.3-70b-versatile"


def generate_question(topic):
    prompt = f"""
You are a strict viva examiner.

Ask ONE conceptual viva question about: {topic}

Rules:
- Only one question
- No explanation
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
    )

    return response.choices[0].message.content.strip()


def evaluate_answer(answer):
    prompt = f"""
You are a strict AI viva examiner.

Evaluate this answer:

"{answer}"

Return ONLY JSON:
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

    content = response.choices[0].message.content.strip()

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