def is_palindrome(s):
    # Clean the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

def main():
    print("--- Palindrome Checker ---")
    text = input("Enter a word or phrase to check: ")
    if is_palindrome(text):
        print(f"'{text}' is a palindrome!")
    else:
        print(f"'{text}' is not a palindrome.")

if __name__ == "__main__":
    main()
