from pydantic import BaseModel


class TransactionData(BaseModel):
    transaction_id: str
    amount: float
    merchant_score: float
    risk_level: float


class PredictionResponse(BaseModel):
    transaction_id: str
    is_fraudulent: bool
