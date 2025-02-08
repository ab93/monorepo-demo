import numpy as np
import pandas as pd


class DummyDataFetcher:
    """
    Dummy data fetcher for simulating data retrieval from an
    external database.

    Parameters
    ----------
    conn_params : dict[str, str]
        Connection parameters to the external database.
    """
    def __init__(self, **conn_params):
        self._conn_params = conn_params

    @property
    def connection_parameters(self) -> dict[str, str]:
        """Connection parameters to the external database."""
        return self._conn_params

    def fetch(self, num_rows: int) -> tuple[pd.DataFrame, pd.Series]:
        """
        Fetch dummy data from an external database.

        Parameters
        ----------
        num_rows : int
            Number of rows to fetch.

        Returns
        -------
        tuple[pd.DataFrame, pd.Series]
            Tuple containing the input data (X) and the target
            variable (y).
        """
        # Simulating database query with a dummy dataframe
        x_dummy = pd.DataFrame(
            np.random.randn(num_rows, 3),
            columns=["amount", "merchant_score", "risk_level"],
        )
        y_dummy = pd.Series(
            np.random.randint(0, 2, size=num_rows), name="is_fraudulent"
        )
        return x_dummy, y_dummy
