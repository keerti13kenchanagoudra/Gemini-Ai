
def generate_response(prompt):
    lower_prompt = prompt.lower()
    score = 0
    if "role:" in lower_prompt:
        score += 1
    if "task:" in lower_prompt:
        score += 1
    if "format:" in lower_prompt:
        score += 1
    if "constraint:" in lower_prompt:
        score += 1
    if score <= 2:
        return (
            "prompt is not in good structure"
        )

    return (
       "its a good prompt"
    )


vague_prompt = "Explain Python functions."
structured_prompt = """
Role: You are a Python tutor.
Task: Explain Python functions.
Audience: First-year BCA students.
Format: Use 3 points and one short code example.
Constraint: Avoid advanced words.
"""

print(generate_response(vague_prompt))
print(structured_prompt.strip())
print(generate_response(structured_prompt))

