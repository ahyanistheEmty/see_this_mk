import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_special=True):
    """Generates a random password based on specified criteria."""
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation

    if not chars:
        return "Error: No characters selected for password generation."

    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == "__main__":
    print("--- Simple Password Generator ---")
    try:
        pwd_length = int(input("Enter desired password length: ") or "12")
        upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        digits = input("Include numbers? (y/n): ").lower() == 'y'
        special = input("Include special characters? (y/n): ").lower() == 'y'
        
        password = generate_password(pwd_length, upper, digits, special)
        print(f"\nYour generated password is: {password}")
    except ValueError:
        print("Invalid input. Please enter a number for the length.")
