# 🏥 AI Triage Assistant (Gemini + FastAPI)

This is a minimal FastAPI service that uses **Gemini Pro (via Google Generative AI)** to recommend the most relevant hospital department based on patient info (gender, age, and symptoms).

---

## 🚀 Features

- ✅ Endpoint: `POST /recommend`
- ✅ Accepts: patient JSON input
- ✅ Uses Gemini 1.5 Flash (or any Gemini model)
- ✅ Returns department suggestion (e.g., "Neurology")

---

## 📦 Requirements

- Python 3.8+
- Google API Key from [https://makersuite.google.com/app/apikey](https://makersuite.google.com/app/apikey)

---

## 🔧 Installation

```bash
git clone <your-repo-url>  # or unzip the folder
cd triage_llm

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
🔑 Setup
Create a .env file with your Google API key:

env
Copy
Edit
GOOGLE_API_KEY=your-gemini-api-key-here
▶️ Run the App
bash
Copy
Edit
uvicorn main:app --reload
Then open your browser and go to:

http://localhost:8000/docs

🧪 Example Request
Endpoint:
bash
Copy
Edit
POST /recommend
Sample Body:
json
Copy
Edit
{
  "gender": "female",
  "age": 62,
  "symptoms": ["pusing", "mual", "sulit berjalan"]
}
Sample Response:
json
Copy
Edit
{
  "recommended_department": "Neurology"
}
📁 Project Structure
bash
Copy
Edit
triage_llm/
├── main.py                # FastAPI logic
├── llm_agent.py           # Gemini prompt logic
├── requirements.txt       # Dependencies
├── .env                   # Your Gemini API key
└── README.md              # This file
🤖 Model Note
The app uses gemini-1.5-flash by default.

You can change this in llm_agent.py:

python
Copy
Edit
model = genai.GenerativeModel("gemini-1.5-pro")  # or other
✅ Done!
This app helps medical staff route patients faster and more accurately using AI.

Feel free to improve it with:

LLM caching

LangChain or vector-based memory

Full frontend