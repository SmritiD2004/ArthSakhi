# test_groq.py
import requests

# NOTE: For this test to work, you MUST hardcode your key here, 
# or load it via a standard environment variable (e.g., os.environ).
# It WILL NOT load from Streamlit's secrets.toml.
GROQ_API_KEY = "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" # Your key here
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"
GROQ_MODEL = "llama-3.1-8b-instant"

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json",
}

payload = {
    "model": GROQ_MODEL,
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Explain the difference between saving and investing in simple terms."},
    ],
    "max_tokens": 100,
    "temperature": 0.7,
}

print(f"Sending request to {GROQ_API_URL}...")
response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=15)

print(f"\nStatus Code: {response.status_code}")
try:
    if response.status_code == 200:
        result = response.json()
        print("Success! Response from Groq:")
        print(result['choices'][0]['message']['content'])
    else:
        print(f"API Error. Response body: {response.text}")
except Exception as e:
    print(f"Error processing response: {e}")