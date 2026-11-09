import random
import string

def generate_password(length, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Please select at least one character type!"

    # Ensure at least one char from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Fill remaining length
    for _ in range(length - len(password)):
        password.append(random.choice(chars))

    random.shuffle(password)
    return ''.join(password)

def main():
    print("=== CODSOFT - PASSWORD GENERATOR ===\n")
    
    try:
        length = int(input("Enter password length (e.g., 8-16): "))
        if length < 4:
            print("Length should be at least 4!")
            return

        print("\nInclude? (y/n)")
        upper = input("Uppercase letters (A-Z)? [y]: ").lower() != 'n'
        lower = input("Lowercase letters (a-z)? [y]: ").lower() != 'n'
        digits = input("Numbers (0-9)? [y]: ").lower() != 'n'
        symbols = input("Symbols (!@#$)? [y]: ").lower() != 'n'

        password = generate_password(length, upper, lower, digits, symbols)
        
        print("\n" + "="*35)
        print(f"Generated Password: {password}")
        print("="*35)
        print(f"Length: {len(password)} | Strength: {'Strong' if len(password) >= 12 else 'Medium'}")

    except ValueError:
        print("Please enter a valid number!")

if __name__ == "__main__":
    main()