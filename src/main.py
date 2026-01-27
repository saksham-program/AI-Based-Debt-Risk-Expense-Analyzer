from rules_engine import analyze_finances
from ml_model import train_model, predict_risk

print("\nAI-Based Debt Risk Analyzer\n")

income = float(input("Enter your monthly income (₹): "))
expenses = float(input("Enter your monthly expenses (₹): "))
debt = float(input("Enter your total debt (₹): "))

# Rule-based analysis
result = analyze_finances(income, expenses, debt)

print("\n--- Rule-Based Financial Analysis ---")
print(f"Monthly Savings       : ₹{result['savings']}")
print(f"Debt-to-Income Ratio  : {result['debt_to_income']}")
print(f"Expense Ratio         : {result['expense_ratio']}")
print(f"Risk Level            : {result['risk']}")
print(f"Advice                : {result['advice']}")

# ML-based prediction
model = train_model()
ml_risk = predict_risk(model, income, expenses, debt)

print("\n--- ML-Based Risk Prediction ---")
print(f"Predicted Risk Level  : {ml_risk}")
