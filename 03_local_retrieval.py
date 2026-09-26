"""Day 1 Demo 3: Local retrieval from a small knowledge base.

This demonstrates the idea behind RAG without using an LLM or API.
"""

from pathlib import Path
import re


DATA_FILE = Path(__file__).parent / "data" / "college_faq.txt"


def tokenize(text):
    """Convert text into lowercase words for simple matching."""
    return set(re.findall(r"[a-zA-Z]+", text.lower()))


def load_faq_entries(file_path):
    """Load FAQ entries separated by blank lines."""
    content = file_path.read_text(encoding="utf-8")
    entries = []

    for block in content.strip().split("\n\n"):
        lines = block.splitlines()
        if len(lines) >= 2:
            question = lines[0].replace("Question:", "").strip()
            answer = lines[1].replace("Answer:", "").strip()
            entries.append({"question": question, "answer": answer})

    return entries


def score_entry(user_question, entry):
    """Score an FAQ entry using word overlap."""
    question_words = tokenize(user_question)
    entry_words = tokenize(entry["question"] + " " + entry["answer"])
    return len(question_words.intersection(entry_words))


def retrieve_best_answer(user_question, entries):
    """Find the most relevant entry and return a simple answer."""
    best_entry = None
    best_score = 0

    for entry in entries:
        score = score_entry(user_question, entry)
        if score > best_score:
            best_score = score
            best_entry = entry

    if best_entry is None:
        return "I could not find a related FAQ entry."

    return (
        f"Most relevant FAQ: {best_entry['question']}\n"
        f"Answer from local knowledge base: {best_entry['answer']}"
    )


entries = load_faq_entries(DATA_FILE)
user_question = input("Question: ")
print(retrieve_best_answer(user_question, entries))
