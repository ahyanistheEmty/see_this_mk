import random

def generate_quote():
    quotes = [
        "The only way to do great work is to love what you do. - Steve Jobs",
        "Innovation distinguishes between a leader and a follower. - Steve Jobs",
        "Stay hungry, stay foolish. - Steve Jobs",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "It does not matter how slowly you go as long as you do not stop. - Confucius",
        "Everything you've ever wanted is on the other side of fear. - George Addair",
        "Success is not final, failure is not fatal: it is the courage to continue that counts. - Winston Churchill",
        "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print("Your Random Quote of the Day:")
    print(generate_quote())
