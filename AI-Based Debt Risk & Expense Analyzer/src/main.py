# Entry point of the application
# Keeping things simple here since this is a CLI-based demo project

from rules_engine import analyze_finances
from ml_model import train_model, predict_risk


def get_user_input():
    """
    Separated input logic so main flow stays readable.
    Did this because earlier everything in main() was getting messy.
    """
    try:
        monthly_income = float(input("Enter your monthly income (₹): "))
        monthly_expenses = float(input("Enter your monthly expenses (₹): "))
        total_debt = float(input("Enter your total debt (₹): "))
    except ValueError:
        # Basic validation only — advanced checks can be added later
        print("\nInvalid input detected. Please enter numeric values only.")
        return None

    return monthly_income, monthly_expenses, total_debt


def main():
    print("\nAI-Based Debt Risk Analyzer\n")

    user_data = get_user_input()
    if not user_data:
        # Exiting early to avoid unnecessary crashes
        return

    income, expenses, debt_amount = user_data

    # -------- Rule-based analysis --------
    # Using this first because it gives transparent logic-based feedback
    finance_report = analyze_finances(income, expenses, debt_amount)

    print("\n--- Rule-Based Financial Analysis ---")
    print(f"Monthly Savings       : ₹{finance_report['savings']}")
    print(f"Debt-to-Income Ratio  : {finance_report['debt_to_income']}")
    print(f"Expense Ratio         : {finance_report['expense_ratio']}")
    print(f"Risk Level            : {finance_report['risk']}")
    print(f"Advice                : {finance_report['advice']}")

    # -------- ML-based prediction --------
    # Model is trained every run since this is a small demo dataset
    # In real systems, the model would be pre-trained and loaded
    model = train_model()
    predicted_risk = predict_risk(model, income, expenses, debt_amount)

    print("\n--- ML-Based Risk Prediction ---")
    print(f"Predicted Risk Level  : {predicted_risk}")


# Standard Python convention
# Added explicitly to avoid accidental execution during imports
if __name__ == "__main__":
    main()
