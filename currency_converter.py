def currency_converter():
    # Fixed exchange rates for simplicity
    rates = {
        'USD': 1.0,
        'EUR': 0.92,
        'GBP': 0.79,
        'JPY': 151.62,
        'INR': 83.38
    }
    
    print("Welcome to the Simple Currency Converter!")
    print("Available currencies: " + ", ".join(rates.keys()))
    
    try:
        amount = float(input("Enter the amount: "))
        from_currency = input("From currency (e.g., USD): ").upper()
        to_currency = input("To currency (e.g., EUR): ").upper()
        
        if from_currency in rates and to_currency in rates:
            # Convert amount to USD first, then to target currency
            usd_amount = amount / rates[from_currency]
            converted_amount = usd_amount * rates[to_currency]
            print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}")
        else:
            print("Invalid currency code entered.")
    except ValueError:
        print("Please enter a valid numerical amount.")

if __name__ == "__main__":
    currency_converter()
