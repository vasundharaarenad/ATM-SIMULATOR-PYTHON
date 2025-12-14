import time

# Account data
accounts = {
    7082: {"name": "vasundhara", "balance": 10000},
    6982: {"name": "spoorti", "balance": 8000},
    1703: {"name": "thrupthi", "balance": 12000}
}

# Store last transaction
last_transaction = {
    "type": None,
    "amount": 0,
    "time": None,
    "balance": 0
}

def current_time():
    return time.strftime("%d-%m-%Y  %H:%M:%S")

def check_balance(pin):
    print("Checking balance...")
    time.sleep(1)
    print("Balance: ₹", accounts[pin]["balance"])

def deposit(pin):
    amount = int(input("Enter deposit amount: ₹"))
    if amount > 0:
        accounts[pin]["balance"] += amount
        t = current_time()

        last_transaction["type"] = "Deposit"
        last_transaction["amount"] = amount
        last_transaction["time"] = t
        last_transaction["balance"] = accounts[pin]["balance"]

        print("Depositing...")
        time.sleep(1)
        print(f"₹{amount} deposited successfully")
        print("Date & Time:", t)
    else:
        print("Invalid amount")

def withdraw(pin):
    amount = int(input("Enter withdrawal amount: ₹"))
    if amount > 0 and amount <= accounts[pin]["balance"]:
        accounts[pin]["balance"] -= amount
        t = current_time()

        last_transaction["type"] = "Withdraw"
        last_transaction["amount"] = amount
        last_transaction["time"] = t
        last_transaction["balance"] = accounts[pin]["balance"]

        print("Processing withdrawal...")
        time.sleep(1)
        print(f"₹{amount} withdrawn successfully")
        print("Date & Time:", t)
    else:
        print("Insufficient balance or invalid amount")

def print_receipt(pin):
    if last_transaction["type"] is None:
        print("No transaction done yet")
    else:
        print("\n----- ATM RECEIPT -----")
        print("Name:", accounts[pin]["name"])
        print("Transaction:", last_transaction["type"])
        print("Amount: ₹", last_transaction["amount"])
        print("Date & Time:", last_transaction["time"])
        print("Available Balance: ₹", last_transaction["balance"])
        print("----------------------")

def atm_menu(pin):
    while True:
        print("\n------ MENU ------")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Print Receipt")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            check_balance(pin)
        elif choice == 2:
            deposit(pin)
        elif choice == 3:
            withdraw(pin)
        elif choice == 4:
            print_receipt(pin)
        elif choice == 5:
            print("Thank you for using ATM")
            time.sleep(1)
            break
        else:
            print("Invalid choice")

# -------- MAIN PROGRAM --------
print("===== Welcome to ATM =====")
time.sleep(1)

attempts = 0
MAX_ATTEMPTS = 3

while attempts < MAX_ATTEMPTS:
    pin = int(input("Enter your PIN: "))

    if pin in accounts:
        print(f"Welcome {accounts[pin]['name']}")
        time.sleep(1)
        atm_menu(pin)
        break
    else:
        attempts += 1
        print("Invalid PIN")
        print(f"Attempts left: {MAX_ATTEMPTS - attempts}")

        if attempts == MAX_ATTEMPTS:
            print("\n❌ Card Blocked due to 3 wrong attempts")
            print("Please contact your bank")
            time.sleep(2)