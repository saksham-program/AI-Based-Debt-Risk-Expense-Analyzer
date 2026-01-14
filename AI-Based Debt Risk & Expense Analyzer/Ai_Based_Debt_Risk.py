# AI-Based Debt Risk & Expense Analyzer

def analyze_finances(income, expenses, debt):
    savings = income - expenses
    debt_to_income = debt / income
    expense_ratio = expenses / income

    print("\n--- Financial Analysis Report ---")
    print(f"Monthly Income   : ₹{income}")
    print(f"Monthly Expenses : ₹{expenses}")
    print(f"Total Debt       : ₹{debt}")
    print(f"Monthly Savings  : ₹{savings}")

    # Risk Analysis
    if debt_to_income < 0.3 and expense_ratio < 0.6:
        risk = "LOW RISK 🟢"
        advice = "Your finances are healthy. Keep saving and investing."
    elif debt_to_income < 0.6:
        risk = "MEDIUM RISK 🟡"
        advice = "Try to reduce expenses and avoid taking new loans."
    else:
        risk = "HIGH RISK 🔴"
        advice = "High financial stress. Focus on clearing debt urgently."

    print(f"\nDebt-to-Income Ratio : {round(debt_to_income, 2)}")
    print(f"Expense Ratio       : {round(expense_ratio, 2)}")
    print(f"Risk Level          : {risk}")
    print("AI Suggestion       :", advice)


# -------- MAIN PROGRAM --------
print("AI-Based Debt Risk & Expense Analyzer")

income = float(input("Enter your monthly income: ₹"))
expenses = float(input("Enter your monthly expenses: ₹"))
debt = float(input("Enter your total debt: ₹"))

analyze_finances(income, expenses, debt)
