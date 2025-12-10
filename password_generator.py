import random
import string

def generate_password(num_letters, num_digits, num_symbols):
    # Pools
    letters = string.ascii_letters           # a-zA-Z
    digits = string.digits                   # 0-9
    symbols = "!@#$%^&*()-_=+[]{};:,.?/\\|"  # customize if you want

    # Build parts
    password_chars = []
    password_chars += random.choices(letters, k=num_letters)
    password_chars += random.choices(digits, k=num_digits)
    password_chars += random.choices(symbols, k=num_symbols)

    # Shuffle for randomness
    random.shuffle(password_chars)

    # Join into a string
    return "".join(password_chars)

def main():
    print("Password Generator")

    # Get user input
    while True:
        try:
            num_letters = int(input("How many letters should the password have? "))
            num_digits = int(input("How many digits should the password have? "))
            num_symbols = int(input("How many symbols should the password have? "))
            if num_letters < 0 or num_digits < 0 or num_symbols < 0:
                print("Please enter non-negative numbers.\n")
                continue
            break
        except ValueError:
            print("Please enter valid integers.\n")

    password = generate_password(num_letters, num_digits, num_symbols)
    total_length = num_letters + num_digits + num_symbols

    print(f"\nGenerated password ({total_length} characters):")
    print(password)

if __name__ == "__main__":
    main()
