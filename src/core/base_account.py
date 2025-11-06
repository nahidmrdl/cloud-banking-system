from abc import ABC, abstractmethod
from typing import List
from models.transaction import Transaction

class Account(ABC):
    def __init__(self, id: str, user_id: str, balance: float = 0.0):
        self.id = id
        self.user_id = user_id
        self.balance = balance
        self.transactions: List[Transaction] = []
    
    @abstractmethod
    def deposit(self, amount: float):
        pass

    @abstractmethod
    def withdraw(self, amount: float):
        pass

    @abstractmethod
    def transfer(self, target_account, amount: float):
        pass