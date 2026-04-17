def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    sequence = []
    a, b = 0, 1
    while len(sequence) < n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        num_terms = int(input("Enter the number of terms: "))
        if num_terms <= 0:
            print("Please enter a positive integer.")
        else:
            print(f"Fibonacci sequence ({num_terms} terms):")
            print(fibonacci(num_terms))
    except ValueError:
        print("Invalid input. Please enter an integer.")
