import ipywidgets as widgets
from IPython.display import display, clear_output

class ATM:
    def __init__(self, pin):
        self.balance = 0
        self.pin = pin
        self.transaction_history = []

    def check_pin(self, pin):
        return self.pin == pin

    def check_balance(self):
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdraw: ${amount}")
            return f"${amount} withdrawn. New balance: ${self.balance}"

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(f"Deposit: ${amount}")
        return f"${amount} deposited. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        if self.check_pin(old_pin):
            self.pin = new_pin
            self.transaction_history.append("PIN changed")
            return "PIN changed successfully"
        else:
            return "Incorrect old PIN"

    def get_transaction_history(self):
        return self.transaction_history if self.transaction_history else "No transactions yet"


# Widgets
account_input = widgets.Text(description="Account:")
pin_input = widgets.Password(description="PIN:")
amount_input = widgets.FloatText(description="Amount:")
output = widgets.Output()

# Accounts dictionary
accounts = {}

# Functions for each ATM action
def create_account(pin):
    account_number = account_input.value
    if account_number in accounts:
        with output:
            clear_output()
            print("Account number already exists.")
    else:
        accounts[account_number] = ATM(pin)
        with output:
            clear_output()
            print("Account created successfully.")

def check_balance(pin):
    account_number = account_input.value
    atm = accounts.get(account_number)
    if atm and atm.check_pin(pin):
        with output:
            clear_output()
            print(f"Your balance is: ${atm.check_balance()}")
    else:
        with output:
            clear_output()
            print("Incorrect account number or PIN.")

def deposit_money(pin, amount):
    account_number = account_input.value
    atm = accounts.get(account_number)
    if atm and atm.check_pin(pin):
        with output:
            clear_output()
            print(atm.deposit(amount))
    else:
        with output:
            clear_output()
            print("Incorrect account number or PIN.")

def withdraw_money(pin, amount):
    account_number = account_input.value
    atm = accounts.get(account_number)
    if atm and atm.check_pin(pin):
        with output:
            clear_output()
            print(atm.withdraw(amount))
    else:
        with output:
            clear_output()
            print("Incorrect account number or PIN.")

def change_pin(old_pin, new_pin):
    account_number = account_input.value
    atm = accounts.get(account_number)
    if atm:
        with output:
            clear_output()
            print(atm.change_pin(old_pin, new_pin))
    else:
        with output:
            clear_output()
            print("Incorrect account number or PIN.")

def view_transactions(pin):
    account_number = account_input.value
    atm = accounts.get(account_number)
    if atm and atm.check_pin(pin):
        with output:
            clear_output()
            print("Transaction history:")
            for transaction in atm.get_transaction_history():
                print(transaction)
    else:
        with output:
            clear_output()
            print("Incorrect account number or PIN.")


# Buttons
create_account_button = widgets.Button(description="Create Account")
check_balance_button = widgets.Button(description="Check Balance")
deposit_button = widgets.Button(description="Deposit Money")
withdraw_button = widgets.Button(description="Withdraw Money")
change_pin_button = widgets.Button(description="Change PIN")
view_transactions_button = widgets.Button(description="View Transactions")

# Button actions
create_account_button.on_click(lambda _: create_account(pin_input.value))
check_balance_button.on_click(lambda _: check_balance(pin_input.value))
deposit_button.on_click(lambda _: deposit_money(pin_input.value, amount_input.value))
withdraw_button.on_click(lambda _: withdraw_money(pin_input.value, amount_input.value))
change_pin_button.on_click(lambda _: change_pin(pin_input.value, amount_input.value))
view_transactions_button.on_click(lambda _: view_transactions(pin_input.value))

# Displaying the widgets
display(account_input, pin_input, amount_input, 
        create_account_button, check_balance_button, 
        deposit_button, withdraw_button, 
        change_pin_button, view_transactions_button, output)
