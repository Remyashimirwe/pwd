
def atm(balance,withdraw):
      if withdraw <= balance:
            print("Allowed")
            new_balance = balance - withdraw
            print("Your new balance is: ",new_balance)
      else:
            
            print("insurficient fund !!")
balance = int(input("Enter the balance: "))
withdraw = int(input("Enter Withdrawal money: "))
result = atm(balance, withdraw)
print(result)