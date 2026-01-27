def analyze_finances(income, expenses, debt):
    savings = income - expenses
    debt_to_income = debt / income
    expense_ratio = expenses / income

    if debt_to_income < 0.3 and expense_ratio < 0.6:
        risk = "LOW RISK"
        advice = "Your finances are healthy. Continue saving and investing wisely."
    elif debt_to_income < 0.6:
        risk = "MEDIUM RISK"
        advice = "Monitor your spending and avoid unnecessary debt."
    else:
        risk = "HIGH RISK"
        advice = "High financial stress detected. Focus on reducing debt urgently."

    return {
        "income": income,
        "expenses": expenses,
        "debt": debt,
        "savings": savings,
        "debt_to_income": round(debt_to_income, 2),
        "expense_ratio": round(expense_ratio, 2),
        "risk": risk,
        "advice": advice
    }
