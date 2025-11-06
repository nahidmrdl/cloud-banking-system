from core.base_account import Account

class CheckingAccount(Account):
    def __init__(self, id: str, user_id: str, balance: float = 0.0, overdraft_limit: float = 0.0):
        super().__init__(id, user_id, balance)
        self.overdraft_limit = overdraft_limit

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def transfer(self, target_account, amount: float):
        pass

    def check_overdraft(self, amount: float) -> bool:
        pass