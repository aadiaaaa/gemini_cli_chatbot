from google import genai
import os

# Securely retrieve the key from environment variables
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable not found. Please set it before running.")

client = genai.Client(api_key=api_key)

print("Gemini Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",   
            contents=user_input
        )
        print(f"Gemini: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")
