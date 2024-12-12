# BankingProgram
Create a Banking Program
Banking Program Algorithm
1. Initialize Banking Program
●
The Bank Manager Object:
○
This where the program starts from, and handles the user-driven
operations selected from the main menu.
○
Create a Bank Object:
◆
A bank system with a limit of 100 accounts stored in a list.
●
Main Menu and User Interaction
○
The main method should continuously present a menu with options:
1.
Open an account
2.
Get account information and balance
3.
Change PIN
4.
Deposit money in account
5.
Transfer money between accounts
6.
Withdraw money from account
7.
ATM withdrawal
8.
Deposit change
9.
Close an account
10.
Add monthly interest to all accounts
11.
Exit program
2. Account Management
●
Create an Account (Menu Option 1):
○
Request user to enter first name, last name, and SSN.
○
Validate SSN.
○
Generate a random account number and PIN for the new account.
○
Add the new account to the bank system (find an empty slot in the
account list).
●
Retrieve Account Info and Balance (Menu Option 2):
○
Prompt for account number and PIN.
○
Validate the PIN, then display account information.
○
SSN should be displayed, but masked except for last 4 digits.
●
Change Account PIN (Menu Option 3):
○
Prompt for account number.
○
Prompt for PIN (validate).
○
Allow the user to enter and re-enter (confirm) a new PIN
●
Close Account (Menu Option 9):
○
Prompt for account number and PIN.
○
If valid, remove the account from the bank's account list.
3. Available Transactions
●
Deposit Money (Menu Option 4):
○
Prompt user for account number and PIN and validate
○
Prompt user for amount to deposit and validate
○
Convert the amount to cents and update account balance.
●
Withdraw Money (Menu Option 5):
○
Prompt user for account number and PIN.
○
Prompt user for amount to withdraw and validate (positive amount).
○
Ensure sufficient funds are available then deduct the amount from the
account.
●
Transfer Money Between Accounts (Menu Option 6):
○
Prompt for the source account number and PIN.
○
Prompt for the target account number and ensure it exists.
○
Prompt for transfer amount, validate it, and ensure sufficient funds in
the source account.
○
Transfer the funds by updating both accounts' balances.
4. ATM and Coin Collection
Operations:
●
ATM Withdrawal (Menu Option 7):
○
Prompt for account number and PIN.
○
Allow withdrawal of money in multiples of $5, up to $1000.
○
Print the breakdown of the withdrawal in $20, $10, and $5 bills.
○
Deduct the amount withdrawn in cents from the account balance.
●
Deposit Change (Menu Option 8):
○
Prompt for account number and PIN.
○
Ask the user for a string representing coin types (P for Penny, Q for
Quarter etc).
○
Parse the coin string and update the account balance by converting
the total to cents.
5. Applying Interest (Menu Option 10)
Operation:
●
Add Monthly Interest:
○
Prompt for the annual interest rate (percentage).
○
Convert the annual rate to a monthly rate.
○
Compute the monthly interest for each account and update the
balance.
6. Exit Program (Menu Option 11)
Operation:
●
Terminate program, display exit message.
