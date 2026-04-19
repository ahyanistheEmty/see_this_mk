import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    """Generates a random password based on specified criteria."""
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "Error: No characters selected for password."

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

if __name__ == "__main__":
    print("--- Simple Password Generator ---")
    try:
        pwd_length = int(input("Enter password length (default 12): ") or 12)
        include_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        include_special = input("Include special characters? (y/n, default y): ").lower() != 'n'
        
        generated_pwd = generate_password(pwd_length, include_digits, include_special)
        print(f"\nYour generated password is: {generated_pwd}")
    except ValueError:
        print("Invalid input. Please enter a number for the length.")
