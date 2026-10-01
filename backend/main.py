import joblib

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


model = joblib.load("fraud_model.pkl")


class Transaction(BaseModel):
    amount: float
    transactions_today: int
    account_age_days: int
    new_location: int


@app.get("/")
def home():
    return {
        "message": "FraudGuard AI is running"
    }


@app.post("/predict")
def predict(transaction: Transaction):

    data = [[
        transaction.amount,
        transaction.transactions_today,
        transaction.account_age_days,
        transaction.new_location
    ]]

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)[0][1]

    if prediction == 1:
        result = "Potential Fraud"
    else:
        result = "Likely Legitimate"

    return {
        "prediction": result,
        "fraud_probability": round(probability * 100, 2)
    }
