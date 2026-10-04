import json
with open("account.json", "r") as file:
      account_data = json.load(file)
print(account_data)

class BankAccount:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance

    def add_money(self):
        while True:
            try:
                        user_add = input("Add amount, it shouldn't be $0 or less:$")
                        amount = float(user_add)
                        if amount <= 0:
                            print(f"Invalid amount, number must be above $0")
                        elif amount > 0 :
                            self.balance = self.balance + amount
                            print(f"${amount} has been credited to Your account. Your account balance is ${self.balance}")
                            return self.balance
            except ValueError:
                        print(f"Invalid input")

    def withdraw_money(self):
          while True:
                user_remove = input("Enter amount You want to withdraw :$")
                try:
                      amount = float(user_remove)
                      if amount <=0:
                            print("Amount must be higher than $0")
                      elif self.balance < amount:
                            print("Insufficient funds")
                      else:
                            self.balance -= amount
                            print(f"${amount} has been withdrawn from Your account. Account balance is ${self.balance}")
                            return self.balance
                except ValueError:
                      print("Invalid input")


class Interest(BankAccount):
      def __init__(self, name, balance, interest_rate):
            super().__init__(name, balance)
            self.interest_rate = interest_rate

      def add_interest(self):
            interest = self.interest_rate * self.balance
            self.balance = interest + self.balance
            print(f"You've earned an interest of ${interest}. Your account balance is ${self.balance}")
            return self.balance
            


def save_balance(account):
      account_data = {
            "name":account.name,
            "balance": account.balance,
            "interest_rate":account.interest_rate
      }
      with open("account.json", "w") as file:
            json.dump(account_data, file)
user = user = Interest(
    account_data["name"],
    account_data["balance"],
    account_data["interest_rate"]
)
user.add_money()
save_balance(user)
user.withdraw_money()
save_balance(user)
user.add_interest()
save_balance(user)