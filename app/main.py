import numpy as np
from fastapi import FastAPI

from data_connector import ModelManager
from fraud_ml.model import FraudModel
from app.internal.rmodels import PredictionResponse, TransactionData

app = FastAPI()


@app.get("/health")
def health_check() -> dict[str, str]:
    """Check if the server is running."""
    return {"status": "Server is running"}


@app.post("/detect", response_model=PredictionResponse)
def detect(transaction: TransactionData) -> PredictionResponse:
    """
    Detect fraudulent transactions using a trained
    dummy ML model.

    Parameters
    ----------
    transaction : TransactionData
        Transaction data to be used for prediction.

    Returns
    -------
    PredictionResponse
        Prediction response containing the transaction ID
        and whether the transaction is fraudulent.
    """

    # Convert input data to numpy array for model
    x = np.array(
        [transaction.amount, transaction.merchant_score, transaction.risk_level]
    )

    # Load and get predictions from model
    loader = ModelManager("some/path/to/model")
    weights = loader.load_model_weights("fraud_model", "v1")
    model = FraudModel.from_weights(weights)
    y = model.predict(x)

    # Format response
    return PredictionResponse(
        transaction_id=transaction.transaction_id, is_fraudulent=bool(y[0])
    )
