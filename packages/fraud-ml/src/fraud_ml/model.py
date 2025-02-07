from typing import Any

import numpy as np
import numpy.typing as npt


class FraudModel:
    def __init__(self):
        self._model = None
        self._weights = None

    def fit(self, _x: npt.NDArray[np.float64], _y: npt.NDArray[np.float64]):
        """Simulate model training"""
        return self

    def predict(self, x: npt.NDArray[np.float64]) -> npt.NDArray[np.int64]:
        """Simulate prediction"""
        return np.random.choice([0, 1], x.shape[0])

    @classmethod
    def from_weights(cls, _: dict[str, Any]):
        """Simulate loading model weights"""
        return cls()
