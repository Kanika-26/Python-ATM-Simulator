
print("===== ATM SIMULATOR =====")

bal = 78000
correct_pin = 1426
transactions = []

attempts = 0
while attempts < 3:
    pin = input("Enter your PIN: ")

    if pin.isdigit() and int(pin) == correct_pin:  #correct credentials
        print("Login successful!")
        break
    else:
        attempts += 1
        print("Incorrect PIN!")  #incorrect credentials

if attempts == 3:
    print("Too many incorrect attempts. Exiting.") #exits on reaching limits
else:
    while True:
        print("===== ATM MENU =====")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Deposit Money")
        print("4. Change PIN")
        print("5. Other Enquiry")
        print("6. Transaction History")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Current balance:", bal)

        elif choice == "2":
            amount = input("Enter amount to withdraw: ")

            if not amount.isdigit() or int(amount) <= 0:
                print("Enter a valid positive amount!")
            else:
                amount = int(amount)

                if amount <= bal:
                    bal -= amount
                    transactions.append(
                        f"Withdrawn: Rs. {amount}"
                    )
                    print("Withdrawal successful!")
                    print("Remaining balance:", bal)
                else:
                    print("Insufficient balance!")

        elif choice == "3":
            amount = input("Enter amount to deposit: ")

            if not amount.isdigit() or int(amount) <= 0:
                print("Enter a valid positive amount!")
            else:
                amount = int(amount)
                bal += amount
                transactions.append(
                    f"Deposited: Rs. {amount}"
                )
                print("Deposit successful!")
                print("Updated balance:", bal)

        elif choice == "4":
            old_pin = input("Enter current PIN: ")

            if old_pin.isdigit() and int(old_pin) == correct_pin:
                new_pin = input("Enter new 4-digit PIN: ")

                if new_pin.isdigit() and len(new_pin) == 4:
                    correct_pin = int(new_pin)
                    print("PIN changed successfully!")
                else:
                    print("PIN must contain exactly 4 digits.")
            else:
                print("Incorrect current PIN!")

        elif choice == "5":
            print("For account-related enquiries, please contact your bank.")
            
        elif choice == "6":
            if len(transactions) == 0:
                print("No transactions yet.")
            else:
                print("===== TRANSACTION HISTORY =====")
                for transaction in transactions:
                    print(transaction)

        elif choice == "7":
            print("Thank you for using our ATM!")
            break

        else:
            print("Invalid choice! Please select 1 to 7.")



