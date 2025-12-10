💬 ArthSakhi – Financial Literacy Chatbot for Women (India)

Empowering women with financial knowledge, government schemes, budgeting tips, and fraud awareness — built using Streamlit and Groq AI models. [web:36][web:31]
---

 🌟 Features

- 💰 "Financial Literacy Support" — Ask questions about budgeting, saving, debt, investments, and more.
- 🏦 "Government Schemes Lookup" — See state‑specific schemes for women entrepreneurs and SHGs, powered by `state_schemes.csv`.
- 📊 "Budgeting Tips" — Simple, practical suggestions for saving and tracking expenses.
- 🚨 "Fraud Awareness" — Learn safe UPI, net banking, and digital payment habits.
- 🤖 "AI‑Powered Chat" — Uses Groq’s Llama 3.1 model (OpenAI‑compatible API) for fast, smart responses. [web:36]
- 🌐 "Multilingual Support" — UI and answers available in:
  - English, हिन्दी (Hindi), मराठी (Marathi)
  - தமிழ் (Tamil), తెలుగు (Telugu), ગુજરાતી (Gujarati)
  - ಕನ್ನಡ (Kannada), বাংলা (Bengali)
- 🎙 "Optional Voice Input" — Microphone recording via `streamlit-mic-recorder`, with hooks to plug in Speech‑to‑Text.

---

 🧩 Tech Stack

| Component | Tool |
|----------|------|
| Frontend | Streamlit |
| Backend  | Python |
| AI Model | Groq (Llama 3.1, OpenAI‑compatible chat completions) [web:36] |
| Data     | CSV (`state_schemes.csv` for state government schemes) |
| Voice    | `streamlit-mic-recorder` (browser mic recording) [web:23][web:25] |

---

 📁 Project Structure


FINANCIAL LITERACY CHATBOT/
│
├── app.py              Main chatbot app (includes TRANSLATIONS dict)
├── state_schemes.csv   CSV of Indian state schemes (optional, has a fallback)
├── requirements.txt    Python dependencies
└── README.md           Documentation (this file)



---

 ⚙ Setup Instructions (Local)

 1️⃣ Install Python

Make sure "Python 3.8+" is installed.
python --version


 2️⃣ Install Required Packages

From your project folder:
pip install -r requirements.txt
Minimum `requirements.txt`:
streamlit
requests
pandas
deep-translator
streamlit-mic-recorder


---

 🔑 Configure Groq API Key
ArthSakhi uses Groq’s OpenAI‑compatible Chat Completions endpoint. [web:36]

 A. Local (`.streamlit/secrets.toml`)
Create a folder `.streamlit` in the project root and inside it a file `secrets.toml`:
GROQ_API_KEY = "your_groq_api_key_here"
In `app.py`, the key is read as:


GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"


You can generate an API key from the Groq console. [web:36]

---

 🚀 Run the Chatbot Locally

From the project folder:


streamlit run app.py
You’ll see something like:
Local URL: http://localhost:8501


Open that URL in your browser to use ArthSakhi. [web:34]

---

 🌐 Deploying on Streamlit Community Cloud

1. Push this project to a "GitHub repo".
2. Go to "https://share.streamlit.io" and click "“New app”". [web:32]
3. Select your repository, branch (e.g., `main`), and `app.py` as the entrypoint.
4. Click "Deploy".

 Set Secrets on Streamlit Cloud

In your deployed app:

1. Open "⋮ → Settings → Secrets".
2. Add:


GROQ_API_KEY = "your_groq_api_key_here"


3. Save and "Rerun" the app.

---

 🗃 Optional: State Schemes CSV

Create a file named `state_schemes.csv` in the same folder as `app.py`:


state,scheme,description
Maharashtra,Mahila Arthik Vikas,Interest subsidy on SHG loans up to ₹5 lakhs
Karnataka,Stree Shakti,Microenterprise grants for women SHGs
Tamil Nadu,Mahalir Thittam,Skill and credit support for rural women
Delhi,Women Welfare Loan Scheme,Financial support for small business women
Gujarat,Sakhi Mandal,Support for women self-help groups


If the file is missing, the app automatically falls back to a small in‑code default DataFrame with similar sample data.

---

 🎙 Voice Input (Optional)

The app supports microphone recording via `streamlit-mic-recorder`. [web:23][web:25]

- The component records audio in the browser.
- Your code integrates it with a text input “draft” so you can later plug in a Speech‑to‑Text (STT) backend (e.g., Whisper via Groq or other providers).
- Once STT is wired, the transcript will appear in the text input box, and the user can edit and send it like a normal chat message.

Make sure the browser has microphone permission enabled for your app URL.

---

 🧠 How the Chat Works (High Level)

1. User asks a question (typed or via voice → text).
2. If the selected language is not English:
   - The question is translated to English using `deep_translator`. [web:10][web:8]
3. The English prompt is sent to Groq’s chat completion endpoint (`llama-3.1-8b-instant`). [web:36]
4. The model’s English reply is optionally translated back to the user’s selected language.
5. Both question and answer are appended to `st.session_state.messages` and rendered in a chat‑style UI.

---

 🛡 Privacy & Disclaimer

- Conversations are stored only in the current Streamlit session (`st.session_state`) and are not persisted to an external database in this version.
- ArthSakhi provides "educational" financial information and general guidance only.
- It is "not" a substitute for professional financial, legal, or tax advice.
- Users should verify scheme details and financial decisions with official government sources or certified advisors.

---

 🧭 Future Improvements

- Connect recorded audio to a production‑grade STT API and fully automate voice → text.
- Add richer scheme metadata (eligibility, links, documents).
- Support user profiles and personalized financial journeys.
- Add analytics and feedback (with proper privacy and consent).

---

Made with ❤️ using Streamlit and Groq to support financial literacy for women in India.
