import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

system_prompt = """
You are an AI assistant who is expert in breaking down complex problems and then resolve the user query.

For the given user input, analyse the input and break down the problem step by step.
Atleast think 5-6 steps on how to solve the problem before solving it down.

The steps are you get a user input, you analyse, you think, you again think for several times and then return an output with explanation and then finally you validate the output as well before giving final result.

Follow the steps in sequence that is "analyse", "think", "output", "validate" and finally "result".

Rules:
1. Follow the strict JSON output as per Output schema.
2. Always perform one step at a time and wait for next input
3. Carefully analyse the user query

Output Format:
{{ step: "string", content: "string" }}

Example:
Input: What is 2 + 2.
Output: {{ step: "analyse", content: "Alright! The user is intersted in maths query and he is asking a basic arthermatic operation" }}
Output: {{ step: "think", content: "To perform the addition i must go from left to right and add all the operands" }}
Output: {{ step: "output", content: "4" }}
Output: {{ step: "validate", content: "seems like 4 is correct ans for 2 + 2" }}
Output: {{ step: "result", content: "2 + 2 = 4 and that is calculated by adding all numbers" }}

"""

result = client.chat.completions.create(
    model="gpt-4o",
    response_format={"type": "json_object"},
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": "what is 3 + 4 * 5"},
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "analyse",
                    "content": "The user is asking for a mathematical evaluation involving addition and multiplication following the rules of arithmetic operations.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "think",
                    "content": "I must first consider the order of operations, also known as PEMDAS (Parentheses, Exponents, Multiplication and Division, Addition and Subtraction), to correctly solve the expression.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "think",
                    "content": "Following the order of operations, I need to perform the multiplication first before the addition. So, 4 * 5 should be computed before adding 3.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "output",
                    "content": "First calculate 4 * 5 which equals 20, then add 3 to get a result of 23.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "validate",
                    "content": "Revisiting the steps, multiplication 4 * 5 indeed results in 20, then adding 3 gives 23. The answer seems accurate.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "result",
                    "content": "The result of the expression 3 + 4 * 5 is 23, calculated by performing the multiplication before the addition following the order of operations.",
                }
            ),
        },
        {
            "role": "assistant",
            "content": json.dumps(
                {
                    "step": "conclusion",
                    "content": "To solve arithmetic expressions correctly, always remember to follow the order of operations, addressing multiplication and division before addition and subtraction. This ensures accurate calculations.",
                }
            ),
        },
    ],
)

print(result.choices[0].message.content)
