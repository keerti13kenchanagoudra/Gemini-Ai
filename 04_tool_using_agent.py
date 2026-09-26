"""Day 1 Demo 4: A tiny tool-using agent.

The agent chooses a Python function based on the user's request.
"""

from datetime import date


def calculator(expression):
    """Safely evaluate basic arithmetic expressions."""
    allowed_characters = set("0123456789+-*/(). ")

    if any(character not in allowed_characters for character in expression):
        return "Only basic arithmetic is allowed."

    try:
        return str(eval(expression, {"__builtins__": {}}, {}))
    except ZeroDivisionError:
        return "Cannot divide by zero."
    except SyntaxError:
        return "The arithmetic expression is not valid."


def uppercase_text(text):
    """Convert text to uppercase."""
    return text.upper()


def today_date():
    """Return today's date from the computer."""
    return date.today().isoformat()


def choose_tool(user_message):
    """Choose a tool using simple keyword rules."""
    clean_message = user_message.lower().strip()

    if clean_message.startswith("calculate "):
        expression = user_message[len("calculate "):]
        return "calculator", calculator(expression)

    if clean_message.startswith("uppercase "):
        text = user_message[len("uppercase "):]
        return "uppercase_text", uppercase_text(text)

    if "date" in clean_message or "today" in clean_message:
        return "today_date", today_date()

    return None, "I can calculate, uppercase text, or tell today's date."


def main():
    print("Tool-Using Agent Demo")
    print("Examples:")
    print("- calculate 10 + 5 * 2")
    print("- uppercase agentic ai")
    print("- what is today's date")
    print("Type 'exit' to stop.\n")

    while True:
        user_message = input("User: ")

        if user_message.lower().strip() == "exit":
            print("Agent: Goodbye.")
            break

        tool_name, result = choose_tool(user_message)

        if tool_name:
            print(f"Agent selected tool: {tool_name}")
        else:
            print("Agent selected no tool")

        print("Agent result:", result)
        print()


if __name__ == "__main__":
    main()
