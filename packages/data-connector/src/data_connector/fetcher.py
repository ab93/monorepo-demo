import numpy as np
import pandas as pd


class DummyDataFetcher:
    def __init__(self, **conn_params):
        self._conn_params = conn_params

    @property
    def connection_parameters(self) -> dict[str, str]:
        return self._conn_params

    def fetch(self, num_rows: int) -> tuple[pd.DataFrame, pd.Series]:
        # Simulating database query with a dummy dataframe
        x_dummy = pd.DataFrame(
            np.random.randn(num_rows, 3),
            columns=["amount", "merchant_score", "risk_level"]
        )
        y_dummy = pd.Series(np.random.randint(0, 2, size=num_rows), name="is_fraudulent")
        return x_dummy, y_dummy
