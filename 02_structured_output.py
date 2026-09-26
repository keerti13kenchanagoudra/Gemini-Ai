"""Use case 2: request predictable JSON and parse it in Python."""

import json
from common import create_client, model_name
request = "Create a study plan for Python."
prompt = (
    f"{request}\n"
    "Return only valid JSON with this shape: "
    '{"title": "string", "steps": ["string"], "minutes": 30}'
)
client = create_client()
response = client.models.generate_content(
    model=model_name(),
    contents=prompt,
    config={"response_mime_type": "application/json"},
)
result = json.loads(response.text)

print(json.dumps(result, indent=2))

