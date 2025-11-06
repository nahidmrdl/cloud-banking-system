from typing import List
from models.account import Account

class User:
    def __init__(self, id: str, name: str, email: str, role: str = "customer"):
        self.id = id
        self.name = name
        self.email = email 
        self.role = role

    def authenticate(self, password: str) -> bool:
        pass

    def get_accounts(self) -> List[Account]:
        pass