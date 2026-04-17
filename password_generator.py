import random
import string

def generate_password(length=12):
    """Generates a random password with letters, digits, and punctuation."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

if __name__ == "__main__":
    try:
        user_length = int(input("Enter the desired password length: "))
        if user_length < 1:
            print("Please enter a positive number.")
        else:
            print(f"Your generated password is: {generate_password(user_length)}")
    except ValueError:
        print("Invalid input. Please enter a number.")
