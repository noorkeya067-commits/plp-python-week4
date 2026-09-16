age = int(input("Enter your age: "))

# Anyone 18 or older is eligible without parental consent.
if age >= 18:
    print("Welcome to the club!")

# Anyone under 18 must be at least 13 and have parental consent.
elif age >= 13 and age < 18:
    consent = input("Do you have parental consent? (yes/no): ").lower()

    # A person aged 13 to 17 is eligible if they have consent.
    if consent == "yes":
        print("Welcome to the club!")
    else:
        print("Sorry, you are not eligible yet.")

# Anyone younger than 13 is not eligible.
else:
    print("Sorry, you are not eligible yet.")