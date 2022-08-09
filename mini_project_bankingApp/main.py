william = 100000
adeola = 20000
josephine = 1000000
olumide = 50000
hamzat = 500000

print('Good morning! \nYou are welcome to UNILAG DS Bank \nPress the number corresponding to what you would like to '
      'do today:')
option = input('1. Withdraw \n2. Deposit \n3. Transfer \n4. Forex \n5. ATM Card acquisition \n6. Loan \nResponse:')

choice = int(option)
if choice == 1:
    Account_name = input('What is your account name? ')
    Amount = eval(input('How much would you like to withdraw? '))
    # Amount = int(Amount)
    if Account_name == "hamzat":
        Balance = hamzat
    elif Account_name == "william":
        Balance = william
    elif Account_name == "olumide":
        Balance = olumide
    elif Account_name == "josephine":
        Balance = josephine
    elif Account_name == "adeola":
        Balance = adeola
    else:
        print('Account does not exist!')
    while Amount > Balance:
        print("You don't have that much money")
        newAmount = eval(input('Enter a lower amount!:'))
        Amount = newAmount
    print("Here is your cash of", Amount)
    newBal = Balance + Amount
    print('\n Your new account balance is ', newBal)

if choice == 2:
    Account_name = input('What is your account name? ')
    Amount = eval(input('How much would you like to deposit? '))
    # Amount = int(Amount)
    if Account_name == "hamzat":
        Balance = hamzat
    elif Account_name == "william":
        Balance = william
    elif Account_name == "olumide":
        Balance = olumide
    elif Account_name == "josephine":
        Balance = josephine
    elif Account_name == "adeola":
        Balance = adeola
    else:
        print('Account does not exist!')

    while Amount < 0:
        print('This entry is invalid, try again!')
        newAmount = eval(input('Enter a higher value:'))
        Amount = newAmount
    print("Amount accepted!")
    newBal = Balance + Amount
    print('\n Your new account balance is ', newBal)

if choice == 3:
    Account_name = input('What is your account name? ')
    Amount = eval(input('How much would you like to transfer? '))
    Recipient = input('Who do you want to transfer to?:')  #beneficiary
    if Account_name == "hamzat":
        Balance = hamzat
    elif Account_name == "william":
        Balance = william
    elif Account_name == "olumide":
        Balance = olumide
    elif Account_name == "josephine":
        Balance = josephine
    elif Account_name == "adeola":
        Balance = adeola
    else:
        print('Account does not exist!')

    while Account_name == Recipient:
        print('Invalid beneficiary choice!')
        newRecipient = input('Enter a new recipient:')
        Recipient = newRecipient

    print('Transfer successful!')
    NewBal = Balance - Amount
    print('Your new account balance is', NewBal)

    if Recipient == "hamzat":
        newBalance = hamzat+Amount
    elif Recipient == "william":
        newBalance = william+Amount
    elif Recipient == "olumide":
        newBalance = olumide+Amount
    elif Recipient == "josephine":
        newBalance = josephine+Amount
    elif Recipient == "adeola":
        newBalance = adeola+Amount
    else:
        print(' Beneficiary does not exist!')
    print(Recipient, 'new balance is:', newBalance)

if choice == 4:
    Account_name = input('Welcome to the new FOREX exchange division! \nWhat is your account name? ')
    Currency = input('What currency are you exchanging in?')
    Amount = eval(input('How much would you like to change? '))
    if Account_name == "hamzat":
        Balance = hamzat
    elif Account_name == "william":
        Balance = william
    elif Account_name == "olumide":
        Balance = olumide
    elif Account_name == "josephine":
        Balance = josephine
    elif Account_name == "adeola":
        Balance = adeola
    else:
        print('Account does not exist!')

    if Currency == "USD":
        #N700 to $1
        Exchange = Amount / 700
    elif Currency == "GBP":
        #N800 to &1
        Exchange = Amount / 800
    elif Currency == "Yuan":
        #N1 to 0.37Y
        Exchange = Amount*0.37
    else:
        print('Invalid entry!')

    while Amount > Balance:
        print('Insufficient funds for conversion!')
        newAmount = eval(input('Enter a new amount:'))
        Amount = newAmount
    print('You have successfully converted N', Amount, 'into', Exchange, Currency)
    newBal = Balance - Amount
    print('You have', newBal, 'left.')

if choice == 5:
    Account_name = input('What is your account name? ')
    cardFee = 500

    print('Here is your new card. New card fee is:', cardFee)
    newBal = Balance - cardFee

if choice == 6: #loan
    Account_name = input('What is your account name? ')
    lend = eval(input('How much would you like to borrow?'))
    #for every N1 borrowed there is an interest of 0.05
    loan = lend + lend*0.05
    if Account_name == "hamzat":
        Balance = hamzat
    elif Account_name == "william":
        Balance = william
    elif Account_name == "olumide":
        Balance = olumide
    elif Account_name == "josephine":
        Balance = josephine
    elif Account_name == "adeola":
        Balance = adeola
    else:
        print('Account does not exist!')

    print('Your new balance is:', Balance+lend)
    print('You are to pay back', loan)



