from functools import lru_cache
from typing import Any


class ModelManager:
    """
    Manages loading and saving of ML models.

    Parameters
    ----------
    model_location : str
        Location to save/load the model.
    """
    def __init__(self, model_location: str):
        self._model_location = model_location

    def load_model_weights(
        self, model_name: str, model_version: str = None
    ) -> dict[str, Any]:
        """
        Load model weights from the model location.

        Parameters
        ----------
        model_name : str
            Name of the model.
        model_version : str, optional
            Version of the model to load.

        Returns
        -------
        dict[str, Any]
            Model weights.
        """
        pass

    @lru_cache(maxsize=1)
    def load_model(self, model_name: str, model_version: str = None) -> bytes:
        """
        Load a serialized model from the model location.

        Parameters
        ----------
        model_name : str
            Name of the model.
        model_version : str, optional
            Version of the model to load.

        Returns
        -------
        bytes
            Serialized model.
        """
        pass

    def save_model(self, _serialized_model: bytes) -> None:
        """
        Save a serialized model to the model location.

        Parameters
        ----------
        _serialized_model : bytes
            Serialized model.
        """
        print("Saving model to location:", self._model_location)
