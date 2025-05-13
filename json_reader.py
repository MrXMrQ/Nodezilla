import json
import os


class JSONReader:
    def __init__(self, path: str = "graph.json") -> None:
        if not isinstance(path, str):
            raise TypeError(
                f"Invalid type for 'path': expected 'str', got '{type(path)}' instead."
            )

        self._path: str = path
        self._data: dict = self.load()

    def load(self) -> dict:
        try:
            with open(self._path, "r") as file:
                return json.load(file)

        except FileNotFoundError:
            raise FileNotFoundError(
                f"The specified file does not exist: '{self._path}'"
            )

    @property
    def data(self) -> dict:
        return self._data
