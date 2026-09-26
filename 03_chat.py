"""Use case 3: keep a short multi-turn conversation."""

from common import create_client, model_name

client = create_client()
chat = client.chats.create(model=model_name())

first_reply = chat.send_message("Explain lists in python.")
second_reply = chat.send_message("Now give me one short practice question.")

print("TUTOR:")
print(first_reply.text)
print("\nPRACTICE:")
print(second_reply.text)
