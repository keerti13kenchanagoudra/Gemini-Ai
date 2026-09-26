
import sys


def create_plan(goal):
    """Create small steps for the goal."""
    goal_lower = goal.lower()

    if "notes" in goal_lower or "prepare" in goal_lower:
        return ["find topic", "create points", "give practice task"]

    return ["understand goal", "give simple answer"]


def act(step, goal):
    """Run one step and return an observation."""
    if step == "find topic":
        return f"Topic identified from goal: {goal}"

    if step == "create points":
        return "Key points: agents plan, use tools, observe results, and respond."

    if step == "give practice task":
        return "Practice: write one example where an agent can help a student."

    return "Simple answer: an agentic system works step by step toward a goal."


def run_agent(goal):
    """Run the simple plan-act-observe flow."""
    plan = create_plan(goal)
    observations = []

    for step in plan:
        observation = act(step, goal)
        observations.append(observation)

    return plan, observations


goal = " ".join(sys.argv[1:]).strip() or "prepare notes on agentic ai"
plan, observations = run_agent(goal)

print("GOAL")
print(goal)

print("\nPLAN")
for step in plan:
    print(f"- {step}")

print("\nOBSERVATIONS")
for observation in observations:
    print(f"- {observation}")

print("\nFINAL ANSWER")
print(" ".join(observations))

