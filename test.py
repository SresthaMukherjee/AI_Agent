from backend.feature import gemini_chatbot

print("Asking Gemini...")
response = gemini_chatbot("What's the capital of France?")
print("Response:", response)
