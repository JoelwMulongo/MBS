# main.py
from bank import MiniBank
from cash_machine import CashMachine

def main():
    """
    Main driver function for the bank system, which allows users to interact with the cash machine.
    """
    # Initialize the bank and cash machine
    bank = MiniBank()
    cash_machine = CashMachine(bank)

    while True:
        print("\n--- Welcome to MiniBank ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Display All Accounts")
        print("4. Show Total Bank Balance")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            account_number = input("Enter account number: ")
            password1 = input("Enter password: ")
            password2 = None
            if account_number.startswith("SA"):
                password2 = input("Enter second password: ")
            print(cash_machine.display_account_balance(account_number, password1, password2))

        elif choice == "2":
            account_number = input("Enter account number: ")
            password1 = input("Enter password: ")
            password2 = None
            if account_number.startswith("SA"):
                password2 = input("Enter second password: ")
            amount = float(input("Enter amount to withdraw: "))
            print(cash_machine.perform_withdrawal(account_number, password1, password2, amount))

        elif choice == "3":
            bank.display_accounts()

        elif choice == "4":
            print(f"Total bank balance: {bank.total_bank_balance()} Ksh.")

        elif choice == "5":
            print("Thank you for using MiniBank. Goodbye!")
            break

        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
