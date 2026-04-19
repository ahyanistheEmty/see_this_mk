import requests
import matplotlib.pyplot as plt

def fetch_crypto_prices():
    """Fetches current prices of a few cryptocurrencies from CoinGecko API."""
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        prices = {
            "Bitcoin": data['bitcoin']['usd'],
            "Ethereum": data['ethereum']['usd'],
            "Solana": data['solana']['usd']
        }
        return prices
    except Exception as e:
        print(f"Error fetching data: {e}")
        # Fallback data in case of API failure
        return {"Bitcoin": 60000, "Ethereum": 3000, "Solana": 150}

def visualize_prices(prices):
    """Creates a bar chart of the cryptocurrency prices."""
    names = list(prices.keys())
    values = list(prices.values())

    plt.figure(figsize=(10, 6))
    plt.bar(names, values, color=['gold', 'blue', 'purple'])
    plt.xlabel('Cryptocurrency')
    plt.ylabel('Price (USD)')
    plt.title('Current Cryptocurrency Prices')
    
    # Use log scale because BTC price dwarfs the others
    plt.yscale('log') 
    plt.ylabel('Price (USD) - Log Scale')

    plt.savefig('crypto_prices.png')
    print("Chart saved as crypto_prices.png")

if __name__ == "__main__":
    print("Fetching crypto prices...")
    crypto_data = fetch_crypto_prices()
    print(f"Data retrieved: {crypto_data}")
    print("Visualizing data...")
    visualize_prices(crypto_data)
