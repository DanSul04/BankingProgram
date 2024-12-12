import random # Several uses for random import

# Account class
class Account:
    def __init__(self, first_name, last_name, ssn):
        # Random 8 digit account number not starting with 0
        self.account_number = random.randint(10000000, 99999999)
        
        # Account owner details, PIN and balance
        self.owner_first_name = first_name
        self.owner_last_name = last_name
        self.ssn = ssn  
        self.pin = self.generate_pin()
        self.balance = 0

    # Random 4-digit PIN
    def generate_pin(self):
        return str(random.randint(0, 9999)).zfill(4)

    # Getter and setter for account number
    def get_account_number(self):
        return self.account_number

    def set_account_number(self, number):
        self.account_number = number

    # Getter and setter for owner first name
    def get_owner_first_name(self):
        return self.owner_first_name

    def set_owner_first_name(self, first_name):
        self.owner_first_name = first_name

    # Getter and setter for owner last name
    def get_owner_last_name(self):
        return self.owner_last_name

    def set_owner_last_name(self, last_name):
        self.owner_last_name = last_name

    # Getter and setter for SSN
    def get_ssn(self):
        return self.ssn

    def set_ssn(self, ssn):
        self.ssn = ssn

    # Getter and setter for PIN
    def get_pin(self):
        return self.pin

    def set_pin(self, pin):
        self.pin = pin

    # Getter and setter for balance
    def get_balance(self):
        return self.balance

    def set_balance(self, balance):
        self.balance = balance

    # Deposit funds
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        return self.balance

    # Withdraw funds
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self.balance

    # PIN Validation, check for match
    def isValidPIN(self, pin):
        return self.pin == pin

    '''toString method, returns names and
    values in a formatted string'''
    def to_string(self):
        # Format balance as dollars (converts from cents)
        formatted_balance = f"${self.balance / 100:.2f}"
        return (f"Account Number: {self.account_number}\n"
                f"Owner First Name: {self.owner_first_name}\n"
                f"Owner Last Name: {self.owner_last_name}\n"
                f"Owner SSN: XXX-XX-{self.ssn[-4:]}\n"  # For
                f"PIN: {self.pin}\n"
                f"Balance: {formatted_balance}")

# Bank Class
class Bank:
    MAX_ACCOUNTS = 100

    def __init__(self):
        # Initialize accounts list
        self.accounts = [None] * Bank.MAX_ACCOUNTS

    def addAccountToBank(self, account):
        """Add an account to the bank: iterate through all
        the accounts in the list until it finds an empty index (None)"""
        for i in range(Bank.MAX_ACCOUNTS):
            if self.accounts[i] is None:
                self.accounts[i] = account
                return True
        print("Max Account Limit Reached.")
        return False

    def removeAccountFromBank(self, account):
        for i in range(Bank.MAX_ACCOUNTS):
            if self.accounts[i] and self.accounts[i].get_account_number() == account.get_account_number():
                self.accounts[i] = None 
                return True
        print("Account not found.")
        return False

    def findAccount(self, account_number):
        """Find an account by account number."""
        for account in self.accounts:
            if account and account.get_account_number() == int(account_number):
                return account
        return None  # Return None to indicate account is not found

    def addMonthlyInterest(self, annual_rate):
        """Add monthly interest to all accounts."""
        monthly_rate = annual_rate / 12 / 100  # Convert annual rate to monthly rate
        for account in self.accounts:
            if account:
                # Calculate the interest and add it to the balance (in cents)
                interest = account.get_balance() * monthly_rate
                '''iterate through all the accounts and deposit
                    a monthly interest payment into every account'''
                account.deposit(int(interest))  # Deposit the interest into the account

# Coin Collector Class
class CoinCollector:
    
    @staticmethod
    def parseChange(change):
        total_cents = 0
        
        # Loop through each character in the input string
        for coin in change:
            if coin == 'P':
                total_cents += 1  # Penny
            elif coin == 'N':
                total_cents += 5  # Nickel
            elif coin == 'D':
                total_cents += 10  # Dime
            elif coin == 'Q':
                total_cents += 25  # Quarter
            elif coin == 'H':
                total_cents += 50  # Half-dollar
            elif coin == 'W':
                total_cents += 100  # Whole dollar
            else:
                # If the character is invalid, raise an error
                raise ValueError(f"Invalid coin: {coin}")
        
        # Return the total amount in cents
        return total_cents

   
# BankUtility class
class BankUtility:
    
    # Method to check if a string is numeric
    @staticmethod
    def isNumeric(numberToCheck):
        try:
            if numberToCheck.isdigit():
                return True
            else:
                return False
        except ValueError:
            return False

    # Prompt the user for a string and return the input
    @staticmethod
    def promptUserForString(prompt):
        user_input = input(prompt)
        return user_input
    
    # Prompt the user for a positive number
    @staticmethod
    def promptUserForPositiveNumber(prompt):
        while True:
            try:
                user_input = float(input(prompt))
                if user_input <= 0:
                    print("Amount cannot be negative. Try again.")
                else:
                    return user_input
            except ValueError:
                print("Please enter a valid number.")
    
    # Dollars to cents method
    @staticmethod
    def convertFromDollarsToCents(dollars):
        return int(dollars * 100)
    
    # Generate random integer method
    @staticmethod
    def generateRandomInteger(min_value, max_value):
        return random.randint(min_value, max_value)


class BankManager:
    def __init__(self):
        # Create an instance of the Bank object
        self.bank = Bank()

    # Main method to run the program
    def main(self):
        while True:
            print("\n============================================================")
            print("What do you want to do?")
            print("1. Open an account")
            print("2. Get account information and balance")
            print("3. Change PIN")
            print("4. Deposit money in account")
            print("5. Transfer money between accounts")
            print("6. Withdraw money from account")
            print("7. ATM withdrawal")
            print("8. Deposit change")
            print("9. Close an account")
            print("10. Add monthly interest to all accounts")
            print("11. End Program")
            print("============================================================")
            
            choice = input("Enter choice (1-11): ")

            if choice == '1':
                self.openAccount()
            elif choice == '2':
                self.getAccountInfo()
            elif choice == '3':
                self.changePIN()
            elif choice == '4':
                self.depositMoney()
            elif choice == '5':
                self.transferMoney()
            elif choice == '6':
                self.withdrawMoney()
            elif choice == '7':
                self.atmWithdrawal()
            elif choice == '8':
                self.depositChange()
            elif choice == '9':
                self.closeAccount()
            elif choice == '10':
                self.addMonthlyInterest()
            elif choice == '11':
                print("Exiting the banking program")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 11.")

    # Prompt for account number and PIN
    @staticmethod
    def promptForAccountNumberAndPIN(bank):
        while True:
            account_number = BankUtility.promptUserForString("Enter account number: ")
        
            # Check if the entered account number is a valid numeric string
            if not account_number.isdigit():
                print("Invalid account number. Please enter a valid numeric account number.")
                continue
        
            # Try to find the account in the bank system
            account = bank.findAccount(account_number)
    
            # Check if the account exists
            if not account:
                print(f"Account not found for account number: {account_number}")
                continue  # Prompt again if the account doesn't exist
        
            pin = BankUtility.promptUserForString("Enter PIN: ")
        
            if not account.isValidPIN(pin):
                print("Invalid PIN")
                return None
        
            return account

    # Open a new account
    def openAccount(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        # SSN validation
        while True:
            ssn = input("Enter SSN (9 digits): ")
            if len(ssn) == 9 and ssn.isdigit():
                break  # Valid SSN
            else:
                print("Social Security Number must be 9 digits. Please try again.")

        # Create the new account
        new_account = Account(first_name, last_name, ssn)
        if self.bank.addAccountToBank(new_account):
            print(f"Account created successfully! Account number: {new_account.get_account_number()}")
            print(f"Your PIN: {new_account.get_pin()}")  # Display the PIN in this case
        else:
            print("Failed to create account.")

    # Get account info and balance
    def getAccountInfo(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            print(account.to_string())

    # Change PIN
    def changePIN(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            while True:
                new_pin = BankUtility.promptUserForString("Enter new PIN: ")

                if len(new_pin) != 4 or not new_pin.isdigit():
                    print("Invalid PIN. Please try again.")
                    continue  # Ask for the PIN again if it’s not valid
            
            # Confirm new PIN with additional user input
                confirm_pin = BankUtility.promptUserForString("Confirm new PIN: ")

            # Check if the two PINs match
                if new_pin == confirm_pin:
                    account.set_pin(new_pin)
                    print("PIN changed successfully.")
                    break  # Exit the loop after successfully changing the PIN
                else:
                    print("The PINs do not match. Please try again.")


    # Deposit money into an account
    def depositMoney(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to deposit: ")
            cents = BankUtility.convertFromDollarsToCents(amount)
            account.deposit(cents)
            print(f"Deposited ${amount}. New balance: ${account.get_balance() / 100:.2f}")

    # Transfer money between accounts
    def transferMoney(self):
        account_from = self.promptForAccountNumberAndPIN(self.bank)
        if not account_from:
            return
        
        account_to_number = input("Enter the account number to transfer to: ")
        account_to = self.bank.findAccount(account_to_number)
        
        if not account_to:
            print("Account not found.")
            return
        
        amount = BankUtility.promptUserForPositiveNumber("Enter amount to transfer: ")
        cents = BankUtility.convertFromDollarsToCents(amount)
        
        if account_from.get_balance() >= cents:
            account_from.withdraw(cents)
            account_to.deposit(cents)
            print(f"Transferred ${amount} from account {account_from.get_account_number()} to account {account_to.get_account_number()}.")
        else:
            print("Insufficient funds.")

    # Withdraw money from an account
    def withdrawMoney(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw: ")
            cents = BankUtility.convertFromDollarsToCents(amount)
            account.withdraw(cents)
            print(f"Withdrew ${amount}. New balance: ${account.get_balance() / 100:.2f}")

    # ATM withdrawal
    def atmWithdrawal(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            amount = BankUtility.promptUserForPositiveNumber("Enter amount to withdraw in dollars (no cents) in multiples of $5 (limit $1000):")
                # Check if amount is valid for ATM withdrawl
            if amount < 5 or amount > 1000 or amount % 5 != 0:
                print("Invalid amount. Try again.")
                return
            # Store original amount for withdrawl later
            original_amount = amount
            
            # Calculate number of bills
            twenties = amount // 20
            amount %= 20
            tens = amount // 10
            amount %= 10
            fives = amount // 5
            print(f"Number of 20-dollar bills: {twenties}")
            print(f"Number of 10-dollar bills: {tens}")
            print(f"Number of 5-dollar bills: {fives}")
            
            # Convert dollars to cents
            cents = BankUtility.convertFromDollarsToCents(original_amount)
            
            account.withdraw(cents)
            
            # Print remaining balance
            print(f"New balance: ${account.get_balance() / 100:.2f}")

    

    # Deposit change
    def depositChange(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            change = input("Deposit coins: ")
            try:
                change_in_cents = CoinCollector.parseChange(change)
                account.deposit(change_in_cents)
                print(f"Deposited {change_in_cents / 100:.2f} into account. New balance: ${account.get_balance() / 100:.2f}")
            except ValueError as e:
                print(f"Invalid Coin: {e}")

    # Close an account
    def closeAccount(self):
        account = self.promptForAccountNumberAndPIN(self.bank)
        if account:
            if self.bank.removeAccountFromBank(account):
                print(f"Account {account.get_account_number()} closed successfully.")
            else:
                print("Failed to close account.")

    # Add monthly interest to all accounts 
    def addMonthlyInterest(self):
        annual_rate = float(input("Enter annual interest rate percentage: "))
        monthly_rate = annual_rate / 12
        self.bank.addMonthlyInterest(annual_rate)
        print(f"Added monthly interest at rate of {monthly_rate:.2f}% to all accounts.")

if __name__ == "__main__":
    manager = BankManager()
    manager.main()
