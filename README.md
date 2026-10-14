# FraudGuard AI

**A machine learning-based fraud detection web application.**

FraudGuard AI is a web application that analyzes transaction-related features to classify transactions as potentially fraudulent or likely legitimate. It combines a Python machine learning model with a FastAPI backend and a React frontend to demonstrate an end-to-end AI application.

## Features

- Transaction risk classification using a trained machine learning model
- Analysis of transaction amount and daily transaction activity
- Account age and new-location indicators
- Risk score returned alongside the prediction
- REST API built with FastAPI
- Interactive web interface built with React
- API testing through automatically generated Swagger documentation

## Technology Stack

- **Programming language:** Python
- **Machine learning:** scikit-learn
- **Backend:** FastAPI, Uvicorn
- **Frontend:** React, Vite, JavaScript, CSS
- **Version control:** Git and GitHub

## How It Works

FraudGuard AI accepts transaction-related information and passes it to a trained classification model.

The model considers the following features:

| Feature | Description |
|---|---|
| Transaction amount | Monetary value of the transaction |
| Transactions today | Number of transactions made during the day |
| Account age | Age of the account in days |
| New location | Indicates whether the transaction originates from a new location |

The backend processes the input and returns a classification and a risk score. The frontend displays the result to the user.

**Example classifications:**
- `Potential Fraud`
- `Likely Legitimate`

The returned score is a model-generated risk indicator, not a guarantee that a transaction is fraudulent or legitimate.

## Project Structure

```text
fraud-detection-ai/
├── backend/
│   ├── main.py
│   ├── train_model.py
│   └── fraud_model.pkl
├── frontend/
│   ├── src/
│   ├── package.json
│   └── index.html
├── .gitignore
└── README.md
```

## Installation and Setup

### Prerequisites

- Python 3
- Node.js and npm
- Git

### 1. Clone the repository

```bash
git clone https://github.com/fatima-alhitmi/fraud-detection-ai.git
cd fraud-detection-ai
```

### 2. Set up the backend

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required packages:

```bash
python -m pip install fastapi "uvicorn[standard]" scikit-learn numpy
```

Start the backend from the project root:

```bash
uvicorn backend.main:app --reload
```

The API will be available at:

`http://127.0.0.1:8000`

Interactive API documentation:

`http://127.0.0.1:8000/docs`

### 3. Set up the frontend

Open a separate terminal and run:

```bash
cd fraud-detection-ai/frontend
npm install
npm run dev
```

Open the local URL displayed in the terminal, normally:

`http://localhost:5173`

Keep both the backend and frontend running while testing the application.

## API

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check backend status |
| POST | `/predict` | Classify a transaction and return its risk score |

The `/predict` endpoint accepts transaction features and returns a prediction that the frontend can display.

Interactive request and response details are available through the FastAPI documentation at `/docs`.

## Model Training

The model is trained using `backend/train_model.py` and saved as `backend/fraud_model.pkl` for use by the API.

The current implementation is a demonstration project designed to showcase the integration of machine learning into a web application. Its predictions depend on the quality and representativeness of the training data.

It has not been established as a production-ready fraud detection system. Real-world deployment would require a representative, sufficiently large dataset, rigorous validation, threshold calibration, and monitoring for changing fraud patterns.

## Future Improvements

- Train and evaluate the model using a larger, realistic transaction dataset
- Measure precision, recall, F1-score, and false-positive rates
- Improve risk-score calibration
- Add transaction history and risk analytics
- Improve model explainability
- Deploy the application with appropriate security and monitoring

## Author

**Fatma Al-Hitmi**

GitHub: [fatima-alhitmi](https://github.com/fatima-alhitmi)
