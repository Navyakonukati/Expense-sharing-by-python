class ExpenseSharingApp:
    def __init__(self):
        self.users = {}
        self.expenses = []

    def add_user(self, name):
        if name not in self.users:
            self.users[name] = 0

    def record_expense(self, payer, amount, beneficiaries):
        if payer not in self.users:
            print(f"{payer} is not a registered user.")
            return

        total_beneficiaries = len(beneficiaries)
        if total_beneficiaries == 0:
            print("Please specify at least one beneficiary.")
            return

        split_amount = amount / (total_beneficiaries + 1)
        self.users[payer] -= amount

        for beneficiary in beneficiaries:
            if beneficiary not in self.users:
                print(f"{beneficiary} is not a registered user.")
                return
            self.users[beneficiary] += split_amount

        self.expenses.append((payer, amount, beneficiaries))

    def print_balance(self):
        print("Balance:")
        for user, balance in self.users.items():
            print(f"{user}: {balance}")

    def simplify_debts(self):
        debts = {}
        for user, balance in self.users.items():
            if balance > 0:
                debts[user] = balance
            elif balance < 0:
                for creditor, amount in debts.items():
                    if amount >= abs(balance):
                        debts[creditor] -= abs(balance)
                        self.users[user] = 0
                        print(f"{user} owes {creditor} {abs(balance)}")
                        break
                    else:
                        self.users[user] += amount
                        debts[creditor] = 0
                        print(f"{user} owes {creditor} {amount}")
                        balance += amount
                        if balance == 0:
                            break

# Example usage:
app = ExpenseSharingApp()
app.add_user("Alice")
app.add_user("Bob")
app.add_user("Charlie")

app.record_expense("Alice", 100, ["Bob", "Charlie"])
app.record_expense("Bob", 50, ["Alice"])
app.record_expense("Charlie", 30, ["Bob"])

app.print_balance()
print("Simplified Debts:")
app.simplify_debts()