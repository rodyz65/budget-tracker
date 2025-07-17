import json
import os

def add_transaction(transactions):
    while True:
        try:
            amount = float(input("An amount for the transaction. Positive if it is income or negative if it is an expense: "))
            break
        except ValueError:
            print("Invalid amount. Please enter a number.")
    transaction_name = input("The name of the transaction: ")
    transactions.append({"Name": transaction_name, "Amount": amount})
def view_balance(transactions):
    balance = sum(t["Amount"] for t in transactions)
    print(f"Your current balance is: ${balance:.2f}")
def view_transactions(transactions):
    if not transactions:
        print("No transactions found.")
    else:
        print("Transactions:")
        for t in transactions:
            print(f"{t['Name']}: ${t['Amount']:.2f}")
def delete_transaction(transactions):
    if not transactions:
        print("No transactions to delete.")
        return
    print('Transactions:')
    for i,t in enumerate(transactions):
        print(f"{i}. {t['Name']}: ${t['Amount']:.2f}")

    try:
        choice = int(input("Enter the number of the transaction you want to delete: "))
        if 0 <= choice < len(transactions):
            deleted = transactions.pop(choice)
            print(f"Deleted transaction: {deleted['Name']}: ${deleted['Amount']:.2f}")
        else:
            print("Invalid choice. No transaction deleted.")
    except ValueError:
        print("Invalid input. Please enter a number.")
def delete_all_transactions(transactions):
    confirmation = input("Are you sure that you want to delete all transactions? (y/n):")
    if confirmation.lower() == 'y':
        transactions.clear()
        print("All transactions have been deleted.")
        save_transactions(transactions)
    else:
        print('Delete all attempt canceled.')
TRANSACTION_FILE = "transactions.json"
def load_transactions():
    """This function loads transactions from a JSON file."""
    if os.path.exists(TRANSACTION_FILE):
        with open(TRANSACTION_FILE, "r") as file:
            return json.load(file)
    else:
        return []
def save_transactions(transactions):
    """This function saves transactions to a JSON file."""
    with open(TRANSACTION_FILE, "w") as file:
        json.dump(transactions, file, indent=4)
def main():
    print("Hello! Welcome to the budget tracking script!")
    transactions = load_transactions()
    while True:
        print("Main Menu:\n")
        print("1. Add a transaction")
        print("2. View balance")
        print("3. View transactions")
        print("4. Delete a transaction")
        print("5. Delete all transactions")
        print("6. Exit")
        decision = input("Please enter your choice (1-6):")
        if decision == '1':
            add_transaction(transactions)
            save_transactions(transactions)
        elif decision == '2':
            view_balance(transactions)
        elif decision == '3':
            view_transactions(transactions)
        elif decision == '4':
            delete_transaction(transactions)
            save_transactions(transactions)
        elif decision == '5':
            delete_all_transactions(transactions)
        elif decision == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()   
