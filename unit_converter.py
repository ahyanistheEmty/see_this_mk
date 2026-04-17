def unit_converter():
    print("--- Simple Unit Converter ---")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    
    choice = input("Choose a conversion (1-6): ")
    
    if choice == '1':
        km = float(input("Enter kilometers: "))
        print(f"{km} km is {km * 0.621371:.2f} miles")
    elif choice == '2':
        miles = float(input("Enter miles: "))
        print(f"{miles} miles is {miles / 0.621371:.2f} km")
    elif choice == '3':
        c = float(input("Enter Celsius: "))
        print(f"{c}°C is {(c * 9/5) + 32:.2f}°F")
    elif choice == '4':
        f = float(input("Enter Fahrenheit: "))
        print(f"{f}°F is {(f - 32) * 5/9:.2f}°C")
    elif choice == '5':
        kg = float(input("Enter kilograms: "))
        print(f"{kg} kg is {kg * 2.20462:.2f} lbs")
    elif choice == '6':
        lbs = float(input("Enter pounds: "))
        print(f"{lbs} lbs is {lbs / 2.20462:.2f} kg")
    else:
        print("Invalid choice")

if __name__ == "__main__":
    unit_converter()
