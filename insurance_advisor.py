"""Educational insurance category recommendation prototype.

No personal data is collected, saved, or transmitted.
This is a rule-based AI-inspired decision support baseline, not a trained ML model.
"""

CATEGORIES = {
    "Life insurance": "Protection for financial dependents if the insured dies.",
    "Health insurance": "Help with eligible medical expenses, subject to policy terms.",
    "Savings plan": "A structured way to pursue medium-term financial goals.",
    "Retirement plan": "Long-term planning for retirement income needs.",
}

QUESTIONS = [
    ("Do other people depend on your income? (yes/no): ", "dependents"),
    ("Is covering unexpected medical expenses your main priority? (yes/no): ", "health"),
    ("Are you saving for a goal within the next 10 years? (yes/no): ", "savings"),
    ("Is retirement planning your main priority? (yes/no): ", "retirement"),
]


def recommend(answers):
    """Rank categories using transparent, illustrative preference scores."""
    scores = {
        "Life insurance": 3 if answers.get("dependents") else 0,
        "Health insurance": 3 if answers.get("health") else 0,
        "Savings plan": 3 if answers.get("savings") else 0,
        "Retirement plan": 3 if answers.get("retirement") else 0,
    }
    ranked = sorted(scores, key=lambda name: (-scores[name], list(scores).index(name)))
    if max(scores.values()) == 0:
        return [], scores
    return [name for name in ranked if scores[name] == max(scores.values())], scores


def ask_yes_no(prompt):
    while True:
        value = input(prompt).strip().lower()
        if value in {"yes", "y"}:
            return True
        if value in {"no", "n"}:
            return False
        print("Please type yes or no.")


def main():
    print("AI Insurance Advisor — educational prototype")
    print("Do not enter names, medical histories, or other personal details.\n")
    answers = {key: ask_yes_no(question) for question, key in QUESTIONS}
    recommendations, scores = recommend(answers)
    print("\nRecommendation:")
    if recommendations:
        for category in recommendations:
            print(f"- {category}: {CATEGORIES[category]}")
        if len(recommendations) > 1:
            print("Multiple priorities were selected; these categories are tied.")
    else:
        print("No clear category yet. Consider speaking with a qualified advisor.")
    print("\nScores (illustrative, not probabilities):", scores)
    print("Disclaimer: This is not personalized financial, medical, or insurance advice.")
    print("Actual coverage, eligibility, exclusions, and pricing require professional review.")


if __name__ == "__main__":
    main()
