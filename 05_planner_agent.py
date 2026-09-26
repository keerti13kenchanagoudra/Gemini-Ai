
from datetime import date


TOPICS = {
    "prompt": "prompting",
    "rag": "rag"
}
def summarize_topic(topic):
    """Return a short local summary for a known topic."""
    summaries = {
        "prompting": "Prompting means writing clear instructions for an AI system.",
        "rag": "RAG means retrieving trusted information before generating an answer."
    }

    return summaries.get(topic, "No local summary is available for this topic.")

def make_quiz(topic):
    """Return a small quiz for a known topic."""
    quizzes = {
        "prompting": [
            "What is a prompt?",
            "Name two parts of a good prompt.",
        ],
        "rag": [
            "What does RAG stand for?",
            "Why is retrieval useful before answering?",
        ]
    }

    return quizzes.get(topic, ["No quiz is available for this topic."])


def create_plan(goal):
    """Convert a goal into simple agent steps."""
    clean_goal = goal.lower().strip()
    topic = "agents"

    for keyword, matched_topic in TOPICS.items():
        if keyword in clean_goal:
            topic = matched_topic
            break

    return [
        {"action": "summarize", "topic": topic},
        {"action": "quiz", "topic": topic}    ]


def act(step):
    """Perform one planned step."""
    if step["action"] == "summarize":
        return summarize_topic(step["topic"])

    if step["action"] == "quiz":
        questions = make_quiz(step["topic"])
        return "\n".join(f"- {question}" for question in questions)

    return "Unknown action."


def run_agent(goal):
    """Run the full plan-act-observe loop."""
    plan = create_plan(goal)
    observations = []

    print("PLAN")
    for index, step in enumerate(plan, start=1):
        print(f"{index}. {step}")

    print("\nACT AND OBSERVE")
    for step in plan:
        result = act(step)
        observations.append(result)
        print(f"Action: {step['action']}")
        print(f"Observation: {result}\n")

    return "\n".join(observations)

goal = input("Goal: ")
final_answer = run_agent(goal)

print("FINAL ANSWER")
print(final_answer)
