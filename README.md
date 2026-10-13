# AI Insurance Advisor

## Building AI course project — Educational prototype

### 1. Summary

AI Insurance Advisor is a simple Python prototype that helps users explore which **category of insurance or financial protection** may match their stated priorities: life insurance, health insurance, savings, or retirement. It asks four yes/no questions and provides a transparent explanation of its recommendation. It does **not** quote policies, calculate premiums, decide eligibility, or replace a licensed insurance professional.

### 2. The problem

Insurance products can be difficult to understand, and people may not know where to begin when discussing protection and long-term planning. A lightweight decision-support tool could help organize their priorities before meeting an advisor.

### 3. Why AI could help

AI can support recommendation systems by connecting user preferences with relevant options. This prototype starts with an interpretable **rule-based baseline**. It does not claim to be a trained machine-learning system. In a future version, a properly consented, anonymized dataset could support testing a classification or ranking model.

### 4. How it works

The program asks whether the user:

1. Has people financially dependent on their income.
2. Prioritizes protection from unexpected medical expenses.
3. Is saving for a goal within the next ten years.
4. Prioritizes retirement planning.

Each "yes" assigns three points to the corresponding category. The category with the highest score is recommended. Ties are shown explicitly. If all answers are "no," the program does not force a recommendation. Scores are **not probabilities**.

### 5. Technologies

- Python 3 (standard library only)
- Transparent rule-based recommendation logic
- No external services, tracking, or data storage

### 6. Run the project

```bash
python insurance_advisor.py
```

Answer each question with `yes` or `no`.

### 7. Example

**Input:** Dependents: yes; Medical expenses: no; Savings: no; Retirement: no.

**Output:** Life insurance — protection for financial dependents if the insured dies.

### 8. Testing

Run:

```bash
python -m unittest discover -s tests -v
```

Tests cover life insurance, health insurance, tied priorities, and no clear priority.

### 9. Limitations and ethical considerations

- The rules are illustrative and have not been validated against customer outcomes.
- A preference match is not a suitability assessment or recommendation to purchase a particular policy.
- Actual product suitability depends on budget, needs, policy exclusions, underwriting, regulations, and professional review.
- No sensitive medical, financial, or identity data should be entered.
- The tool must not be used to infer protected characteristics, discriminate, or automate insurance eligibility or pricing.
- Users should be able to understand and challenge the reasoning.

### 10. Future development

With appropriate consent, governance, and evaluation, the project could be extended to compare model recommendations against qualified expert assessments, measure error rates, examine fairness, and improve explanations. Any real deployment would require legal, privacy, and domain-specific review.

### 11. Conclusion

This project demonstrates how a transparent recommendation baseline can support clearer conversations about insurance needs. It also illustrates a central Building AI lesson: useful AI systems require clear goals, reliable evaluation, and responsible human oversight.

### 12. Authorship

Prepared as a customizable educational project template. The student should review, test, adapt, and take responsibility for the final submission. No external datasets or third-party images are included.
