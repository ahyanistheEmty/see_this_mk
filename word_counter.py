def count_words_and_chars(text):
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    return word_count, char_count

def main():
    print("--- Word and Character Counter ---")
    user_input = input("Enter the text you want to analyze: ")
    words, chars = count_words_and_chars(user_input)
    print(f"Word Count: {words}")
    print(f"Character Count: {chars}")

if __name__ == "__main__":
    main()
