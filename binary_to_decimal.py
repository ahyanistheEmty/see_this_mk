def binary_to_decimal(binary_string):
    """Converts a binary string to its decimal equivalent."""
    try:
        return int(binary_string, 2)
    except ValueError:
        return "Invalid binary string"

def main():
    print("--- Binary to Decimal Converter ---")
    binary_val = input("Enter a binary number: ")
    decimal_val = binary_to_decimal(binary_val)
    
    if isinstance(decimal_val, int):
        print(f"The decimal equivalent of {binary_val} is {decimal_val}.")
    else:
        print(decimal_val)

if __name__ == "__main__":
    main()
