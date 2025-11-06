from datetime import datetime

class Transaction:
    def __init__(self, id: str, account_id: str, type: str, amount: float, description: str = ""):
        self.id = id
        self.account_id = account_id
        self.type = type  # "deposit", "withdrawal", "transfer"
        self.amount = amount
        self.description = description
        self.timestamp = datetime.now()