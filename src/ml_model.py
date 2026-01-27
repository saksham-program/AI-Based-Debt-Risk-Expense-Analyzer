import pandas as pd
from sklearn.linear_model import LogisticRegression

def train_model():
    data = pd.read_csv("data/sample_financial_data.csv")
    print("CSV rows used for training:", len(data))

    X = data[['income', 'expenses', 'debt']]
    y = data['risk_label']

    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)

    return model


def predict_risk(model, income, expenses, debt):
    input_data = pd.DataFrame(
        [[income, expenses, debt]],
        columns=['income', 'expenses', 'debt']
    )

    prediction = model.predict(input_data)
    labels = {0: "LOW RISK", 1: "MEDIUM RISK", 2: "HIGH RISK"}
    return labels[prediction[0]]

