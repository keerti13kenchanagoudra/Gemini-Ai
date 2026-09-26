
RESPONSES = {
    "python": "Python is a beginner-friendly programming language ",
    "gen ai": "Generative AI ",
    "agent": "An agent can work toward a goal"
}

def get_response(message):
    clean_message = message.lower().strip()

    for keyword, response in RESPONSES.items():
        if keyword in clean_message:
            return response

    return "I do not know that yet. Try asking again"


user_message = input("You: ")
print("Bot:", get_response(user_message))

