from core.base_account import Account

class SavingsAccount(Account):
    def __init__(self, id: str, user_id: str, balance: float = 0.0, interest_rate: float = 0.0):
        super().__init__(id, user_id, balance)
        self.interest_rate = interest_rate

    def deposit(self, amount: float):
        pass

    def withdraw(self, amount: float):
        pass

    def transfer(self, target_account, amount: float):
        pass

    def apply_interest(self):
        pass