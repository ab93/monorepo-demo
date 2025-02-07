from functools import lru_cache
from typing import Any


class ModelManager:
    def __init__(self, model_location: str):
        self._model_location = model_location

    def load_model_weights(self, model_name: str, model_version: str = None) -> dict[str, Any]:
        pass

    @lru_cache(maxsize=1)
    def load_model(self, model_name: str, model_version: str = None) -> bytes:
        pass

    def save_model(self, serialized_model: bytes) -> None:
        print("Saving model...")
