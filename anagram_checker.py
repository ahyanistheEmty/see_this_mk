def is_anagram(str1, str2):
    # Remove whitespace and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Anagrams must have the same length
    if len(str1) != len(str2):
        return False

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)

def main():
    print("--- Anagram Checker ---")
    string1 = input("Enter first string: ")
    string2 = input("Enter second string: ")

    if is_anagram(string1, string2):
        print(f"'{string1}' and '{string2}' are anagrams!")
    else:
        print(f"'{string1}' and '{string2}' are NOT anagrams.")

if __name__ == "__main__":
    main()
