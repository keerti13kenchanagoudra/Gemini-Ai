"""Use case 1: generate a simple answer from one prompt."""

import sys

from common import create_client, model_name


def main():
    prompt = " ".join(sys.argv[1:]).strip() or "Explain what an AI agent is in three sentences."
    client = create_client()
    response = client.models.generate_content(model=model_name(), contents=prompt)

    print(response.text)


if __name__ == "__main__":
    main()
