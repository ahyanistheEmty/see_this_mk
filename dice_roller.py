import random

def roll_dice(sides=6, rolls=1):
    """
    Simulates rolling one or more dice with a specified number of sides.
    """
    results = [random.randint(1, sides) for _ in range(rolls)]
    return results

if __name__ == "__main__":
    print("--- Welcome to the Digital Dice Roller! ---")
    try:
        num_sides = int(input("Enter the number of sides on the dice (default 6): ") or 6)
        num_rolls = int(input("How many times do you want to roll? (default 1): ") or 1)
        
        outcomes = roll_dice(num_sides, num_rolls)
        
        if num_rolls == 1:
            print(f"You rolled a {num_sides}-sided die and got: {outcomes[0]}")
        else:
            print(f"You rolled {num_rolls} {num_sides}-sided dice and got: {outcomes}")
            print(f"Total sum: {sum(outcomes)}")
            
    except ValueError:
        print("Invalid input. Please enter numeric values.")
