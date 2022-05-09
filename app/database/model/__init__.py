from app.database.model.employee_model import _EmployeeModel


class TableModel:
    def __init__(self, connection):
        self.user = _EmployeeModel(connection)
