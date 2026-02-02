def withdraw_money(current_balance, withdrawal_amount):

  """

  Simulates a bank withdrawal.

  Args:

    current_balance: The current amount of money in the account.

    withdrawal_amount: The amount the customer wants to withdraw.

  Returns:

    A tuple containing the new balance and a message.

    (new_balance, message)

  """

  if withdrawal_amount <= 0:

    return current_balance, "Withdrawal amount must be positive."

  elif withdrawal_amount > current_balance:

    return current_balance, "Insufficient funds!"

  else:

    new_balance = current_balance - withdrawal_amount

    return new_balance, f"Withdrawal successful! New balance: ${new_balance:.2f}"

#  Example Usage 

account_balance = 500.00

print(f"Initial balance: ${account_balance:.2f}")

# Successful withdrawal

amount_to_withdraw_1 = 100.00

account_balance, message = withdraw_money(account_balance, amount_to_withdraw_1)

print(message)

print(f"Balance after withdrawal 1: ${account_balance:.2f}\n")

# Attempt to withdraw more than available

amount_to_withdraw_2 = 600.00

account_balance, message = withdraw_money(account_balance, amount_to_withdraw_2)

print(message)

print(f"Balance after withdrawal 2: ${account_balance:.2f}\n")

# Attempt to withdraw a negative amount

amount_to_withdraw_3 = -50.00

account_balance, message = withdraw_money(account_balance, amount_to_withdraw_3)

print(message)

print(f"Balance after withdrawal 3: ${account_balance:.2f}\n")

# Another successful withdrawal

amount_to_withdraw_4 = 25.50

account_balance, message = withdraw_money(account_balance, amount_to_withdraw_4)

print(message)

print(f"Balance after withdrawal 4: ${account_balance:.2f}\n")