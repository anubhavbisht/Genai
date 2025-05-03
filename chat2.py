from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

systemPrompt="""
You are an AI assistant who is specialized in maths.
You should not answer any question that is not related to maths.

For a given query help user to solve that along with explaination

Input: 2+2
Output: 2+2 is 4 which is calculated by adding 2 and 2

Input: why is sky blue?
Output: Bruh!Don't ask me silly question
"""

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": systemPrompt},
        {
            "role": "user",
            "content": "what is 2+2",
        },
    ],
)

print(result.choices[0].message.content)
result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": systemPrompt},
        {
            "role": "user",
            "content": "what is 2*2",
        },
    ],
)

print(result.choices[0].message.content)
result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": systemPrompt},
        {
            "role": "user",
            "content": "what is 2/2",
        },
    ],
)

print(result.choices[0].message.content)

result = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {
            "role": "system",
            "content": systemPrompt},
        {
            "role": "user",
            "content": "how is weather today?",
        },
    ],
)

print(result.choices[0].message.content)