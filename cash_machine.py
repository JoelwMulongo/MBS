# cash_machine.py
from bank import MiniBank

class CashMachine:
    """
    A class representing the cash machine that allows account holders to withdraw money and check balances.
    
    Attributes:
        bank (MiniBank): The MiniBank object that holds all accounts.
    """
    
    def __init__(self, bank):
        """
        Initializes the cash machine with a reference to the bank.

        Args:
            bank (MiniBank): The bank that holds all account information.
        """
        self.bank = bank

    def authenticate_and_withdraw(self, account_number, password1, password2=None, amount=None):
        """
        Authenticates the user and either performs a withdrawal or shows the balance.

        Args:
            account_number (str): The account number of the user.
            password1 (str): The first password for authentication.
            password2 (str, optional): The second password for special accounts.
            amount (float, optional): The amount to withdraw, or None to check balance.

        Returns:
            str: A message indicating whether the transaction was successful.
        """
        account = self.bank.find_account(account_number)

        if isinstance(account, GeneralAccount):
            if account.check_password(password1):
                if amount is None:
                    return f"Balance: {account.get_balance()} Ksh."
                else:
                    return account.withdraw(amount)
            else:
                return "Authentication failed. Incorrect password."

        elif isinstance(account, SpecialAccount):
            if account.check_password(password1, password2):
                if amount is None:
                    return f"Balance: {account.get_balance()} Ksh."
                else:
                    return account.withdraw(amount)
            else:
                return "Authentication failed. Incorrect password(s)."
        else:
            return "Account not found."

    def display_account_balance(self, account_number, password1, password2=None):
        """
        Displays the balance of the account after authenticating.

        Args:
            account_number (str): The account number.
            password1 (str): The first password for authentication.
            password2 (str, optional): The second password for special accounts.

        Returns:
            str: Balance information or an authentication error.
        """
        return self.authenticate_and_withdraw(account_number, password1, password2)

    def perform_withdrawal(self, account_number, password1, password2, amount):
        """
        Performs a withdrawal after authenticating.

        Args:
            account_number (str): The account number.
            password1 (str): The first password for authentication.
            password2 (str, optional): The second password for special accounts.
            amount (float): The amount to withdraw.

        Returns:
            str: Transaction result or authentication error.
        """
        return self.authenticate_and_withdraw(account_number, password1, password2, amount)
