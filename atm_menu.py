

balance = 1000

print("ATM Menu")
print("1. Check Balance")
print("2. Withdraw")
print("3. Deposit")

choice = input("Enter your choice (1-3): ")

if choice == "1":
    print(f"Your balance is: ${balance:.2f}")

elif choice == "2":
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Error: Amount must be greater than 0.")
    elif amount > balance:
        print("Error: Insufficient funds.")
    else:
        balance -= amount
        print(f"Withdrawal successful. New balance: ${balance:.2f}")

elif choice == "3":
    amount = float(input("Enter deposit amount: "))

    if amount <= 0:
        print("Error: Amount must be greater than 0.")
    else:
        balance += amount
        print(f"Deposit successful. New balance: ${balance:.2f}")

else:
    print("Error: Invalid choice.")















