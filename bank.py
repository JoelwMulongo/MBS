# bank.py
from accounts import GeneralAccount, SpecialAccount

class MiniBank:
    """
    MiniBank class that manages general and special accounts. It allows account holders to perform deposits, withdrawals, and balance inquiries.
    """

    def __init__(self):
        """
        Initializes the MiniBank with 10 General and 10 Special accounts, each with default balances and passwords.
        """
        self.accounts = self._initialize_accounts()

    def _initialize_accounts(self):
        """
        Creates and initializes 10 general and 10 special accounts.

        Returns:
            list: A list containing 20 account objects (10 general, 10 special).
        """
        accounts = []
        # Create General Accounts
        for i in range(10):
            accounts.append(GeneralAccount(f"GA{i+1}", f"pass{i+1}", 10000 + i * 1000))
        
        # Create Special Accounts
        for i in range(10, 20):
            accounts.append(SpecialAccount(f"SA{i+1}", f"pass1{i+1}", f"pass2{i+1}", 200000 + i * 10000))

        return accounts

    def find_account(self, account_number):
        """
        Searches for an account using the account number.

        Args:
            account_number (str): The account number to search for.

        Returns:
            Account: The account object if found, or None if no match is found.
        """
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def display_accounts(self):
        """
        Displays all the accounts in the bank.
        """
        print("\nList of All Accounts in the Bank:")
        for account in self.accounts:
            print(account)

    def total_bank_balance(self):
        """
        Calculates and returns the total balance of all accounts in the bank.

        Returns:
            float: The total balance of all accounts in the bank.
        """
        total_balance = sum(account.get_balance() for account in self.accounts)
        return total_balance
