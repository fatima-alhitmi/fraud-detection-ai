import { useState } from "react";
import "./App.css";

function App() {
  const [amount, setAmount] = useState("");
  const [transactionsToday, setTransactionsToday] = useState("");
  const [accountAge, setAccountAge] = useState("");
  const [newLocation, setNewLocation] = useState("0");

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (event) => {
    event.preventDefault();

    setLoading(true);
    setResult(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          amount: Number(amount),
          transactions_today: Number(transactionsToday),
          account_age_days: Number(accountAge),
          new_location: Number(newLocation),
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error("Prediction request failed");
      }

      setResult(data);
    } catch (error) {
      setResult({
        prediction: "Unable to connect to server",
        fraud_probability: null,
      });
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <header className="header">
        <h1>FraudGuard AI</h1>
        <p>AI-powered transaction fraud detection</p>
      </header>

      <main className="main">
        <section className="card">
          <h2>Analyze a Transaction</h2>
          <p className="description">
            Enter the transaction details below to check for potential fraud.
          </p>

          <form onSubmit={handleSubmit}>
            <label>
              Transaction Amount
              <input
                type="number"
                value={amount}
                onChange={(e) => setAmount(e.target.value)}
                placeholder="e.g. 500"
                required
              />
            </label>

            <label>
              Transactions Today
              <input
                type="number"
                value={transactionsToday}
                onChange={(e) => setTransactionsToday(e.target.value)}
                placeholder="e.g. 8"
                required
              />
            </label>

            <label>
              Account Age (days)
              <input
                type="number"
                value={accountAge}
                onChange={(e) => setAccountAge(e.target.value)}
                placeholder="e.g. 60"
                required
              />
            </label>

            <label>
              New Location?
              <select
                value={newLocation}
                onChange={(e) => setNewLocation(e.target.value)}
              >
                <option value="0">No</option>
                <option value="1">Yes</option>
              </select>
            </label>

            <button type="submit" disabled={loading}>
              {loading ? "Analyzing..." : "Analyze Transaction"}
            </button>
          </form>
        </section>

        {result && (
          <section className="result-card">
            <h2>Analysis Result</h2>

            <p className="prediction">
              {result.prediction}
            </p>

            {result.fraud_probability !== null && (
              <p>
                Fraud probability:{" "}
                <strong>{result.fraud_probability}%</strong>
              </p>
            )}
          </section>
        )}
      </main>
    </div>
  );
}

export default App;