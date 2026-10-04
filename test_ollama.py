import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

response = requests.post(
    OLLAMA_URL,
    json={
        "model": "deepseek-coder:latest",
        "prompt": "Write a Python function to reverse a string.",
        "stream": False
    }
)

print("Status:", response.status_code)
print()
print("Response:")
print(response.json())