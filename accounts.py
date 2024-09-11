# accounts.py
class Account:
    """
    Base class for all types of bank accounts, including General and Special Accounts.
    This class contains the common functionality shared by all account types.

    Attributes:
        account_number (str): The unique account number associated with the account.
        password (str): The primary password required for authentication.
        balance (float): The amount of money in the account.
    """

    def __init__(self, account_number, password, balance):
        """
        Initializes an Account with the provided account number, password, and balance.

        Args:
            account_number (str): The unique identifier for the account.
            password (str): The password used to authenticate the account.
            balance (float): The initial balance in the account.
        """
        self.account_number = account_number
        self.password = password
        self.balance = balance
        self.transaction_history = []

    def check_password(self, password):
        """
        Validates the password by comparing it to the stored password.

        Args:
            password (str): The password to verify.

        Returns:
            bool: True if the password matches, False otherwise.
        """
        return self.password == password

    def deposit(self, amount):
        """
        Deposits a certain amount into the account and logs the transaction.

        Args:
            amount (float): The amount of money to deposit.

        Returns:
            str: Confirmation of the deposit transaction.
        """
        if amount <= 0:
            return "Deposit amount must be greater than zero."
        self.balance += amount
        self.transaction_history.append(f"Deposited {amount} Ksh.")
        return f"Successfully deposited {amount}. New balance is {self.balance}"

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the account if the balance is sufficient.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            str: Confirmation of the withdrawal transaction or an error if insufficient funds.
        """
        if amount <= 0:
            return "Withdrawal amount must be greater than zero."
        if amount > self.balance:
            return f"Insufficient funds. Balance is {self.balance}."
        self.balance -= amount
        self.transaction_history.append(f"Withdrew {amount} Ksh.")
        return f"Successfully withdrew {amount}. Remaining balance: {self.balance}"

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current balance of the account.
        """
        return self.balance

    def get_transaction_history(self):
        """
        Retrieves the transaction history of the account.

        Returns:
            list: A list of all transaction entries for the account.
        """
        if not self.transaction_history:
            return "No transactions have been made yet."
        return self.transaction_history

    def __str__(self):
        """
        Provides a string representation of the account, including the account number and balance.

        Returns:
            str: A summary of the account details.
        """
        return f"Account Number: {self.account_number}, Balance: {self.balance} Ksh."


class GeneralAccount(Account):
    """
    A class representing General Accounts, which have no minimum balance requirement and require only one password for authentication.
    """

    def __init__(self, account_number, password, balance):
        """
        Initializes a GeneralAccount instance with a unique account number, password, and balance.

        Args:
            account_number (str): The unique account number for the general account.
            password (str): The password used for authentication.
            balance (float): The initial balance of the account.
        """
        super().__init__(account_number, password, balance)
        print(f"General Account created with Account Number: {account_number}, Initial Balance: {balance}")

    def account_info(self):
        """
        Provides specific information about the general account.

        Returns:
            str: Information regarding the general account.
        """
        return f"General Account {self.account_number}: No minimum balance required."


class SpecialAccount(Account):
    """
    A class representing Special Accounts, which require two passwords and must maintain a minimum balance of 100,000 Ksh.
    """

    MINIMUM_BALANCE = 100000

    def __init__(self, account_number, password1, password2, balance):
        """
        Initializes a SpecialAccount instance with two passwords and a minimum balance requirement.

        Args:
            account_number (str): The unique account number for the special account.
            password1 (str): The primary password for authentication.
            password2 (str): The secondary password for authentication.
            balance (float): The initial balance of the account.
        """
        self.password2 = password2
        super().__init__(account_number, password1, balance)
        print(f"Special Account created with Account Number: {account_number}, Initial Balance: {balance}")

    def check_password(self, password1, password2):
        """
        Validates both primary and secondary passwords.

        Args:
            password1 (str): The primary password for authentication.
            password2 (str): The secondary password for authentication.

        Returns:
            bool: True if both passwords are correct, False otherwise.
        """
        return super().check_password(password1) and self.password2 == password2

    def withdraw(self, amount):
        """
        Withdraws a specified amount from the special account if the remaining balance stays above the minimum balance.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            str: Confirmation of the withdrawal transaction or an error if the balance is insufficient.
        """
        if self.balance - amount < SpecialAccount.MINIMUM_BALANCE:
            return f"Cannot withdraw {amount}. The balance cannot drop below the minimum of {SpecialAccount.MINIMUM_BALANCE} Ksh."
        return super().withdraw(amount)

    def account_info(self):
        """
        Provides specific information about the special account.

        Returns:
            str: Information regarding the special account.
        """
        return f"Special Account {self.account_number}: Minimum balance required is {self.MINIMUM_BALANCE} Ksh."
