from app.database.base_connector import BaseConnector
from app.database.model import TableModel


class _ModelGetter:
    def __init__(self):
        self._connection = BaseConnector()
        self._model = None

    def get_model(self) -> TableModel:
        if self._model is None:
            self._model = TableModel(self._connection)
        return self._model


ModelGetter = _ModelGetter()
