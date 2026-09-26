"""Use case 4: run a local tool and ask Gemini to explain its result."""

import re
import sys

from common import create_client, model_name

def multiply_numbers(text):
    """Multiply the first two numbers found in text."""
    numbers = [int(value) for value in re.findall(r"-?\d+", text)]
    if len(numbers) < 2:
        return None
    return numbers[0] * numbers[1]


request = "What is 12 multiplied by 8?"
tool_result = multiply_numbers(request)
if tool_result is None:
    print("Please include two whole numbers")
    sys.exit(1)

client = create_client()
prompt = f"The local calculator returned {tool_result} for this request: {request}. Explain the answer briefly."
response = client.models.generate_content(model=model_name(), contents=prompt)

print(f"LOCAL TOOL RESULT: {tool_result}")
print(f"GEMINI EXPLANATION: {response.text}")

