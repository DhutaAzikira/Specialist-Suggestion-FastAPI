import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash")

def get_department_recommendation(info: dict) -> str:
    prompt = f"""
You are a medical triage assistant. Based on the following patient info, recommend the most relevant hospital department.

Patient Info:
- Gender: {info['gender']}
- Age: {info['age']}
- Symptoms: {", ".join(info['symptoms'])}

Just reply with the department name only (e.g. "Neurology"). Don't add any explanation.
"""

    response = model.generate_content(prompt)
    return response.text.strip()
