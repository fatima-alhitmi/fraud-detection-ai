import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib


data = {
    "amount": [
        20, 45, 100, 35, 60,
        500, 1200, 850, 1500, 900,
        30, 55, 80, 40, 70,
        2000, 1300, 750, 1100, 1600
    ],

    "transactions_today": [
        1, 2, 3, 2, 4,
        8, 12, 10, 15, 11,
        2, 1, 3, 2, 4,
        18, 14, 9, 13, 16
    ],

    "account_age_days": [
        800, 600, 400, 900, 500,
        60, 30, 45, 20, 50,
        700, 1000, 300, 650, 450,
        15, 25, 40, 35, 10
    ],

    "new_location": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1
    ],

    "fraud": [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1
    ]
}


df = pd.DataFrame(data)

print("Training data:")
print(df)


X = df[
    [
        "amount",
        "transactions_today",
        "account_age_days",
        "new_location"
    ]
]

y = df["fraud"]


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


model = LogisticRegression()

model.fit(X_train, y_train)


predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("\nModel accuracy:", accuracy)


joblib.dump(model, "fraud_model.pkl")

print("\nModel saved as fraud_model.pkl")