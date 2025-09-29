from typing import List, Dict

class TransactionProcessor:
    def __init__(self,initial_balance: int = 0):
        self.balance = initial_balance
        self.log = []
        
    def process(self, transactions_list_dict: List[Dict]):
        for transaction in transactions_list_dict:
            transaction_id = transaction["id"]
            transaction_type = transaction["type"].lower()
            transaction_amount = transaction["amount"]
            
            if transaction_type == "deposit":
                self.balance += transaction_amount
                self.log.append(f"Transaction {transaction_id}: deposit {transaction_amount} succeeded. Balance = {self.balance}")
            elif transaction_type =="withdrawal":
                if self.balance >= transaction_amount:
                        self.balance -= transaction_amount
                        self.log.append(f"Transaction {transaction_id}: withdrawal {transaction_amount} succeeded. Balance = {self.balance}")
                else:
                    self.log.append(f"Transaction {transaction_id}: withdrawal {transaction_amount} failed. Insufficient funds (Balance = {self.balance})")

            
    def get_log(self) -> List[str]:
        return self.log
transactions = [
    {"id": 1, "type": "deposit", "amount": 200},
    {"id": 2, "type": "withdrawal", "amount": 50},
    {"id": 3, "type": "deposit", "amount": 100},
    {"id": 4, "type": "withdrawal", "amount": 500},  # fail
]

tp = TransactionProcessor()
tp.process(transactions)

for entry in tp.get_log():
    print(entry)
