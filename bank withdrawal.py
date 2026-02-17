def withdraw_money(current_balance, withdrawal_amount):
  if withdrawal_amount <= 0:

    return current_balance, "Withdrawal amount must be positive."

  elif withdrawal_amount > current_balance:

    return current_balance, "Insufficient funds!"

  else:

    new_balance = current_balance - withdrawal_amount

    return new_balance, f"Withdrawal successful! New balance: ${new_balance:.2f}"

#  Example Usage 

current_balance = 500.00

print(f"Initial balance: ${current_balance:.2f}")

# Successful withdrawal

withdrawal_amount = int(input("Enter the amount to withdraw"))

current_balance, message = withdraw_money(current_balance, withdrawal_amount)

print(message)

print(f"Balance after withdrawal 1: ${current_balance:.2f}\n")