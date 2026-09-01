# CODSOFT Python Programming Internship
# Task 3: Password Generator

import string
import random


def generate_password(length):
    characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = ''.join(random.choice(characters) for _ in range(length))

    return password


def main():
    print("==============================")
    print("      PASSWORD GENERATOR")
    print("==============================")

    while True:
        try:
            length = int(input("\nEnter password length: "))

            if length <= 0:
                print("Password length must be greater than zero.")
                continue

            password = generate_password(length)

            print("\nGenerated Password:")
            print(password)

            again = input("\nGenerate another password? (yes/no): ").lower()

            if again != "yes":
                print("Password generator closed.")
                break

        except ValueError:
            print("Please enter a valid number.")


if __name__ == "__main__":
    main()
