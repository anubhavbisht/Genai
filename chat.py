from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user","content":"Hello how are you? What is your name. My name is anubhav"}
    ]
)

print(result.choices[0].message.content)