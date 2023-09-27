

class Client:
    def __init__(self, name):
        self.name = name

    def check_balance(self, bank):
        balance = bank.get_balance(self)
        return f"{self.name}'s balance: ${balance}"


class Bank:
    def __init__(self):
        self.accounts = {}

    def open_account(self, client):
        self.accounts[client] = BankAccount()

    def get_balance(self, client):
        if client in self.accounts:
            return self.accounts[client].balance
        else:
            return 0


class BankAccount:
    def __init__(self):
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")


if __name__ == '__main__':
    # Using the classes
    bank = Bank()
    client1 = Client("Alice")
    client2 = Client("Bob")

    bank.open_account(client1)
    bank.open_account(client2)

    client1_account = bank.get_balance(client1)
    client2_account = bank.get_balance(client2)

    print(client1.check_balance(bank))  # Client checks balance through the bank
    print(client2.check_balance(bank))